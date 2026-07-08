"""Entrena y guarda best models CNN + LSTM (solo docente) — Lab 3.

Uso local con GPU:
  bash labs/lab3/_install_torch_cuda.sh   # una vez
  python labs/lab3/_generar_modelos.py --device cuda

Codespaces / CPU:
  python labs/lab3/_generar_modelos.py
"""
from __future__ import annotations

import argparse
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader, TensorDataset
from torchvision import datasets, transforms
from torchvision.transforms import ColorJitter, Normalize, RandomHorizontalFlip, RandomRotation, Resize, ToTensor

LAB3 = Path(__file__).parent
P1 = LAB3 / "part_1"
P2 = LAB3 / "part_2"
sys.path.insert(0, str(P1))
sys.path.insert(0, str(P2))

from _modelo_cnn import CrackCNN, RUTA_META as CNN_META, RUTA_PT as CNN_PT  # noqa: E402
from _modelo_lstm import (  # noqa: E402
    FEATURES_DEFAULT,
    LSTMClassifier,
    StrainLSTM,
    RUTA_CLF_PT,
    RUTA_META as LSTM_META,
    RUTA_STRAIN_PT,
)

SEED = 42
IMAGE_SIZE = 128
FEATURES = FEATURES_DEFAULT
SEGMENTO_LEN = 120
GAP_INICIO, GAP_FIN = 40, 60
W_EXTRAP, HORIZONTE_EXTRAP = 80, 15

CNN_CONFIGS = [
    {"n_filters": 64, "dropout": 0.3, "lr": 1e-3, "use_batchnorm": True, "epochs": 15},
    {"n_filters": 32, "dropout": 0.3, "lr": 1e-3, "use_batchnorm": False, "epochs": 12},
]
LSTM_CONFIGS = [
    {"hidden": 128, "n_layers": 1, "dropout": 0.2, "lr": 1e-3, "epochs": 10},
    {"hidden": 64, "n_layers": 2, "dropout": 0.3, "lr": 1e-3, "epochs": 10},
]
STRAIN_CONFIGS = [
    {"hidden": 64, "epochs": 30},
    {"hidden": 48, "epochs": 25},
]


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Entrena modelos docente Lab 3")
    p.add_argument(
        "--device",
        default="auto",
        choices=("auto", "cuda", "cpu"),
        help="auto = cuda si está disponible",
    )
    p.add_argument("--cnn-batch", type=int, default=0, help="0 = 64 en GPU, 32 en CPU")
    return p.parse_args()


def pick_device(choice: str) -> torch.device:
    if choice == "cuda":
        if not torch.cuda.is_available():
            raise RuntimeError("CUDA no disponible. Ejecuta: bash labs/lab3/_install_torch_cuda.sh")
        return torch.device("cuda")
    if choice == "cpu":
        return torch.device("cpu")
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def set_seed() -> None:
    random.seed(SEED)
    np.random.seed(SEED)
    torch.manual_seed(SEED)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(SEED)


def _run_prep(script: Path) -> None:
    import importlib.util
    spec = importlib.util.spec_from_file_location("prep", script)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    mod.main()


def train_eval_epoch(
    model,
    loader,
    criterion,
    optimizer,
    device: torch.device,
    train: bool,
    use_amp: bool,
) -> tuple[float, float]:
    model.train(train)
    loss_sum, correct, total = 0.0, 0, 0
    scaler = torch.cuda.amp.GradScaler(enabled=use_amp)
    ctx = torch.enable_grad() if train else torch.no_grad()
    with ctx:
        for xb, yb in loader:
            xb, yb = xb.to(device, non_blocking=True), yb.to(device, non_blocking=True)
            if train:
                optimizer.zero_grad(set_to_none=True)
            with torch.cuda.amp.autocast(enabled=use_amp):
                logits = model(xb)
                loss = criterion(logits, yb)
            if train:
                scaler.scale(loss).backward()
                scaler.step(optimizer)
                scaler.update()
            loss_sum += loss.item() * xb.size(0)
            correct += (logits.argmax(1) == yb).sum().item()
            total += yb.size(0)
    return loss_sum / max(total, 1), correct / max(total, 1)


def cnn_loaders(batch_size: int, pin_memory: bool) -> tuple[DataLoader, DataLoader]:
    train_t = transforms.Compose([
        RandomHorizontalFlip(), RandomRotation(15), ColorJitter(0.2, 0.2),
        Resize((IMAGE_SIZE, IMAGE_SIZE)), ToTensor(),
        Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]),
    ])
    val_t = transforms.Compose([
        Resize((IMAGE_SIZE, IMAGE_SIZE)), ToTensor(),
        Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]),
    ])
    root = P1 / "data" / "cracks_subset"
    train_ds = datasets.ImageFolder(root / "train", transform=train_t)
    val_ds = datasets.ImageFolder(root / "val", transform=val_t)
    kw = {"num_workers": 2 if pin_memory else 0, "pin_memory": pin_memory}
    return (
        DataLoader(train_ds, batch_size=batch_size, shuffle=True, **kw),
        DataLoader(val_ds, batch_size=batch_size, shuffle=False, **kw),
    )


def tune_cnn(device: torch.device, batch_size: int) -> tuple[dict, float]:
    use_amp = device.type == "cuda"
    pin = device.type == "cuda"
    if device.type == "cuda":
        torch.backends.cudnn.benchmark = True
    best_acc, best = 0.0, {}
    train_loader, val_loader = cnn_loaders(batch_size, pin)
    for cfg in CNN_CONFIGS:
        model = CrackCNN(cfg["n_filters"], cfg["dropout"], cfg["use_batchnorm"]).to(device)
        opt = torch.optim.Adam(model.parameters(), lr=cfg["lr"])
        crit = nn.CrossEntropyLoss()
        best_ep_acc, best_state = 0.0, None
        for ep in range(cfg["epochs"]):
            tl, ta = train_eval_epoch(model, train_loader, crit, opt, device, True, use_amp)
            vl, va = train_eval_epoch(model, val_loader, crit, opt, device, False, use_amp)
            best_ep_acc = max(best_ep_acc, va)
            if va >= best_ep_acc:
                best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            print(
                f"    ep {ep+1}/{cfg['epochs']} | train {ta:.3f} val {va:.3f} | loss {tl:.3f}/{vl:.3f}",
                flush=True,
            )
        print(f"  CNN f={cfg['n_filters']} bn={cfg['use_batchnorm']} → best val={best_ep_acc:.3f}", flush=True)
        if best_ep_acc > best_acc and best_state is not None:
            best_acc = best_ep_acc
            best = {**cfg, "val_accuracy": round(best_ep_acc, 4), "state_dict": best_state}
        if best_acc >= 0.90:
            break
    if best_acc < 0.70:
        raise RuntimeError(f"CNN best val_acc={best_acc:.3f} demasiado bajo")
    if best_acc < 0.85:
        print(f"⚠️ CNN val_acc={best_acc:.3f} < 0.85 objetivo; se guarda igual.", flush=True)
    return best, best_acc


def lstm_loaders(window_size: int, batch_size: int, pin_memory: bool) -> tuple[DataLoader, DataLoader]:
    csv = P2 / "data" / "building_health_monitoring_dataset.csv"
    df = pd.read_csv(csv).dropna(subset=FEATURES).sort_values("Timestamp")
    X = StandardScaler().fit_transform(df[FEATURES].values)
    y = df["Condition Label"].values.astype(int)
    seqs, labels = [], []
    for i in range(window_size, len(X)):
        seqs.append(X[i - window_size : i])
        labels.append(y[i])
    X_arr = np.array(seqs, dtype=np.float32)
    y_arr = np.array(labels, dtype=np.int64)
    cut = int(0.8 * len(X_arr))
    train_ds = TensorDataset(torch.from_numpy(X_arr[:cut]), torch.from_numpy(y_arr[:cut]))
    val_ds = TensorDataset(torch.from_numpy(X_arr[cut:]), torch.from_numpy(y_arr[cut:]))
    kw = {"pin_memory": pin_memory}
    return (
        DataLoader(train_ds, batch_size=batch_size, shuffle=True, **kw),
        DataLoader(val_ds, batch_size=batch_size, shuffle=False, **kw),
    )


def tune_lstm_classifier(device: torch.device, batch_size: int) -> tuple[dict, float]:
    use_amp = device.type == "cuda"
    pin = device.type == "cuda"
    best_acc, best = 0.0, {}
    train_loader, val_loader = lstm_loaders(30, batch_size, pin)
    for cfg in LSTM_CONFIGS:
        model = LSTMClassifier(5, cfg["hidden"], cfg["n_layers"], cfg["dropout"]).to(device)
        opt = torch.optim.Adam(model.parameters(), lr=cfg["lr"])
        crit = nn.CrossEntropyLoss()
        best_ep_acc, best_state = 0.0, None
        for ep in range(cfg["epochs"]):
            tl, ta = train_eval_epoch(model, train_loader, crit, opt, device, True, use_amp)
            vl, va = train_eval_epoch(model, val_loader, crit, opt, device, False, use_amp)
            best_ep_acc = max(best_ep_acc, va)
            if va >= best_ep_acc:
                best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            print(f"    ep {ep+1}/{cfg['epochs']} | train {ta:.3f} val {va:.3f}", flush=True)
        print(f"  LSTM h={cfg['hidden']} L={cfg['n_layers']} → best val={best_ep_acc:.3f}", flush=True)
        if best_ep_acc > best_acc and best_state is not None:
            best_acc = best_ep_acc
            best = {
                "input_size": 5,
                "hidden_size": cfg["hidden"],
                "n_layers": cfg["n_layers"],
                "dropout": cfg["dropout"],
                "learning_rate": cfg["lr"],
                "epochs": cfg["epochs"],
                "val_accuracy": round(best_ep_acc, 4),
                "state_dict": best_state,
            }
        if best_acc >= 0.80:
            break
    if best_acc < 0.65:
        raise RuntimeError(f"LSTM clf best val_acc={best_acc:.3f} < 0.65")
    return best, best_acc


def eval_strain_mae(model: StrainLSTM, serie: np.ndarray, device: torch.device) -> tuple[float, float]:
    model.eval()

    def interp_mae() -> float:
        seg = serie[200 : 200 + SEGMENTO_LEN].copy()
        entrada = seg.copy()
        entrada[GAP_INICIO:GAP_FIN] = 0.0
        x = torch.tensor(entrada[:, None], dtype=torch.float32).unsqueeze(0).to(device)
        with torch.no_grad():
            pred = model(x).squeeze().cpu().numpy()
        return float(np.mean(np.abs(seg[GAP_INICIO:GAP_FIN] - pred[GAP_INICIO:GAP_FIN])))

    def extrap_mae() -> float:
        hist = serie[300 : 300 + W_EXTRAP]
        fut = serie[300 + W_EXTRAP : 300 + W_EXTRAP + HORIZONTE_EXTRAP]
        x = torch.tensor(hist[:, None], dtype=torch.float32).unsqueeze(0).to(device)
        with torch.no_grad():
            pred = model(x).squeeze().cpu().numpy()[-HORIZONTE_EXTRAP:]
        return float(np.mean(np.abs(fut - pred)))

    return interp_mae(), extrap_mae()


def train_strain_lstm(serie: np.ndarray, device: torch.device) -> tuple[dict, float, float]:
    best = {"mae_interp": 999.0}
    chunks = [serie[s : s + SEGMENTO_LEN] for s in range(0, len(serie) - SEGMENTO_LEN - 1, 8)]
    X_all = torch.tensor(np.array(chunks)[:, :, None], dtype=torch.float32).to(device)
    for cfg in STRAIN_CONFIGS:
        model = StrainLSTM(cfg["hidden"]).to(device)
        opt = torch.optim.Adam(model.parameters(), lr=1e-3)
        loss_fn = nn.MSELoss()
        model.train()
        for ep in range(cfg["epochs"]):
            opt.zero_grad(set_to_none=True)
            pred = model(X_all)
            loss = loss_fn(pred, X_all)
            loss.backward()
            opt.step()
            if (ep + 1) % 10 == 0:
                print(f"    StrainLSTM ep {ep+1}/{cfg['epochs']} loss={loss.item():.4f}", flush=True)
        mi, me = eval_strain_mae(model, serie, device)
        print(f"  StrainLSTM h={cfg['hidden']} → mae_i={mi:.3f} mae_e={me:.3f}", flush=True)
        if mi < best["mae_interp"]:
            best = {
                "hidden": cfg["hidden"],
                "epochs": cfg["epochs"],
                "mae_interp": round(mi, 4),
                "mae_extrap": round(me, 4),
                "state_dict": {k: v.cpu().clone() for k, v in model.state_dict().items()},
            }
    return best, best["mae_interp"], best["mae_extrap"]


def save_checkpoint(path: Path, state_dict: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    torch.save({"state_dict": state_dict}, path)


def main() -> None:
    args = parse_args()
    set_seed()
    device = pick_device(args.device)
    batch = args.cnn_batch or (64 if device.type == "cuda" else 32)
    print(f"▶ device={device} | batch={batch}", flush=True)
    if device.type == "cuda":
        print(f"   GPU: {torch.cuda.get_device_name(0)}", flush=True)

    print("▶ Preparando datos…", flush=True)
    _run_prep(P1 / "_preparar_datos.py")
    _run_prep(P2 / "_preparar_datos.py")

    print("▶ Tuning CNN…", flush=True)
    cnn_best, cnn_acc = tune_cnn(device, batch)
    cnn_state = cnn_best.pop("state_dict")
    save_checkpoint(CNN_PT, cnn_state)
    hp_cnn = {
        "n_filters": cnn_best.get("n_filters"),
        "dropout": cnn_best.get("dropout"),
        "use_batchnorm": cnn_best.get("use_batchnorm"),
        "learning_rate": cnn_best.get("lr"),
    }
    CNN_META.write_text(json.dumps({
        "tipo": "CrackCNN",
        "hyperparameters": hp_cnn,
        "val_accuracy": cnn_acc,
        "image_size": IMAGE_SIZE,
        "device_trained": str(device),
        "trained_at": datetime.now(timezone.utc).isoformat(),
    }, indent=2), encoding="utf-8")
    print(f"✅ CNN: {CNN_PT} acc={cnn_acc:.3f}", flush=True)

    print("▶ Tuning LSTM classifier…", flush=True)
    lstm_best, lstm_acc = tune_lstm_classifier(device, batch)
    lstm_state = lstm_best.pop("state_dict")
    save_checkpoint(RUTA_CLF_PT, lstm_state)

    print("▶ Tuning StrainLSTM…", flush=True)
    df = pd.read_csv(P2 / "data" / "building_health_monitoring_dataset.csv")
    strain = df["Strain (με)"].dropna().values.astype(np.float32)
    strain_norm = (strain - strain.mean()) / (strain.std() + 1e-8)
    strain_best, mae_i, mae_e = train_strain_lstm(strain_norm, device)
    strain_state = strain_best.pop("state_dict")
    save_checkpoint(RUTA_STRAIN_PT, strain_state)

    LSTM_META.write_text(json.dumps({
        "classifier": {
            "tipo": "LSTMClassifier",
            "hyperparameters": {k: v for k, v in lstm_best.items() if k != "state_dict"},
            "val_accuracy": lstm_acc,
        },
        "strain_regressor": {
            "tipo": "StrainLSTM",
            "hyperparameters": {k: v for k, v in strain_best.items() if k != "state_dict"},
            "mae_interp": mae_i,
            "mae_extrap": mae_e,
        },
        "device_trained": str(device),
        "trained_at": datetime.now(timezone.utc).isoformat(),
    }, indent=2), encoding="utf-8")
    print(f"✅ LSTM clf: {RUTA_CLF_PT} acc={lstm_acc:.3f}", flush=True)
    print(f"✅ StrainLSTM: {RUTA_STRAIN_PT} mae_i={mae_i:.3f} mae_e={mae_e:.3f}", flush=True)
    print("✅ Todos los modelos Lab 3 listos.", flush=True)


if __name__ == "__main__":
    main()

"""Autoevaluación amigable para Lab 3 Parte 1 — CNN grietas en hormigón."""

from __future__ import annotations

CLASES_ESPERADAS = ("Negative", "Positive")
N_TRAIN_POR_CLASE = 800
N_VAL_POR_CLASE = 200
N_CLASES = 2
MIN_ACC_VAL = 0.75
MIN_ACC_VAL_ALUMNO = 0.60
MAX_EPOCHS_ALUMNO = 5
MIN_COMPONENTES_CNN = 4


def verificar(condicion: bool, ok: str, fail: str) -> bool:
    print(ok if condicion else fail)
    return condicion


def resumen_seccion(nombre: str, resultados: list[bool]) -> None:
    if all(resultados):
        print(f"\n✅ Sección {nombre} completada. Puedes continuar.")
    else:
        print(
            f"\n❌ Sección {nombre}: revisa tu celda «Aquí coloca tu solución» "
            "y vuelve a ejecutar."
        )


def _norm_componente(nombre: str) -> str:
    return nombre.strip().lower().replace(" ", "_")


def verificar_panorama_cnn(componentes: list[str]) -> list[bool]:
    if isinstance(componentes, str):
        componentes = [componentes]
    norm = [_norm_componente(c) for c in componentes]

    def tiene(*palabras: str) -> bool:
        return any(any(p in t for p in palabras) for t in norm)

    r = []
    r.append(
        verificar(
            len(norm) >= MIN_COMPONENTES_CNN,
            f"✅ Panorama CNN con {len(norm)} componentes listados.",
            f"❌ Define COMPONENTES_CNN con al menos {MIN_COMPONENTES_CNN} entradas.",
        )
    )
    r.append(
        verificar(
            tiene("conv", "convol"),
            "✅ Incluye capa de **convolución**.",
            "❌ Añade 'convolución' o 'conv' a COMPONENTES_CNN.",
        )
    )
    r.append(
        verificar(
            tiene("pool", "pooling"),
            "✅ Incluye **pooling**.",
            "❌ Añade 'pooling' a COMPONENTES_CNN.",
        )
    )
    r.append(
        verificar(
            tiene("relu", "activ"),
            "✅ Incluye **activación** (p. ej. ReLU).",
            "❌ Añade 'relu' o 'activación' a COMPONENTES_CNN.",
        )
    )
    return r


def verificar_eda_dataset(
    conteos: dict,
    n_ejemplos_mosaico: int,
    n_muestras_eda: int,
) -> list[bool]:
    r = []
    r.append(
        verificar(
            set(conteos.keys()) == {"train", "val"},
            "✅ Splits train y val identificados.",
            f"❌ conteos debe tener claves 'train' y 'val'; obtuviste {list(conteos.keys())}.",
        )
    )
    for split, n_esperado in (("train", N_TRAIN_POR_CLASE), ("val", N_VAL_POR_CLASE)):
        clases = conteos.get(split, {})
        r.append(
            verificar(
                set(clases.keys()) == set(CLASES_ESPERADAS)
                and all(clases.get(c, 0) == n_esperado for c in CLASES_ESPERADAS),
                f"✅ {split}: {n_esperado} imágenes por clase (Negative/Positive).",
                f"❌ {split}: esperado {n_esperado}×2 clases; obtuviste {clases}.",
            )
        )
    r.append(
        verificar(
            2 <= n_ejemplos_mosaico <= 8,
            f"✅ Mosaico con {n_ejemplos_mosaico} ejemplos por clase.",
            "❌ N_EJEMPLOS_MOSAICO debe estar entre 2 y 8.",
        )
    )
    r.append(
        verificar(
            20 <= n_muestras_eda <= 200,
            f"✅ EDA sobre {n_muestras_eda} imágenes (tamaños / balance).",
            "❌ N_MUESTRAS_EDA debe estar entre 20 y 200.",
        )
    )
    return r


def verificar_augmentation(
    image_size: int,
    aug_rotation: float,
    train_transform,
    val_transform,
    n_aug_mostrados: int,
) -> list[bool]:
    from torchvision.transforms import Compose

    r = []
    r.append(
        verificar(
            64 <= image_size <= 227,
            f"✅ IMAGE_SIZE={image_size} para resize y entrenamiento.",
            "❌ IMAGE_SIZE debe estar entre 64 y 227.",
        )
    )
    r.append(
        verificar(
            5 <= aug_rotation <= 45,
            f"✅ AUG_ROTATION={aug_rotation}° en rango razonable.",
            "❌ AUG_ROTATION debe estar entre 5 y 45 grados.",
        )
    )
    r.append(
        verificar(
            isinstance(train_transform, Compose) and isinstance(val_transform, Compose),
            "✅ train_transform y val_transform definidos (Compose).",
            "❌ Define train_transform (con aumento) y val_transform (determinista).",
        )
    )
    train_names = {t.__class__.__name__ for t in train_transform.transforms}
    r.append(
        verificar(
            any("Random" in n for n in train_names),
            f"✅ train_transform incluye aumento aleatorio ({sorted(train_names)}).",
            "❌ train_transform debe incluir al menos un Random* (flip, rotación, jitter…).",
        )
    )
    val_names = {t.__class__.__name__ for t in val_transform.transforms}
    r.append(
        verificar(
            not any("Random" in n for n in val_names),
            "✅ val_transform sin aleatoriedad (solo resize/normalize).",
            "❌ val_transform no debe incluir transforms Random*.",
        )
    )
    r.append(
        verificar(
            3 <= n_aug_mostrados <= 8,
            f"✅ {n_aug_mostrados} variantes aumentadas visualizadas.",
            "❌ N_AUG_MOSTRADOS debe estar entre 3 y 8.",
        )
    )
    return r


def verificar_dataloaders(
    batch_size: int,
    train_loader,
    val_loader,
    image_size: int | None = None,
) -> list[bool]:
    r = []
    if image_size is not None:
        r.append(
            verificar(
                64 <= image_size <= 227,
                f"✅ IMAGE_SIZE={image_size} coherente con los loaders.",
                "❌ IMAGE_SIZE debe estar entre 64 y 227.",
            )
        )
    r.append(
        verificar(
            8 <= batch_size <= 64,
            f"✅ BATCH_SIZE={batch_size} en rango razonable.",
            "❌ BATCH_SIZE debe estar entre 8 y 64.",
        )
    )
    try:
        xb, yb = next(iter(train_loader))
        r.append(
            verificar(
                xb.ndim == 4
                and xb.shape[1] == 3
                and xb.shape[2] == image_size
                and xb.shape[3] == image_size,
                f"✅ Batch train: {tuple(xb.shape)} (N×3×H×W).",
                f"❌ Forma de batch inesperada: {tuple(xb.shape)}.",
            )
        )
        r.append(
            verificar(
                yb.ndim == 1 and yb.shape[0] == xb.shape[0],
                f"✅ Etiquetas alineadas con batch (n={yb.shape[0]}).",
                "❌ Las etiquetas no coinciden con el tamaño del batch.",
            )
        )
        r.append(
            verificar(
                len(val_loader) >= 1,
                f"✅ val_loader listo ({len(val_loader)} batches).",
                "❌ val_loader vacío — revisa data/cracks_subset/val.",
            )
        )
    except Exception as exc:
        r.append(verificar(False, "", f"❌ Error al iterar train_loader: {exc}"))
    return r


def verificar_arquitectura(modelo, n_filters: int, dropout: float) -> list[bool]:
    import torch.nn as nn

    conv_layers = [m for m in modelo.modules() if isinstance(m, nn.Conv2d)]
    linear_layers = [m for m in modelo.modules() if isinstance(m, nn.Linear)]

    r = []
    r.append(
        verificar(
            8 <= n_filters <= 128,
            f"✅ N_FILTERS={n_filters} en rango válido.",
            "❌ N_FILTERS debe estar entre 8 y 128.",
        )
    )
    r.append(
        verificar(
            0.0 <= dropout <= 0.6,
            f"✅ DROPOUT={dropout} configurado.",
            "❌ DROPOUT debe estar entre 0.0 y 0.6.",
        )
    )
    r.append(
        verificar(
            len(conv_layers) >= 2,
            f"✅ CNN con {len(conv_layers)} capas convolucionales.",
            "❌ El modelo debe tener al menos 2 capas Conv2d.",
        )
    )
    out_features = getattr(linear_layers[-1], "out_features", None) if linear_layers else None
    r.append(
        verificar(
            out_features == N_CLASES,
            f"✅ Capa de salida con {N_CLASES} neuronas (Negative/Positive).",
            f"❌ La última Linear debe tener out_features=2; obtuviste {out_features}.",
        )
    )
    return r


def verificar_entrenamiento(
    history: dict,
    n_epochs: int,
    learning_rate: float,
) -> list[bool]:
    r = []
    keys = {"train_loss", "val_loss", "train_acc", "val_acc"}
    r.append(
        verificar(
            keys.issubset(history.keys()),
            "✅ history con train/val loss y accuracy.",
            f"❌ history debe incluir {sorted(keys)}.",
        )
    )
    max_ep = MAX_EPOCHS_ALUMNO
    r.append(
        verificar(
            1 <= n_epochs <= max_ep,
            f"✅ N_EPOCHS={n_epochs} (entrenamiento corto en CPU).",
            f"❌ N_EPOCHS debe estar entre 1 y {max_ep} para el modelo alumno.",
        )
    )
    r.append(
        verificar(
            1e-4 <= learning_rate <= 0.1,
            f"✅ LEARNING_RATE={learning_rate}.",
            "❌ LEARNING_RATE debe estar entre 1e-4 y 0.1.",
        )
    )
    if keys.issubset(history.keys()):
        r.append(
            verificar(
                len(history["train_loss"]) == n_epochs,
                f"✅ {n_epochs} épocas registradas en history.",
                "❌ La longitud de history no coincide con N_EPOCHS.",
            )
        )
        if len(history["train_loss"]) >= 2:
            loss_baja = history["train_loss"][-1] <= history["train_loss"][0]
            r.append(
                verificar(
                    loss_baja,
                    "✅ Pérdida de entrenamiento no aumentó respecto a la 1.ª época.",
                    "❌ La loss de train subió — revisa LR, arquitectura o datos.",
                )
            )
        acc_val = history["val_acc"][-1] if history["val_acc"] else 0.0
        min_acc = MIN_ACC_VAL_ALUMNO
        r.append(
            verificar(
                acc_val >= min_acc,
                f"✅ Accuracy en validación = {acc_val:.3f} (≥ {min_acc:.2f}, modelo corto).",
                f"❌ Accuracy val {acc_val:.3f} < {min_acc:.2f}. Revisa LR o arquitectura.",
            )
        )
    return r


def verificar_modelo_docente_cargado(acc_docente: float, min_acc: float = 0.85) -> list[bool]:
    r = [
        verificar(
            acc_docente >= min_acc,
            f"✅ Checkpoint docente cargado (acc ref = {acc_docente:.3f}).",
            "❌ Falta crack_cnn_best.pt — docente: python labs/lab3/_generar_modelos.py",
        )
    ]
    return r


def verificar_comparacion_docente(
    acc_alumno: float,
    acc_docente: float,
    n_epochs_alumno: int,
    n_epochs_docente: int,
) -> list[bool]:
    r = []
    r.append(
        verificar(
            1 <= n_epochs_alumno <= MAX_EPOCHS_ALUMNO,
            f"✅ Comparaste tu modelo ({n_epochs_alumno} ép.) con el docente ({n_epochs_docente} ép.).",
            f"❌ N_EPOCHS alumno debe estar entre 1 y {MAX_EPOCHS_ALUMNO}.",
        )
    )
    r.append(
        verificar(
            acc_docente >= acc_alumno,
            f"✅ Modelo docente ({acc_docente:.3f}) ≥ tu modelo ({acc_alumno:.3f}) — "
            "más épocas e hiperparámetros afinados.",
            f"❌ Se esperaba acc_docente ≥ acc_alumno ({acc_docente:.3f} vs {acc_alumno:.3f}).",
        )
    )
    return r


def verificar_curvas(history: dict, n_epochs: int) -> list[bool]:
    r = []
    for key in ("train_loss", "val_loss", "train_acc", "val_acc"):
        serie = history.get(key, [])
        r.append(
            verificar(
                isinstance(serie, list) and len(serie) == n_epochs,
                f"✅ Curva «{key}» con {len(serie)} puntos.",
                f"❌ «{key}» debe tener longitud {n_epochs}.",
            )
        )
    return r


def verificar_metricas(acc_val: float, cm) -> list[bool]:
    import numpy as np

    cm_arr = np.asarray(cm)
    r = []
    r.append(
        verificar(
            cm_arr.shape == (2, 2),
            "✅ Matriz de confusión 2×2 (Negative / Positive).",
            f"❌ Matriz de confusión debe ser 2×2; forma {cm_arr.shape}.",
        )
    )
    r.append(
        verificar(
            acc_val >= MIN_ACC_VAL,
            f"✅ Accuracy en validación = {acc_val:.3f}.",
            f"❌ Accuracy {acc_val:.3f} < {MIN_ACC_VAL:.2f}.",
        )
    )
    return r


def verificar_casos_locales(n_casos_mostrados: int) -> list[bool]:
    return [
        verificar(
            n_casos_mostrados >= 1,
            f"✅ {n_casos_mostrados} caso(s) local(es) visualizado(s).",
            "❌ Muestra al menos 1 imagen con predicción vs etiqueta real.",
        )
    ]

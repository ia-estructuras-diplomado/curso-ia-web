"""Autoevaluación amigable para Lab 4 Parte 2 — xAI en redes neuronales."""

from __future__ import annotations

from pathlib import Path

RUTA_CNN = Path(__file__).resolve().parents[2] / "lab3" / "part_1" / "data" / "crack_cnn_best.pt"
RUTA_LSTM = Path(__file__).resolve().parents[2] / "lab3" / "part_2" / "data" / "lstm_classifier_best.pt"
MIN_ACC_CNN = 0.75
MIN_ACC_LSTM = 0.65


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


def verificar_panorama_xai_redes(tecnicas: list[str]) -> list[bool]:
    if isinstance(tecnicas, str):
        tecnicas = [tecnicas]
    norm = [t.strip().lower() for t in tecnicas]
    r = []
    r.append(
        verificar(
            len(norm) >= 3,
            f"✅ Panorama xAI redes con {len(norm)} técnicas.",
            "❌ Lista al menos 3 técnicas (grad_cam, integrated_gradients, etc.).",
        )
    )
    r.append(
        verificar(
            any("grad" in t or "cam" in t for t in norm),
            "✅ Incluye explicación visual para CNN (Grad-CAM).",
            "❌ Añade 'grad_cam' o similar.",
        )
    )
    r.append(
        verificar(
            any("integrated" in t or "atrib" in t for t in norm),
            "✅ Incluye atribución temporal (Integrated Gradients).",
            "❌ Añade 'integrated_gradients' o 'atribución'.",
        )
    )
    return r


def verificar_modelos_lab3(cnn_ok: bool, lstm_ok: bool) -> list[bool]:
    r = []
    r.append(
        verificar(
            RUTA_CNN.is_file() or cnn_ok,
            f"✅ CNN de Lab 3 disponible ({RUTA_CNN.name}).",
            f"❌ Falta {RUTA_CNN}. Ejecuta: python labs/lab3/_generar_modelos.py",
        )
    )
    r.append(
        verificar(
            RUTA_LSTM.is_file() or lstm_ok,
            f"✅ LSTM de Lab 3 disponible ({RUTA_LSTM.name}).",
            f"❌ Falta {RUTA_LSTM}. Ejecuta: python labs/lab3/_generar_modelos.py",
        )
    )
    return r


def verificar_gradcam(cam_shape: tuple, img_shape: tuple) -> list[bool]:
    r = []
    r.append(
        verificar(
            len(cam_shape) == 2 and cam_shape[0] > 0 and cam_shape[1] > 0,
            f"✅ Mapa Grad-CAM con forma {cam_shape}.",
            f"❌ Grad-CAM con forma inválida: {cam_shape}.",
        )
    )
    r.append(
        verificar(
            cam_shape[0] == img_shape[0] and cam_shape[1] == img_shape[1],
            "✅ Heatmap alineado con la imagen de entrada.",
            f"❌ CAM {cam_shape} no coincide con imagen {img_shape}.",
        )
    )
    return r


def verificar_atribucion_lstm(top_feature: str, n_atrib: int) -> list[bool]:
  features_ok = {
        "Accel_X (m/s^2)", "Accel_Y (m/s^2)", "Accel_Z (m/s^2)",
        "Strain (με)", "Temp (°C)",
    }
    r = []
    r.append(
        verificar(
            top_feature in features_ok,
            f"✅ Feature más atribuida: «{top_feature}».",
            f"❌ top_feature debe ser un sensor válido; obtuviste «{top_feature}».",
        )
    )
    r.append(
        verificar(
            n_atrib == 5,
            "✅ Atribución sobre 5 sensores.",
            f"❌ Se esperaban 5 atribuciones; hay {n_atrib}.",
        )
    )
    return r


def verificar_metricas_cnn(acc_val: float) -> list[bool]:
    return [
        verificar(
            acc_val >= MIN_ACC_CNN,
            f"✅ Accuracy CNN en val = {acc_val:.3f}.",
            f"❌ Accuracy CNN {acc_val:.3f} < {MIN_ACC_CNN}.",
        )
    ]


def verificar_metricas_lstm(acc_val: float) -> list[bool]:
    return [
        verificar(
            acc_val >= MIN_ACC_LSTM,
            f"✅ Accuracy LSTM en val = {acc_val:.3f}.",
            f"❌ Accuracy LSTM {acc_val:.3f} < {MIN_ACC_LSTM}.",
        )
    ]

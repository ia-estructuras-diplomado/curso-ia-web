# Lab 4: Redes Neuronales — CNN y RNN/LSTM

--8<-- "lab4-actions.md"

!!! info "Sesión 5"
    **Duración:** ~4 h · Dos partes · Vía IA-asistida

## Partes

| Parte | Tema | Carpeta | Notebook |
|-------|------|---------|----------|
| **1** | CNN — grietas en hormigón | `part_1/` | `cnn_grietas_estructuras_alumno_ia.ipynb` |
| **2** | LSTM — sensores SHM | `part_2/` | `rnn_sensores_estructuras_alumno_ia.ipynb` |

## Objetivos

1. Entrenar una **CNN** para clasificación de imágenes de patología.
2. Entrenar **LSTM** para series de sensores (ventanas temporales).
3. Comparar costos (datos, cómputo, interpretabilidad) frente a Labs 1–2.

## PyTorch

Si falta `torchvision` o hay error `SymInt`:

```bash
bash labs/lab5/_fix_pytorch.sh

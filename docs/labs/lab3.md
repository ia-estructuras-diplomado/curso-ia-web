# Lab 3: Redes Neuronales — CNN y RNN/LSTM

--8<-- "lab3-actions.md"

!!! info "Sesión 4"
    **Duración:** ~4 h · Dos partes · Vía IA-asistida

## Partes

| Parte | Tema | Carpeta | Notebook |
|-------|------|---------|----------|
| **1** | CNN — grietas en hormigón | `part_1/` | `cnn_grietas_estructuras_alumno_ia.ipynb` |
| **2** | LSTM — sensores SHM | `part_2/` | `rnn_sensores_estructuras_alumno_ia.ipynb` |

## Modelos docente

Checkpoints en `part_1/data/crack_cnn_best.pt` y `part_2/data/lstm_*.pt`. Generar con:

```bash
python labs/lab3/_generar_modelos.py
```

## Objetivos

1. Entrenar o cargar una **CNN** para clasificación de grietas.
2. Entrenar o cargar **LSTM** para series de sensores.
3. Comparar costos frente a modelos clásicos (Labs 1–2).

## PyTorch

```bash
bash labs/lab5/_fix_pytorch.sh
```

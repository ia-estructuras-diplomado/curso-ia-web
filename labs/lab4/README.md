# Lab 4 — Redes neuronales en ingeniería estructural

Dos partes complementarias con el mismo entorno `labs/.venv` (PyTorch CPU).

| Parte | Tema | Carpeta | Notebook alumno |
|-------|------|---------|-----------------|
| **1** | CNN — grietas en hormigón (imágenes) | [`part_1/`](part_1/) | `cnn_grietas_estructuras_alumno_ia.ipynb` |
| **2** | LSTM — sensores SHM (series temporales) | [`part_2/`](part_2/) | `rnn_sensores_estructuras_alumno_ia.ipynb` |

## Estado

**✅ Ambas partes completas** (vía IA-asistida).

## Inicio rápido (Codespaces)

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
```

- **Parte 1:** `cd labs/lab4/part_1` → abrir notebook CNN (~10–15 min CPU).
- **Parte 2:** `cd labs/lab4/part_2` → abrir notebook LSTM (~10 min CPU).

## Diferencia pedagógica

| | Parte 1 (CNN) | Parte 2 (LSTM) |
|---|---------------|----------------|
| Datos | Imágenes de grietas | Sensores 1 Hz (mismo CSV que Labs 1–3) |
| EDA | Mosaico de fotos | **Gráficos de series temporales** |
| Modelo | Convolución espacial | Memoria temporal (ventanas) |
| Extra | Matriz de confusión | **Interpolación vs extrapolación** en Strain |

## PyTorch compartido

Si falta `torchvision` o hay error `SymInt`:

```bash
bash labs/lab5/_fix_pytorch.sh
# o: rm -rf labs/.venv && bash labs/setup.sh
```

Guía del curso: [Lab 4 en curso-ia-web](https://ia-estructuras-diplomado.github.io/curso-ia-web/labs/lab4/)

Ver [`../GUIA_LABORATORIOS.md`](../GUIA_LABORATORIOS.md)

# Lab 3 — Redes neuronales en ingeniería estructural

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web?quickstart=1&devcontainer_path=.devcontainer%2Fdevcontainer.json)

> **Un solo Codespace para todo el curso.** Todos los labs comparten `labs/.venv`.

**Sesión 4** · CNN (grietas) + LSTM (sensores SHM) con PyTorch CPU.

| Parte | Tema | Carpeta | Notebook alumno |
|-------|------|---------|-----------------|
| **1** | CNN — grietas en hormigón | [`part_1/`](part_1/) | `cnn_grietas_estructuras_alumno_ia.ipynb` |
| **2** | LSTM — sensores SHM | [`part_2/`](part_2/) | `rnn_sensores_estructuras_alumno_ia.ipynb` |

## Modelos docente (best)

Entrenamiento **solo docente** con script Python (no notebook):

```bash
# Local con GPU NVIDIA (recomendado)
bash labs/lab3/_install_torch_cuda.sh   # una vez: torch+cu124
python labs/lab3/_generar_modelos.py --device cuda

# Codespaces / CPU
python labs/lab3/_generar_modelos.py
```

Artefactos generados:
- `part_1/data/crack_cnn_best.pt` + `model_meta.json`
- `part_2/data/lstm_classifier_best.pt`, `lstm_strain_best.pt` + `model_meta.json`

Los alumnos **cargan** estos checkpoints en el notebook; no necesitan entrenar 15 épocas en CPU.

## Codespaces

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/lab3/part_1   # o part_2
```

Guía: [Lab 3 en curso-ia-web](https://ia-estructuras-diplomado.github.io/curso-ia-web/labs/lab3/)

Ver [`../GUIA_LABORATORIOS.md`](../GUIA_LABORATORIOS.md)

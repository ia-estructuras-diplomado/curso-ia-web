# Lab 4: Redes Neuronales — CNN y LSTM

--8<-- "lab4-actions.md"

!!! info "Dos partes"
    Mismo entorno `labs/.venv` (PyTorch CPU).

## Partes

| Parte | Tema | Notebook |
|-------|------|----------|
| **1** | CNN — grietas en hormigón (imágenes) | [`part_1/cnn_grietas_estructuras.ipynb`](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab4/part_1/cnn_grietas_estructuras.ipynb) |
| **2** | LSTM — sensores SHM (series temporales) | [`part_2/rnn_sensores_estructuras.ipynb`](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab4/part_2/rnn_sensores_estructuras.ipynb) |

## Objetivos

1. Entrenar una **CNN** para clasificar grietas en imágenes de hormigón.
2. Entrenar una **LSTM** sobre series de sensores SHM.
3. Comparar costo y desempeño frente a los modelos clásicos de los Labs 1–3.

## Si falta `torchvision` o aparece un error `SymInt`

```bash
bash labs/_install_torch_cpu.sh                                   # Linux/macOS
powershell -ExecutionPolicy Bypass -File labs\_install_torch_cpu.ps1  # Windows
```

---

**¿Dudas?** → [Instalación](instalacion.md) · [FAQ](../faq.md)

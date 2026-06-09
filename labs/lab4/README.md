# Lab 4 Parte 1 — CNN para grietas en hormigón

**Sesión 7** · Clasificación de imágenes con redes convolucionales aplicadas a inspección estructural.

## Tema del laboratorio

Entrenar una **CNN binaria** (PyTorch) sobre el dataset [Concrete Crack Images for Classification](https://data.mendeley.com/datasets/5y9wdsg2zt/1) (METU, CC BY 4.0):

| Clase | Significado |
|-------|-------------|
| **Negative** | Hormigón sin grieta visible |
| **Positive** | Hormigón con grieta |

**Parte 2 (futuro):** RNN/LSTM sobre series de sensores SHM.

## Estado

**✅ Parte 1 completa (CNN).**

| Archivo | Uso |
|---------|-----|
| `cnn_grietas_estructuras_alumno_ia.ipynb` | **Única vía alumno** — guía IA + celda vacía por sección |
| `cnn_grietas_estructuras_solucion.ipynb` | Referencia docente |
| `prompts_entregados.md` | Bitácora obligatoria de prompts |
| `referencia_celdas_ia.md` | **Solo docente** — código canónico por celda (✅) |
| `data/cracks_subset.zip` | Subconjunto versionado (2 000 imágenes) |
| `data/DATOS.md` | Fuente y estructura del dataset |
| `_verificar.py` | Autoevaluación ✅ / ❌ |
| `_preparar_datos.py` | Descomprime zip o regenera desde RAR local |

## Objetivos de aprendizaje

1. Explicar los bloques de una CNN (conv, pool, activación, FC) en contexto de inspección.
2. Cargar imágenes con `ImageFolder` y `DataLoader`.
3. Entrenar y evaluar una CNN pequeña en CPU (Codespaces).
4. Interpretar curvas de entrenamiento, matriz de confusión y casos locales.

## Datos

El repo incluye `data/cracks_subset.zip` (~12 MB). Al ejecutar `labs/setup.sh` se descomprime a `data/cracks_subset/`.

Para regenerar desde el RAR completo (opcional, local):

```bash
cd labs/lab4
python _preparar_datos.py
```

## Entorno local

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/lab4
jupyter notebook cnn_grietas_estructuras_alumno_ia.ipynb
```

Dependencias: `torch` (CPU vía setup.sh), `torchvision`, `Pillow` en [`labs/requirements.txt`](../requirements.txt).

## GitHub Codespaces

1. Abrir el repo → **Code** → **Codespaces** → **Create codespace**.
2. Esperar `labs/setup.sh` (descomprime `cracks_subset`).
3. Abrir `labs/lab4/cnn_grietas_estructuras_alumno_ia.ipynb`.
4. **Run All** (~10–15 min en CPU con 5 épocas).

Guía del curso: [Lab 4 en curso-ia-web](https://ia-estructuras-diplomado.github.io/curso-ia-web/labs/lab4/)

Ver [`../GUIA_LABORATORIOS.md`](../GUIA_LABORATORIOS.md)

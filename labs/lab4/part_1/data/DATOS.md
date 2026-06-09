# Dataset — Grietas en hormigón (Mendeley)

## Fuente

- **Nombre:** Concrete Crack Images for Classification
- **Autor:** Çağlar Fırat Özgenel (METU, 2018)
- **DOI:** [10.17632/5y9wdsg2zt.1](https://doi.org/10.17632/5y9wdsg2zt.1)
- **Licencia:** CC BY 4.0

## Contenido original

| Clase | Significado en obra | Imágenes |
|-------|---------------------|----------|
| **Positive** | Superficie **con** grieta visible | 20 000 |
| **Negative** | Superficie **sin** grieta | 20 000 |

- Resolución: **227 × 227** píxeles, RGB.
- Origen: recortes de fotos de edificios del campus METU (sin data augmentation).

## Subconjunto del laboratorio (`cracks_subset/`)

Para GitHub Codespaces se usa un **subconjunto fijo** (semilla 42):

| Split | Negative | Positive | Total |
|-------|----------|----------|-------|
| `train/` | 800 | 800 | 1 600 |
| `val/` | 200 | 200 | 400 |

**Archivo versionado:** `cracks_subset.zip` (~15–25 MB).

El RAR completo (`Concrete Crack Images for Classification.rar`, ~231 MB) es **opcional** para regenerar el subconjunto en local:

```bash
cd labs/lab4/part_1
python _preparar_datos.py
```

## Estructura de carpetas

```
data/cracks_subset/
├── train/
│   ├── Negative/*.jpg
│   └── Positive/*.jpg
└── val/
    ├── Negative/*.jpg
    └── Positive/*.jpg
```

`torchvision.datasets.ImageFolder` ordena clases alfabéticamente: **0 = Negative**, **1 = Positive**.

## Uso en ingeniería estructural

- Inspección visual asistida por cámara / dron sobre elementos de hormigón.
- Clasificación binaria como **filtro rápido** antes de inspección presencial.
- Limitaciones: iluminación, suciedad, textura del encofrado; el modelo explica patrones en píxeles, no sustituye normativa ni peritaje.

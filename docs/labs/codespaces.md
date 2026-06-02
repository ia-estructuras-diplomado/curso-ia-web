# GitHub Codespaces — Guía rápida

Los laboratorios se ejecutan en **GitHub Codespaces** sobre [`curso-ia-web`](https://github.com/ia-estructuras-diplomado/curso-ia-web). Esta web (GitHub Pages) muestra las guías; los notebooks están en la rama `main` del mismo repo.

## Enlaces por laboratorio

| Lab | Guía | Crear Codespace | Abrir notebook |
|:---:|:-----|:----------------|:---------------|
| **0** | [Sesión 1](../sesiones/sesion1.md) | [▶ Lab 0](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web?quickstart=1&devcontainer_path=.devcontainer%2Fdevcontainer.json) | [📓 `lab0/…_alumno.ipynb`](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab0/fundamentos_python_ia_alumno.ipynb) |
| **1** | [Lab 1](lab1.md) | [▶ Lab 1](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web?quickstart=1&devcontainer_path=.devcontainer%2Fdevcontainer.json) | [📓 `lab1/resistencia_compresion_alumno.ipynb`](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab1/resistencia_compresion_alumno.ipynb) |
| **2** | [Lab 2](lab2.md) | [▶ Lab 2](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web?quickstart=1&devcontainer_path=.devcontainer%2Fdevcontainer.json) | *Próximamente* |
| **3** | [Lab 3](lab3.md) | [▶ Lab 3](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web?quickstart=1&devcontainer_path=.devcontainer%2Fdevcontainer.json) | [📓 `lab3/pca_monitoreo_estructural_alumno.ipynb`](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab3/pca_monitoreo_estructural_alumno.ipynb) |

Cada página de lab ([Lab 1](lab1.md), [Lab 2](lab2.md), [Lab 3](lab3.md)) incluye botones **Crear Codespace** y **Abrir notebook** al inicio.

## Formato de la URL de Codespaces

Plantilla usada en este curso:

```text
https://codespaces.new/ia-estructuras-diplomado/curso-ia-web?quickstart=1&devcontainer_path=.devcontainer%2Fdevcontainer.json
```

| Parámetro | Función |
|-----------|---------|
| `quickstart=1` | Página para **reanudar** tu Codespace reciente o **crear** uno nuevo |
| `devcontainer_path=…` | Usa [`.devcontainer/devcontainer.json`](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/.devcontainer/devcontainer.json) (Python 3.11 + `labs/setup.sh`) |

Al crearse el Codespace, se ejecuta `labs/setup.sh` e instala [`labs/requirements.txt`](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/requirements.txt).

## Pasos para el alumno

1. Clic en **▶ Lab N** (tabla arriba o botón en la guía del lab).
2. Iniciar sesión en GitHub si es necesario.
3. Esperar el build (1–3 min la primera vez).
4. Abrir el notebook `*_alumno.ipynb` (botón **📓** o explorador de archivos en `labs/labN/`).
5. Kernel: **Python 3.11** de `labs/.venv`.

## Alternativa local

```bash
git clone https://github.com/ia-estructuras-diplomado/curso-ia-web.git
cd curso-ia-web
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/labN
jupyter notebook *_alumno.ipynb
```

## Troubleshooting

**Build lento** — Normal la primera vez; luego suele ser más rápido.

**Kernel incorrecto** — Recarga la ventana y selecciona `labs/.venv/bin/python`.

**Falta una librería** — En terminal del Codespace: `source labs/.venv/bin/activate && pip install -r labs/requirements.txt`

**Los enlaces fallan** — Confirma que `labs/` está publicado en `main` de GitHub (sync desde `curso-ia-dev`).

---

[← Laboratorios](index.md) · [FAQ](../faq.md)

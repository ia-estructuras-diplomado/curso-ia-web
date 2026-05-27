# Herramientas y Configuración

## 🖥️ Requisitos de Sistema

- **Procesador:** Cualquiera (Intel/AMD)
- **RAM:** Mínimo 4GB (8GB recomendado)
- **Almacenamiento:** 2GB libres
- **SO:** Windows, macOS, Linux

## 🐍 Python: Instalación

### Opción 1: Google Colab (Recomendado para Principiantes)

✅ **Ventajas:**
- Gratuito
- Sin instalación
- GPU gratis
- Integrado con Google Drive

**Cómo usar:**
1. Ve a https://colab.research.google.com
2. Crea un nuevo notebook
3. ¡Empieza a programar!

### Opción 2: Anaconda (Recomendado para Localmente)

**Instalación:**

1. Descarga desde: https://www.anaconda.com/download
2. Ejecuta el instalador
3. Sigue los pasos (mantén opciones por defecto)

**Crear entorno:**
```bash
conda create -n curso python=3.11
conda activate curso
```

**Instalar librerías:**
```bash
pip install -r requirements.txt
```

### Opción 3: pip (Manual)

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install jupyter pandas numpy scikit-learn matplotlib plotly
```

## 📓 Jupyter Notebook

### Inicio

```bash
jupyter notebook
```

Se abrirá en tu navegador en `http://localhost:8888`

### Atajos Útiles

| Atajo | Función |
|-------|---------|
| `Ctrl+Enter` | Ejecutar celda |
| `Shift+Enter` | Ejecutar y siguiente |
| `Alt+Enter` | Ejecutar y crear nueva |
| `A` | Insertar celda arriba |
| `B` | Insertar celda abajo |
| `DD` | Borrar celda |
| `M` | Cambiar a Markdown |
| `Y` | Cambiar a Código |

### Tips

- Usa `# %%` para dividir en secciones
- Utiliza `?function` para ayuda
- Presiona `Tab` para autocompletar
- Usa `Shift+Tab` para ver parámetros

## 📦 Librerías Principales

### Instalación Individual

```bash
pip install numpy pandas scikit-learn matplotlib plotly tensorflow jupyter
```

### En requirements.txt

```txt
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
matplotlib==3.7.1
plotly==5.15.0
tensorflow==2.13.0
jupyter==1.0.0
```

## 🔧 Editor de Código Recomendado

- **VS Code** (ligero, popular)
  - Extensión: Python, Jupyter
  - Descargar: https://code.visualstudio.com

- **PyCharm** (potente, mejor integración)
  - Community Edition (gratuita)
  - Descargar: https://www.jetbrains.com/pycharm

## 📊 Git y GitHub

### Instalación

**Windows/macOS:**
Descargar desde https://git-scm.com

**Linux (Ubuntu/Debian):**
```bash
sudo apt install git
```

### Configuración

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@ejemplo.com"
```

### Comandos Básicos

```bash
git clone <repo-url>          # Clonar repositorio
git add .                      # Agregar cambios
git commit -m "Mensaje"        # Guardar cambios
git push                       # Subir a GitHub
git pull                       # Descargar cambios
```

## 🌐 IDE Online Alternativas

Si prefieres no instalar nada:

- **Google Colab** - Mejor para Jupyter
- **Replit** - Completo pero menos especializado
- **Kaggle Notebooks** - Datasets integrados
- **GitHub Codespaces** - Entorno en la nube

## ✅ Verificar Instalación

Crea un notebook con:

```python
import numpy as np
import pandas as pd
from sklearn import __version__ as sklearn_version
import matplotlib.pyplot as plt

print(f"NumPy: {np.__version__}")
print(f"Pandas: {pd.__version__}")
print(f"Scikit-learn: {sklearn_version}")
print("✅ ¡Todo instalado correctamente!")
```

Si sale ✅ sin errores, ¡estás listo!

## 🔗 Enlaces Útiles

- [Python.org](https://www.python.org)
- [Jupyter Documentation](https://jupyter.org/documentation)
- [Anaconda Docs](https://docs.anaconda.com)
- [NumPy Tutorial](https://numpy.org/doc/stable/user/index.html)
- [Pandas Documentation](https://pandas.pydata.org/docs)

## 🆘 Troubleshooting

**Problema: "Python no encontrado"**
- Asegúrate que Python está en el PATH
- Usa `python3` en lugar de `python`
- Reinstala Python

**Problema: "No se encuentra librería X"**
```bash
pip install <libreria>
```

**Problema: Jupyter no abre**
```bash
pip install --upgrade jupyter
jupyter notebook --no-browser
```

---

¿Necesitas ayuda? Consulta [FAQ](../faq.md) o contáctanos.

# GitHub Codespaces — Guía rápida

Los laboratorios prácticos se ejecutan en **GitHub Codespaces** sobre el repositorio [`curso-ia-web`](https://github.com/ia-estructuras-diplomado/curso-ia-web). El sitio de documentación (GitHub Pages) solo muestra las guías; los notebooks viven en la rama `main` del mismo repo.

## Crear tu entorno

1. Inicia sesión en [GitHub](https://github.com).
2. Abre **[Crear Codespace del curso](https://codespaces.new/ia-estructuras-diplomado/curso-ia-web)**.
3. Espera a que termine el build del contenedor (1–3 minutos la primera vez).
4. En el explorador de archivos, abre el notebook del lab indicado en la guía (ruta `labs/.../*_alumno.ipynb`).
5. Selecciona el kernel **Python 3.11** de `labs/.venv` (configurado automáticamente).

Al crear el Codespace, el contenedor ejecuta `labs/setup.sh` e instala todas las dependencias de [`labs/requirements.txt`](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/requirements.txt).

## Rutas de notebooks por lab

| Guía web | Notebook en el repo |
|----------|---------------------|
| [Lab 0 — Python (Sesión 1)](../sesiones/sesion1.md) | `labs/lab0/fundamentos_python_ia_alumno.ipynb` |
| [Lab 1 — Fundamentos ML](lab1.md) | `labs/lab1/resistencia_compresion_alumno.ipynb` |
| [Lab 2 — Monitoreo SHM](lab2.md) | *Próximamente* (`labs/lab2/`) |
| [Lab 3 — Clustering y señales](lab3.md) | `labs/lab3/pca_monitoreo_estructural_alumno.ipynb` |

## Ejecutar el notebook

- **Run All** o ejecuta celda por celda en orden.
- Completa solo las celdas marcadas con `### TU TAREA AQUÍ ###`.
- Busca mensajes ✅ / ⚠️ / ❌ al final de cada sección (autoevaluación).

## Alternativa local

Si prefieres no usar Codespaces:

```bash
git clone https://github.com/ia-estructuras-diplomado/curso-ia-web.git
cd curso-ia-web
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/labN
jupyter notebook *_alumno.ipynb
```

## Troubleshooting

**El build del Codespace tarda mucho**  
Es normal la primera vez. Los siguientes arranques suelen ser más rápidos.

**No encuentro el kernel de Python**  
Recarga la ventana (`Ctrl+Shift+P` → *Developer: Reload Window*) y vuelve a abrir el notebook. El intérprete debe ser `labs/.venv/bin/python`.

**Error al importar una librería**  
En la terminal del Codespace:

```bash
source labs/.venv/bin/activate
pip install -r labs/requirements.txt
```

**Puerto 8888 / Jupyter**  
El devcontainer puede reenviar el puerto 8888 si lanzas Jupyter desde terminal. En VS Code/Codespaces suele bastar con abrir el `.ipynb` directamente.

**¿Dónde están las soluciones docente?**  
Los notebooks `*_solucion.ipynb` se sincronizan al repo pero no están enlazados desde esta documentación. En un repositorio público son técnicamente accesibles vía GitHub; úsalos solo como referencia docente.

---

¿Más ayuda? → [FAQ](../faq.md) · [Herramientas](../recursos/herramientas.md)

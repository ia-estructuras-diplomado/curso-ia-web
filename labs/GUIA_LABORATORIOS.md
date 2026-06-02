# Guía de laboratorios — Curso IA (profesionales / ingeniería)

Estándar para todos los labs en `labs/labN/`: **GitHub + Codespaces**, enfoque **caja de herramientas**, validación **visual y amigable** (sin Otter ni autograders pesados).

---

## Prompt de sistema (para agentes de IA)

Copia esto al configurar Cursor, ChatGPT o Claude antes de generar un lab:

```
Actúa como un Ingeniero Estructural Senior y Científico de Datos experto en educación (EdTech). Tu objetivo es crear laboratorios en formato Jupyter Notebook (.ipynb) para un diplomado dirigido a ingenieros civiles profesionales.

Reglas estrictas para los Notebooks:

1. Cero fricción inicial: Todo el código complejo de carga de datos y limpieza debe estar pre-escrito.

2. Enfoque de Caja de Herramientas: Los alumnos NO programarán desde cero. Su tarea se limitará a celdas claramente marcadas con ### TU TAREA AQUÍ ###, donde deberán modificar hiperparámetros (ej. número de árboles, clústeres), seleccionar variables de entrada, o probar nuevos datos.

3. Validación amigable (no calificada): No uses Otter-Grader ni frameworks de testing pesados. Incluye al final de cada ejercicio funciones de validación en Python nativo con if/else y asserts que impriman mensajes con emojis (✅, ⚠️, ❌) según el resultado del experimento del alumno.

4. Visualización técnica: Siempre incluye una celda final que grafique resultados (predicción vs realidad, ROC, clústeres, etc.). Para ingenieros, la validación visual es crucial.

5. Archivos de entorno: dependencias en `labs/requirements.txt` (compartido); entorno virtual en `labs/.venv` vía `labs/setup.sh`. Codespaces usa `.devcontainer/devcontainer.json`.

6. Dos notebooks por lab:
   - `*_alumno.ipynb` — exploración + tareas marcadas + autoevaluación.
   - `*_solucion.ipynb` — referencia docente (no distribuir al inicio).

7. Preguntas teóricas breves en Markdown (reflexión, no examen); respuestas sugeridas solo en la versión solución. En labs introductorios incluir sintaxis, `import`, paquetes, `pip` y `requirements.txt`.
```

---

## Estructura de carpetas por lab

```
labs/labN/
├── README.md                      # Objetivos, Codespaces, orden de ejecución
├── nombre_lab_alumno.ipynb
├── nombre_lab_solucion.ipynb
└── _verificar.py                  # (opcional) helpers de autoevaluación
```

Repositorio (una vez):

```
.devcontainer/devcontainer.json    # Codespaces → ejecuta labs/setup.sh
labs/
├── requirements.txt               # Dependencias de TODOS los labs
├── setup.sh                       # Crea labs/.venv (uv o python -m venv)
├── .venv/                         # Entorno virtual centralizado (gitignored)
└── GUIA_LABORATORIOS.md           # Este archivo
```

Cada lab (`labs/labN/`) **no** lleva su propio venv ni `requirements.txt` duplicado.

---

## Qué NO usar

| Herramienta | Motivo |
|-------------|--------|
| **Otter-Grader** | Fricción, metadata estricta; orientado a pregrado masivo calificado |
| **pytest obligatorio para alumnos** | El profesional valida el modelo/dato, no un `test_1a.py` |
| **Celdas vacías “programa desde cero”** | Rompe el enfoque caja de herramientas |

---

## Plantilla de celda — tarea del alumno

```python
# --- Pre-escrito: no modificar ---
df = pd.read_csv("datos/concrete.csv")

### TU TAREA AQUÍ ###
UMBRAL = 55_000          # Experimenta con otro valor
COLUMNAS_X = ["Edad", "Salario"]  # Prueba quitar o agregar columnas
```

---

## Plantilla de celda — validación amigable

```python
from _verificar import verificar, resumen_seccion

resultados = verificar_pandas(df, filtro, cuantas_compraron, UMBRAL_SALARIO)
resumen_seccion("4 — Pandas", resultados)
```

---

## GitHub Codespaces (alumnos)

1. Crear cuenta en GitHub (si no tiene).
2. Abrir el repositorio del curso → **Code** → **Codespaces** → **Create codespace**.
3. Esperar el build del contenedor (`.devcontainer`).
4. Abrir `labs/labN/*_alumno.ipynb` y seleccionar el kernel de Python del contenedor.
5. **Run All** o ejecutar en orden; buscar ✅ antes de avanzar.

---

## Checklist docente al crear un lab nuevo

- [ ] Datos y limpieza pre-escritos
- [ ] Solo celdas `### TU TAREA AQUÍ ###` editables por el alumno
- [ ] Autoevaluación con emojis al final de cada sección
- [ ] Gráfico técnico final
- [ ] `*_alumno.ipynb` + `*_solucion.ipynb`
- [ ] `labs/requirements.txt` actualizado (entorno centralizado)
- [ ] README del lab con enlace a Codespaces
- [ ] Preguntas teóricas (sintaxis, imports, pip si aplica; sin autograder)

---

## Referencia implementada

**Lab 0:** `labs/lab0/` — Fundamentos de Python para IA.

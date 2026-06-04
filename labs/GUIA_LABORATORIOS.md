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

6. Notebooks por lab (vía manual obligatoria; vía IA opcional):
   - `*_alumno.ipynb` — exploración + tareas `### TU TAREA AQUÍ ###` + autoevaluación.
   - `*_solucion.ipynb` — referencia docente (no distribuir al inicio).
   - `*_alumno_ia.ipynb` — misma lógica con prompts, checklist y celdas `### PEGA AQUÍ EL CÓDIGO DE LA IA ###`.
   - `*_solucion_ia.ipynb` — prompts canónicos + código que pasa ✅ (solo docente).
   - `prompts_entregados.md` — plantilla de bitácora para la vía IA.

7. Preguntas teóricas breves en Markdown (reflexión, no examen); respuestas sugeridas solo en la versión solución. En labs introductorios incluir sintaxis, `import`, paquetes, `pip` y `requirements.txt`.

8. Si generas la vía IA: reutiliza el mismo `_verificar.py`; no compares diff de código con la solución manual — valida artefactos (✅, R², conteos, gráficos).
```

---

## Estructura de carpetas por lab

```
labs/labN/
├── README.md                      # Objetivos, Codespaces, orden de ejecución
├── nombre_lab_alumno.ipynb        # Vía manual (hiperparámetros)
├── nombre_lab_solucion.ipynb
├── nombre_lab_alumno_ia.ipynb     # Vía IA-asistida (opcional)
├── nombre_lab_solucion_ia.ipynb
├── prompts_entregados.md          # Bitácora de prompts (entrega vía IA)
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
4. Abrir el notebook según tu perfil:
   - **Con experiencia mínima en código:** `labs/labN/*_alumno.ipynb`
   - **Sin programar / con asistente IA:** `labs/labN/*_alumno_ia.ipynb` + completar `prompts_entregados.md`
5. Seleccionar el kernel de Python del contenedor.
6. **Run All** o ejecutar en orden; buscar ✅ antes de avanzar.

---

## Vía IA-asistida (opcional)

Paralela a la caja de herramientas manual. El alumno **no escribe código desde cero**: copia prompts a Copilot, Gemini, Cursor, etc. y pega el resultado en celdas marcadas.

### Política académica breve

- La IA **propone**; el ingeniero **valida** con autoevaluación, gráficos y criterio técnico.
- Está permitido iterar con la IA hasta obtener ✅; debe entregar **notebook ejecutable** + **bitácora de prompts**.
- No se califica por “código idéntico a la solución”, sino por **llegar a los mismos artefactos** (métricas, conteos, formas de datos).

### Plantilla de prompt (por sección del notebook)

```text
Contexto: [diplomado ingeniería civil, lab N, sección X]
Dataset: ruta exacta, ej. labs/lab2/data/concrete.csv
Columnas relevantes: [lista exacta del DATOS.md]
Objetivo de ingeniería: [una frase]
Tareas:
1. ...
2. ...
Restricciones:
- Solo genera código para la celda marcada ### PEGA AQUÍ EL CÓDIGO DE LA IA ###
- No reescribas el notebook completo
- Usa las variables ya definidas arriba en la celda (df, corr, X_train, etc.)
Criterio de éxito: la autoevaluación de la sección debe imprimir ✅
```

### Verificación docente (sin diff de código)

| Nivel | Qué revisar |
|-------|-------------|
| Cumplimiento | Salida ✅ de `_verificar.py` por sección |
| Consistencia | Mismas tolerancias que `*_solucion_ia.ipynb` (R², top features, conteos) |
| Uso de IA | Calidad de `prompts_entregados.md` (muestra o rúbrica breve) |

Helpers de generación: [`labs/_ia_helpers.py`](_ia_helpers.py).

---

## Checklist docente al crear un lab nuevo

- [ ] Datos y limpieza pre-escritos
- [ ] Solo celdas `### TU TAREA AQUÍ ###` editables por el alumno
- [ ] Autoevaluación con emojis al final de cada sección
- [ ] Gráfico técnico final
- [ ] `*_alumno.ipynb` + `*_solucion.ipynb`
- [ ] (Opcional) `*_alumno_ia.ipynb` + `*_solucion_ia.ipynb` + `prompts_entregados.md`
- [ ] Prompts canónicos probados en ≥ 2 asistentes (Copilot + otro)
- [ ] `labs/requirements.txt` actualizado (entorno centralizado)
- [ ] README del lab con enlace a Codespaces y qué notebook abrir (manual vs IA)
- [ ] Preguntas teóricas (sintaxis, imports, pip si aplica; sin autograder)

---

## Referencia implementada

**Lab 0:** `labs/lab0/` — Fundamentos de Python para IA (vía manual + IA).

**Lab 1:** `labs/lab1/` — PCA y monitoreo estructural (vía manual + IA).

**Lab 2:** `labs/lab2/` — Resistencia a compresión (vía manual + IA; piloto IA).

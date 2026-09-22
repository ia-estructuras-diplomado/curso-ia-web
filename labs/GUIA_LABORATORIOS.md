# Guía de laboratorios — Curso IA (profesionales / ingeniería)

Estándar para todos los labs en `labs/labN/`: **GitHub + entorno local (`labs/.venv`)**, **un
notebook de referencia por lab** (completo, narrado, ejecutable de punta a
punta), validación **visual** (gráficos, métricas) — sin Otter, sin
autograders, sin celdas de autoevaluación con ✅/❌.

---

## Prompt de sistema (para agentes de IA)

Copia esto al configurar Cursor, ChatGPT o Claude antes de generar o editar un lab:

```
Actúa como un Ingeniero Estructural Senior y Científico de Datos experto en educación (EdTech). Tu objetivo es crear/editar laboratorios en formato Jupyter Notebook (.ipynb) para un diplomado dirigido a ingenieros civiles profesionales.

Reglas estrictas para los Notebooks:

1. Cero fricción inicial: todo el código de carga de datos y limpieza debe estar pre-escrito y funcionando.

2. Un solo notebook por lab, narrado de forma directa: no hay una versión "en blanco" para que el alumno complete ni celdas "### TU TAREA AQUÍ ###". El notebook es la referencia completa — objetivo y esquema de secciones al inicio, luego cada sección explica en markdown qué se hace y por qué, seguida directamente del código real y su resultado (gráfico/métrica). Nada de framing "Pregunta / Respuesta sugerida".

3. Sin autoevaluación automática: no importes ni escribas funciones `_verificar.py`/✅-❌. La validación es visual — el alumno compara su propio notebook (que construye guiándose por el README del lab y su asistente de IA) contra los gráficos/métricas de este notebook de referencia.

4. Visualización técnica: cada sección analítica termina en una celda que grafica o reporta el resultado (predicción vs realidad, ROC, clústeres, mapa de calor Grad-CAM, etc.). Para ingenieros, la validación visual es crucial.

5. Cierre obligatorio: última sección del notebook titulada "## Reflexión: preguntas que los alumnos necesitarían" — de 3 a 5 preguntas abiertas de pensamiento crítico, específicas del contenido de ingeniería del lab (no genéricas), que un alumno estudiando solo con este notebook necesitaría hacerse.

6. El README.md del lab (no el notebook) es quien lleva la guía por sección para el alumno: objetivo, qué debería producir su celda (en prosa, sin pegar el código de la solución) y el prompt de IA sugerido en un blockquote. El notebook nunca contiene ese andamiaje de pregunta/prompt — solo el resultado narrado.

7. Cero archivos .py dentro de `labs/labN/`: nada de generadores de notebook, nada de módulos de verificación, nada de scripts de smoke test junto al contenido del lab. Un script de preparación de datos/modelo de un solo uso (no visto por el alumno) va en `tools/`, en la raíz del repo, fuera de `labs/`.

8. Archivos de entorno: dependencias en `labs/requirements.txt` (compartido); entorno virtual en `labs/.venv` vía `labs/setup.sh` (Linux/macOS) o `labs\setup.ps1` (Windows), con Python fijado por `uv`.

9. En labs introductorios incluir sintaxis, `import`, paquetes, `pip` y `requirements.txt` como contenido narrado, no como preguntas de examen.
```

---

## Estructura de carpetas por lab

```
labs/labN/                          # y labs/lab4/part_1/, labs/lab4/part_2/
├── README.md                       # Objetivo + guía de secciones/prompts para que el alumno construya su propio notebook
├── nombre_lab.ipynb                # EL notebook — completo, narrado, ejecutable de punta a punta
├── prompts_entregados.md           # Bitácora de prompts (entrega del alumno)
└── data/                           # (si aplica) DATOS.md + solo los archivos que el notebook lee en tiempo de ejecución
```

Repositorio (una vez):

```
labs/
├── requirements.txt                # Dependencias de TODOS los labs
├── setup.sh                        # Crea labs/.venv (uv, Python fijado)
├── _install_torch_cpu.sh           # Stack PyTorch CPU compartido (Lab 4); también repara el venv
├── _verificar_notebooks.sh         # Docente: ejecuta los 6 notebooks de punta a punta (nbconvert)
├── .venv/                          # Entorno virtual centralizado (gitignored)
└── GUIA_LABORATORIOS.md            # Este archivo
tools/                               # Scripts de autoría de un solo uso (datos/modelos), fuera de labs/
```

Cada lab (`labs/labN/`) **no** lleva su propio venv, `requirements.txt`, ni ningún archivo `.py`.

### Excepción: labs de agentes (Lab 5 y Lab 6)

En los labs de agentes el alumno no construye código: dirige y audita un
agente real (Claude Code) conectado por MCP a programas externos. No hay
notebook; el README es una guía paso a paso por **Partes** (objetivo, qué
debería ver en pantalla, prompt sugerido) y la referencia son archivos de
configuración de agentes, no un notebook.

```
labs/lab5/ (y lab6/)
├── README.md                       # Guía por Partes: instalación, prompts, qué observar, reflexión, entrega
├── .mcp.json                       # Servidores MCP del proyecto (se lanzan con uvx; versiones fijadas)
├── referencia/                     # Subagentes (.md) y skills de referencia para comparar
├── prompts_entregados.md           # Bitácora: prompt, herramientas observadas, verificación manual
└── rag/config.yaml, pdfs/          # (Lab 5) configuración del RAG y corpus
```

Reglas: servidores MCP de terceros solo tras revisar licencia, actividad y
qué hacen al cerrar/desconectar; versiones y hashes fijados; el alumno
trabaja sobre copias de sus modelos y lee el código que aprueba.

---

## Qué NO usar

| Herramienta / patrón | Motivo |
|-------------|--------|
| **Otter-Grader** | Fricción, metadata estricta; orientado a pregrado masivo calificado |
| **pytest / `_verificar.py` para alumnos** | El profesional valida el modelo/dato visualmente, no una suite de tests |
| **Celdas vacías “programa desde cero”** | Este no es un curso de programación — el foco es criterio de ingeniería sobre resultados de IA |
| **Notebooks separados alumno/solución/vía-manual/vía-IA** | El notebook de referencia único **es** la entrega y la guía; mantener 2-4 variantes por lab dejó de ser sostenible |

---

## Plantilla de sección — notebook de referencia

```markdown
## 3. Partición y entrenamiento

Separamos el 80/20 con estratificación por clase porque el desbalance
(pocos casos de daño severo) sesgaría una partición aleatoria simple...
```
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42,
)
modelo = XGBClassifier(n_estimators=200, max_depth=6, learning_rate=0.1)
modelo.fit(X_train, y_train)
```

Nada de "### TU TAREA AQUÍ ###", nada de "# --- Autoevaluación ---" — el
código real, precedido de la explicación de por qué se hace así.

---

## Plantilla de sección — README del lab (guía para el alumno)

```markdown
### Sección 3 — Partición y entrenamiento

**Objetivo:** dividir los datos preservando la proporción de clases y
entrenar un primer clasificador base.

**Qué debería producir tu celda:** un `X_train`/`X_test` con la misma
proporción de clases que el dataset completo, y un modelo entrenado con
`.predict()` funcional.

**Prompt sugerido para tu asistente IA:**
> Tengo un DataFrame `df` con la columna objetivo `Condition Label`
> (0/1/2, desbalanceada). Genera código que separe 80/20 con
> estratificación por clase y entrene un XGBClassifier con
> n_estimators=200, max_depth=6, learning_rate=0.1.
```

---

## Entorno local (alumnos)

1. Clonar el repositorio del curso: `git clone https://github.com/ia-estructuras-diplomado/curso-ia-web.git`.
2. Windows: `powershell -ExecutionPolicy Bypass -File labs\setup.ps1` (ver [`INSTALACION_WINDOWS.md`](INSTALACION_WINDOWS.md)). Linux/macOS: `bash labs/setup.sh`.
3. Labs 5 y 6: instalar Claude Code (Parte 0 del [Lab 5](lab5/README.md)). El Lab 6 requiere **Windows nativo con ETABS 21+**.
4. Abrir `labs/labN/<nombre_lab>.ipynb`, ejecutar **Run All** para ver el resultado esperado.
5. Construir tu propio notebook en una celda/archivo nuevo, guiándote por el README del lab (objetivo + prompts por sección) y copiando prompts a tu asistente de IA (Copilot, Gemini, Cursor…).
6. Entregar: tu notebook ejecutado de punta a punta + `prompts_entregados.md` completado.

---

## Bitácora de prompts

`prompts_entregados.md` es la entrega obligatoria de cada lab — un registro
por sección con tres campos: **Prompt enviado** (texto exacto), **Respuesta
de la IA (resumen)**, **¿Qué aceptaste/rechazaste y por qué?**. Esto
reemplaza la calificación por diff de código: lo que se evalúa es que el
alumno llegó a los mismos artefactos (métricas, gráficos, formas de datos)
que el notebook de referencia, ejerciendo criterio sobre lo que la IA
propuso — "la IA propone, el ingeniero valida visualmente".

---

## Checklist docente al crear o editar un lab

- [ ] Datos y limpieza pre-escritos y funcionando
- [ ] Un solo notebook, narrado directamente, sin framing de pregunta/autoevaluación
- [ ] Gráfico o métrica técnica al final de cada sección analítica
- [ ] Sección de cierre "Reflexión: preguntas que los alumnos necesitarían" (3-5 preguntas específicas del lab)
- [ ] README del lab con objetivo + guía por sección (prosa, no código) + prompt de IA sugerido
- [ ] `prompts_entregados.md` presente y con el nombre del notebook actualizado
- [ ] Cero archivos `.py` dentro de `labs/labN/` (scripts de datos/modelo de un solo uso van en `tools/`)
- [ ] `labs/requirements.txt` actualizado si el lab agrega una dependencia (entorno centralizado)
- [ ] `bash labs/_verificar_notebooks.sh` corre el notebook de punta a punta sin errores
- [ ] (Labs de agentes) servidores MCP probados en una PC real antes de clase; versiones fijadas en `.mcp.json`

---

## Referencia implementada

Los 6 labs con notebook (`lab0`–`lab3`, `lab4/part_1`, `lab4/part_2`) siguen este patrón único desde la reestructuración que eliminó los generadores de notebook y las variantes alumno/solución/manual/IA. `lab5` y `lab6` siguen el patrón de labs de agentes (Claude Code + MCP).

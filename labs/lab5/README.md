# Lab 5 — Tu primer agente: Claude Code + MCP de normas (RAG)

**Sesión 9** · Usarás un agente de IA real (**Claude Code**) conectado por
**MCP** a un buscador RAG local sobre las normas peruanas E.020, E.030 y E.050.
No vas a programar el RAG: vas a **ver funcionar a un agente**, entender qué
hace en cada paso y terminar definiendo **tu propio agente especializado**.

## Objetivo de aprendizaje

1. Entender qué es un **agente**: un modelo de lenguaje que, en un bucle,
   decide qué **herramienta** usar, la ejecuta, lee el resultado y vuelve a
   decidir — hasta terminar la tarea.
2. Entender qué es **MCP** (*Model Context Protocol*): el "enchufe estándar"
   que conecta un agente con programas externos (un buscador de normas hoy;
   ETABS y Excel en el Lab 6).
3. Usar **RAG como herramienta**: que el agente busque en la norma y cite
   archivo y página, en lugar de responder de memoria.
4. Crear un **subagente** (`consultor-normativo`) reutilizable — la pieza que
   el orquestador del Lab 6 va a delegar.

## Contexto de ingeniería

Una cifra de sobrecarga o un coeficiente sísmico mal citado tiene
consecuencias reales. Un LLM "de memoria" puede sonar convincente y estar
equivocado; un agente con RAG está obligado a mostrar **de dónde** sacó cada
valor, y eso permite que tú — el ingeniero — lo verifiques.

```
 Tú ──► Claude Code (agente) ──► MCP "normas" (knowledge-rag) ──► índice local de pdfs/
          ▲    │  decide qué buscar, lee los resultados,
          └────┘  vuelve a buscar si hace falta y responde con cita
```

## Qué hay en esta carpeta

| Archivo | Para qué |
|---|---|
| `pdfs/` | Normas E.020, E.030 y E.050 (ver [`data/DATOS.md`](data/DATOS.md)) |
| `.mcp.json` | Registra el servidor MCP `normas` para Claude Code (se carga solo al abrir Claude en esta carpeta) |
| `rag/config.yaml` | Configuración del RAG: embeddings multilingües, tamaño de fragmentos, carpeta de PDFs |
| `referencia/consultor-normativo.md` | Subagente de referencia (para comparar con el tuyo en la Parte 6) |
| `prompts_entregados.md` | Tu bitácora (entrega) |

No hay notebook: el "código" de este lab ya existe — es el agente. Tu trabajo
es **dirigirlo, observarlo y auditarlo**.

---

## Parte 0 — Instalación (una sola vez)

Necesitas el entorno del curso ya instalado (`labs\setup.ps1`, ver
[`../INSTALACION_WINDOWS.md`](../INSTALACION_WINDOWS.md)) — de ahí viene `uv`,
que usa el servidor MCP.

### 0.1 Instalar Claude Code (PowerShell)

```powershell
irm https://claude.ai/install.ps1 | iex
claude --version
```

Si `claude` no se reconoce, cierra y vuelve a abrir PowerShell.

En macOS/Linux: `curl -fsSL https://claude.ai/install.sh | bash`. (El Lab 6
necesita Windows con ETABS; si vas a hacerlo, instala Claude Code en
Windows nativo, no en WSL.)

### 0.2 Elegir cómo accedes al modelo

| Opción | Cómo | Cuándo |
|---|---|---|
| **A. Suscripción Claude (Pro/Max)** | Ejecuta `claude` y elige iniciar sesión con tu cuenta de Claude | Recomendado: mejor calidad, sobre todo para ETABS en el Lab 6 |
| **B. API key del curso** | Ejecuta `claude` y elige iniciar sesión con cuenta de Anthropic Console (o define `ANTHROPIC_API_KEY`) | Si el docente te entregó una clave/créditos |
| **C. Gratis con Ollama** | Instala [Ollama para Windows](https://ollama.com/download/windows), luego `ollama signin` y `ollama launch claude` (elige un modelo del menú) | Sin costo. Los modelos abiertos usan herramientas con menos precisión: sirve para este lab, pero espera respuestas más irregulares |

> Con la opción C, **siempre** abre Claude Code con `ollama launch claude`
> (desde la carpeta del lab) en lugar de `claude`. Los modelos locales
> pequeños (p. ej. `llama3.2:3b`) **no** alcanzan: Claude Code necesita
> modelos con ventana de contexto de 64k o más y buen *tool calling*.

### 0.3 Abrir Claude Code en la carpeta del lab

```powershell
cd $HOME\curso-ia-web\labs\lab5
claude
```

Al abrir por primera vez, Claude Code te pedirá:
1. **Confiar en la carpeta** → sí.
2. **Aprobar el servidor MCP `normas`** definido en `.mcp.json` → sí.

La primera vez el servidor descarga el modelo de embeddings (~240 MB) e
indexa los PDFs: tarda 1-2 minutos. Escribe `/mcp` para ver su estado:
debe decir **connected** con 13 herramientas.

> **Importante:** abre `claude` siempre desde `labs\lab5`. El servidor busca
> su configuración en `.\rag` relativo a donde lo abras.

---

## Parte 1 — El bucle del agente, en vivo

**Objetivo:** ver que un agente no "responde": **actúa** en pasos.

**Qué deberías ver:** varias líneas con ⏺ antes de la respuesta final — cada
una es una **llamada a herramienta** (listar archivos, leer, ejecutar un
comando) que el modelo decidió hacer. Claude Code te pedirá **permiso** antes
de cada acción que no sea de solo lectura: ese es el *humano en el bucle*.

**Prompt sugerido:**
> Sin usar el servidor normas todavía: lista los PDFs de la carpeta pdfs/,
> dime cuántas páginas tiene cada uno y si tienen texto seleccionable o son
> escaneados. Explícame qué herramientas usaste y por qué en ese orden.

Anota en la bitácora: ¿cuántas herramientas llamó?, ¿alguna te pidió permiso?,
¿qué PDF resultó ser escaneado? (pista: guárdalo para la Parte 4).

> 💡 `Ctrl+O` muestra el detalle completo de cada llamada (entrada y salida).

---

## Parte 2 — Conectar el MCP y ver sus herramientas

**Objetivo:** entender que un servidor MCP es un programa aparte que
**ofrece herramientas** con nombre, descripción y parámetros; el agente las
descubre y decide cuándo usarlas.

**Qué deberías ver:** en `/mcp` → `normas` → la lista de herramientas
(`search_knowledge`, `get_document`, `list_documents`, …). Pregunta al agente
qué documentos hay indexados.

**Prompt sugerido:**
> Usa el servidor MCP normas: ¿qué documentos tiene indexados y cuántos
> fragmentos (chunks) hay en total? Luego explícame con tus palabras, para un
> ingeniero civil, qué hace la herramienta search_knowledge.

---

## Parte 3 — Consulta normativa con cita verificable

**Objetivo:** usar RAG como herramienta y **auditar la cita**.

**Qué deberías ver:** una o varias llamadas a `search_knowledge` (a veces el
agente reformula y vuelve a buscar — eso es el bucle), y una respuesta con
**[archivo, página]**. Después **abre el PDF en esa página y verifica a mano**
que el valor está ahí.

**Prompts sugeridos (haz al menos dos):**
> Según la E.020, ¿cuál es la carga viva repartida mínima para viviendas y para
> oficinas? Usa solo el servidor normas y cita archivo y página de cada valor.

> Según la E.050, ¿en qué casos es obligatorio un Estudio de Mecánica de
> Suelos? Cita la fuente.

Anota: ¿la página citada era la correcta?, ¿el valor coincidía?, ¿cuántas
búsquedas hizo el agente antes de responder?

---

## Parte 4 — Cuando el RAG falla: la E.030

**Objetivo:** ver un modo de falla real y cómo un agente puede (o no) sortearlo.

El PDF de la E.030 incluido en el curso es **escaneado** (imágenes, sin texto):
el indexador lo omite, así que el RAG **no puede** encontrar nada de la norma
sísmica. Pregunta algo de la E.030 y observa qué pasa.

**Prompt sugerido:**
> Usando solo el servidor normas: ¿cuál es el factor de zona Z para la zona 4
> según la E.030?

**Qué deberías ver:** resultados de otras normas (o ninguno). Un buen agente
debería decir que no lo encontró; uno malo, inventar. Luego:

> ¿Por qué no encontraste la E.030? Revisa el PDF. Si es escaneado, lee
> directamente las páginas donde esté la tabla de factores de zona y
> responde citando la página.

Claude Code puede **leer visualmente** las páginas del PDF (sin RAG). Compara
en la bitácora: RAG (índice de fragmentos, rápido, barato, falla con
escaneados) vs. lectura directa (más costosa, limitada en páginas, pero "ve"
la tabla). Verifica el valor a mano.

> **Si usas la opción C (Ollama):** la lectura visual depende del modelo, y
> los modelos abiertos de `ollama launch claude` en general **no** pueden
> leer páginas escaneadas desde Claude Code. Haz igual la primera pregunta
> (RAG) para observar la falla; para la lectura directa, sube
> `pdfs/Norma_E_030_SISMO.pdf` a **Claude Desktop** o
> [claude.ai](https://claude.ai) (el plan gratuito basta) y pide ahí la
> tabla de factores de zona con su página. Anota en la bitácora que esa
> parte la hiciste fuera del agente.

> Si el docente reemplazó el PDF por una versión con texto, esta parte se
> convierte en: comparar la respuesta vía RAG con la respuesta leyendo la
> página directamente.

---

## Parte 5 — Con RAG vs. sin RAG

**Objetivo:** ver la diferencia entre "memoria del modelo" y "documento".

**Prompt sugerido:**
> Responde de memoria, SIN usar ninguna herramienta: ¿qué tipos de sobrecarga
> considera la E.020 y cuál es la carga viva para azoteas? Después responde lo
> mismo usando el servidor normas con citas. Haz una tabla comparando ambas
> respuestas y marca qué afirmaciones de memoria NO aparecen en la norma.

---

## Parte 6 — Tu primer agente especializado (subagente)

**Objetivo:** convertir lo que hiciste a mano en un agente reutilizable con
**rol, herramientas limitadas e instrucciones** — exactamente lo que el
orquestador del Lab 6 va a delegar.

Un subagente de Claude Code es un archivo Markdown en `.claude/agents/` con:
- `name` y `description` (el orquestador decide delegar leyendo la descripción),
- `tools` (solo las herramientas que necesita — mínimo privilegio),
- un *system prompt* con el procedimiento y el formato de respuesta.

**Prompt sugerido:**
> Crea un subagente de Claude Code en .claude/agents/consultor-normativo.md.
> Rol: consultor de normas peruanas E.020/E.030/E.050. Herramientas permitidas:
> solo las de búsqueda/lectura del servidor MCP normas (mcp__normas__...),
> Read y Glob — nada que modifique archivos. Debe responder siempre con:
> Respuesta, Cita textual, Fuente [archivo, página] y Confianza, y decir
> explícitamente cuando no encuentre algo. Muéstrame el archivo antes de
> guardarlo.

Luego **sal y vuelve a abrir** `claude` (los subagentes se cargan al inicio)
y pruébalo:

> Usa el subagente consultor-normativo: ¿cuál es el peso propio de un
> aligerado de 0,20 m según la E.020?

**Qué deberías ver:** la llamada al subagente, sus búsquedas dentro de él y
una respuesta con el formato que definiste. Compara tu archivo con
[`referencia/consultor-normativo.md`](referencia/consultor-normativo.md):
¿qué reglas tiene la referencia que al tuyo le faltan (o al revés)?

---

## Reflexión: preguntas que necesitarías hacerte

1. El agente citó una página correcta pero el valor estaba en otra fila de la
   tabla. ¿Qué parte del sistema falló — la búsqueda, el fragmento o el
   modelo — y cómo lo detectarías sin leer toda la norma?
2. ¿Qué herramientas le quitarías a un agente que consulta normas en una
   oficina de diseño, y por qué? (Piensa en "mínimo privilegio".)
3. La E.030 escaneada rompió el RAG en silencio. ¿Qué verificación harías
   **antes** de confiar en un índice sobre documentos de tu empresa?
4. ¿En qué casos preferirías que el agente lea el PDF completo en lugar de
   buscar fragmentos? ¿Qué costo tiene?
5. ¿Quién firma el cálculo si el valor normativo lo buscó un agente?

## Límites importantes

- El agente puede **alucinar** incluso citando una página real: verifica
  siempre el valor en el PDF.
- Los PDFs del curso pueden no ser la versión vigente: la norma oficial
  prevalece.
- Con la opción C (Ollama), la calidad depende mucho del modelo elegido.

## Entrega

- `prompts_entregados.md` completado (Partes 1-6), incluyendo **qué citas
  verificaste a mano** y si eran correctas.
- Tu `.claude/agents/consultor-normativo.md`.
- Una captura de pantalla de `/mcp` mostrando `normas` conectado.

## Para el docente

- Servidor MCP: [`knowledge-rag`](https://github.com/lyonzin/knowledge-rag)
  (MIT, CI en Windows/Linux/macOS), fijado a `4.9.0` en `.mcp.json` y lanzado
  con `uvx` (no se instala en `labs/.venv`). Probado con los PDFs del curso:
  indexa E.020 + E.050 (173 fragmentos) y omite la E.030 escaneada.
- El índice y el modelo quedan en `rag/data/` y `rag/models_cache/`
  (gitignored). Para reindexar desde cero, borra `rag/data/`.
- Para que la E.030 funcione con RAG, reemplaza `pdfs/Norma_E_030_SISMO.pdf`
  por una versión con capa de texto (o pásale OCR) y ajusta la Parte 4.

Ver [`../GUIA_LABORATORIOS.md`](../GUIA_LABORATORIOS.md).

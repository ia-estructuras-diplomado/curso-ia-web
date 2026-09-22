# Lab 6 — Agentes con ETABS: de un agente a un orquestador

**Sesión 10** · Conectarás Claude Code a **ETABS** (y a **Excel**) mediante
MCP, verás al agente consultar y analizar tu modelo **en tiempo real**, y
terminarás armando un **orquestador** que coordina tres agentes
especializados para hacer un chequeo sísmico E.030 completo.

## Objetivo de aprendizaje

1. Conectar un agente a un programa de ingeniería real (ETABS) vía MCP y
   entender qué puede y qué **no** debe hacer sobre tu modelo.
2. Encadenar programas: ETABS → agente → Excel, sin escribir código tú.
3. Dar **conocimiento de dominio** al agente con una *skill* (procedimiento
   E.030 de derivas).
4. Pasar de **un agente** a un **orquestador + subagentes**: dividir el
   trabajo, limitar herramientas por rol y cruzar resultados.

## Contexto de ingeniería

Extraer periodos, masas participativas, cortantes y derivas de ETABS, pasar
todo a Excel y compararlo con la E.030 es trabajo repetitivo y propenso a
errores de transcripción. Un agente puede hacerlo en minutos — pero **tú**
sigues siendo responsable del modelo, de los supuestos (R, regularidad) y
del veredicto. Este lab muestra ambas cosas: la velocidad y los puntos donde
el ingeniero tiene que intervenir.

```
                    ┌─► analista-etabs ─────► MCP etabs ──► ETABS (modelo abierto)
 Tú ─► orquestador ─┼─► consultor-normativo ► MCP normas ─► PDFs E.020/E.030/E.050
                    └─► redactor-informe ───► MCP excel ──► resultados/chequeo_e030.xlsx
```

## Qué hay en esta carpeta

| Archivo | Para qué |
|---|---|
| `.mcp.json` | Registra los servidores `normas` (el del Lab 5) y `excel` |
| `referencia/agents/` | Subagentes de referencia: `analista-etabs`, `consultor-normativo`, `redactor-informe`, `orquestador-sismico` |
| `referencia/skills/e030-derivas/` | Skill de referencia con el procedimiento E.030 |
| `prompts_entregados.md` | Tu bitácora (entrega) |

El servidor de ETABS **no** va en `.mcp.json` porque la ruta del ejecutable
cambia en cada PC: lo registras tú en la Parte 0.

---

## Parte 0 — Requisitos e instalación del MCP de ETABS

**Requisitos:** **Windows nativo** (no WSL2, no macOS), **ETABS 21 o
superior** con licencia en la misma PC, Claude Code instalado desde
PowerShell y funcionando (Lab 5), y el Lab 5 abierto al menos una vez (para
que el índice de normas exista). Si no tienes ETABS, trabaja en pareja con
alguien que sí lo tenga.

### 0.1 Descargar el servidor

Usamos [`Shekh-Muhsen/ETABS-MCP`](https://github.com/Shekh-Muhsen/ETABS-MCP)
(MIT): se **conecta** a un ETABS ya abierto (no lo cierra al salir), ejecuta
el código en un *sandbox* sin acceso a archivos, e incluye documentación de
la API de ETABS y flujos de trabajo (modal, derivas, cortante basal) que el
agente consulta antes de actuar.

```powershell
cd $HOME\curso-ia-web\labs\lab6
$dest = "$HOME\etabs-mcp"
New-Item -ItemType Directory -Force $dest | Out-Null
Invoke-WebRequest -Uri "https://github.com/Shekh-Muhsen/ETABS-MCP/releases/download/v2.0.0/etabs-mcp.mcpb" -OutFile "$dest\etabs-mcp.zip"
(Get-FileHash "$dest\etabs-mcp.zip" -Algorithm SHA256).Hash
Expand-Archive "$dest\etabs-mcp.zip" -DestinationPath $dest -Force
```

El hash debe ser exactamente:
`F1E0ECC7C294F69D7585129001AFAA18D85ECF6933BEA8360FAF73E4E93B9FDB`.
Si no coincide, **no lo ejecutes** y avisa al docente.

### 0.2 Registrarlo en Claude Code (solo para este proyecto)

```powershell
claude mcp add etabs -- "$HOME\etabs-mcp\etabs-mcp.exe"
New-Item -ItemType Directory -Force resultados | Out-Null
```

La carpeta `resultados\` es donde el agente guarda el `.edb` de práctica,
los JSON y el Excel (ETABS exige guardar el modelo antes de analizarlo).

### 0.3 Probar la conexión

1. Abre **ETABS** (normal, *no* "como administrador") con un modelo.
   **Trabaja sobre una copia** del `.edb`: el agente puede modificar el modelo.
2. En `labs\lab6`, abre `claude` (o `ollama launch claude`), aprueba los
   servidores de `.mcp.json` y escribe `/mcp`: deben aparecer `etabs`,
   `normas` y `excel` conectados.

> Si `etabs` no conecta: verifica que ETABS esté abierto con un modelo, que
> ambos programas corran con el mismo usuario y nivel de permisos, y que la
> versión sea 21+.

---

## Parte 1 — Primer contacto, en tiempo real

**Objetivo:** ver cómo el agente descubre la API de ETABS y consulta tu modelo.

**Prompt sugerido:**
> Usa el servidor etabs: verifica la conexión (get_status) y descríbeme el
> modelo abierto — unidades, número de pisos y alturas, materiales, secciones
> de vigas y columnas, casos de carga y si ya tiene resultados. No modifiques
> nada.

**Qué deberías ver:** `get_status`, `discover_api`/`read_skills` (el agente
"lee el manual" antes de actuar) y varias llamadas a `execute_code`. **Antes
de aprobar cada `execute_code`, lee el código Python** que va a correr sobre
tu modelo — ese es tu control como ingeniero. Anota una llamada que
entendiste y una que no.

## Parte 2 — Modelo de práctica (si no tienes uno)

Si no tienes un modelo, pídele al agente que lo construya **mientras miras
ETABS**:

> Con el servidor etabs, crea un modelo nuevo con
> SapModel.InitializeNewModel(6) y luego SapModel.File.NewGridOnly(3, 3, 3,
> 3, 3, 5, 5) (no uses File.NewBlank). Crea un pórtico de concreto armado de
> 3 pisos (altura 3 m), 2 vanos de 5 m en X y 2 de 5 m en Y, con material
> C21 (concreto, f'c = 21 MPa), columnas 40x40 cm (COL40X40) y vigas
> 30x50 cm (VIGA30X50), asignadas explícitamente a cada frame, y
> empotramiento en la base. En cada piso crea una losa maciza de 0.15 m de
> espesor: una sección de losa LOSA15 con PropArea.SetSlab (SlabType=0
> Slab, ShellType=1 **ShellThin**, material C21), dibujada con
> AreaObj.AddByCoord como un área por paño (4 paños por piso) con PropName
> = LOSA15. Define un diafragma rígido por piso (D1, D2, D3 con
> Diaphragm.SetDiaphragm, SemiRigid=False) y asígnalo a las losas de ese
> piso con AreaObj.SetDiaphragm. Hazlo por pasos, refresca la vista después
> de cada paso y dime qué método de la API usaste en cada uno. Al final
> guárdalo en resultados\practica.edb (ruta absoluta).

> ⚠️ Probado en ETABS 21.2: si ETABS está abierto **sin ningún modelo** y el
> agente llama `File.NewBlank()`, ETABS se cierra sin aviso. Por eso el
> prompt fija la secuencia `InitializeNewModel` → `NewGridOnly`. Otra opción
> segura: crea tú el modelo en blanco desde la interfaz (File → New Model →
> Grid Only) antes de pedirle al agente que construya.

**Qué deberías ver:** la estructura apareciendo en la ventana de ETABS.
Revisa en ETABS (no en el chat) que las secciones y apoyos sean los pedidos.

> ⚠️ **Error real visto en la prueba del curso:** el agente creó las
> secciones de concreto `COL40X40`/`VIGA30X50`, pero dibujó los 16 elementos
> con la sección por defecto de ETABS (acero **W14X500**) y aun así reportó
> "todo OK". Antes del análisis, pídele:
>
> > Solo lectura: para cada frame dime su sección (FrameObj.GetSection) y el
> > material y f'c de esa sección.
>
> y compáralo en ETABS (Assign → Frame → Section Property, o el color de los
> elementos). Si hay acero, pídele reasignar con `FrameObj.SetSection`.
>
> Lo mismo con las losas: pídele leer la tabla **Slab Property
> Definitions** (DatabaseTables) y verifica que `LOSA15` diga
> `ModelType = Shell-Thin`, y que cada área tenga `LOSA15`
> (AreaObj.GetProperty) y el diafragma de su piso (AreaObj.GetDiaphragm).
> En la prueba, la documentación del servidor indicaba `ShellType=0` para
> ShellThin; en ETABS 21 eso deja el tipo **vacío** sin error. El valor
> correcto es `1`.

## Parte 3 — Análisis modal y cortante basal

**Prompt sugerido:**
> Con el servidor etabs: si el modelo no tiene un caso modal y uno espectral
> E.030 en X e Y, dime qué falta y pídeme los parámetros (Z, U, S, R) antes de
> crearlos. Luego corre el análisis y repórtame: periodos de los 3 primeros
> modos por dirección, % de masa participativa acumulada y cortante basal por
> caso.

**Qué deberías ver:** el agente pidiéndote datos que solo tú puedes decidir,
el análisis corriendo en ETABS y una tabla de resultados. Verifica al menos
un periodo y un cortante en las tablas de ETABS.

## Parte 4 — Darle conocimiento E.030 al agente (skill)

**Objetivo:** que el agente siga **tu** procedimiento (0.75R/0.85R, límites
de la Tabla N° 11) en lugar de uno genérico de ASCE 7.

Una *skill* es una carpeta `.claude/skills/<nombre>/SKILL.md` con un
procedimiento que el agente carga cuando lo necesita.

**Prompt sugerido:**
> Crea una skill de Claude Code en .claude/skills/e030-derivas/SKILL.md con el
> procedimiento para verificar derivas según la E.030: deriva inelástica =
> 0.75R (regular) u 0.85R (irregular) por la deriva elástica de ETABS, y los
> límites por material de la Tabla N° 11. Incluye cómo extraer las derivas con
> el servidor etabs. Antes de guardarla, confirma los valores con el servidor
> normas y cita la página (si la E.030 no está indexada, léela directamente).

Compara con [`referencia/skills/e030-derivas/SKILL.md`](referencia/skills/e030-derivas/SKILL.md).
Reinicia `claude` y luego:

> Verifica las derivas de este modelo según la E.030 usando la skill
> e030-derivas. Pregúntame R y si la estructura es regular.

## Parte 5 — Otro programa: Excel

**Prompt sugerido:**
> Con el servidor excel crea resultados\derivas.xlsx (ruta absoluta) con la
> tabla de derivas de la Parte 4 y un gráfico de barras de deriva
> inelástica por piso, con una línea o columna del límite.

Abre el archivo en Excel y verifica que los números coinciden con ETABS.
Acabas de encadenar **ETABS → agente → Excel** sin escribir código.

## Parte 6 — El orquestador

**Objetivo:** pasar de un agente que hace todo a un **equipo**: cada
subagente tiene un rol, herramientas limitadas y su propio contexto; el
orquestador planifica, delega (en paralelo cuando puede) y cruza resultados.

| Agente | Herramientas | Rol |
|---|---|---|
| `analista-etabs` | solo `etabs` (+ leer/escribir `resultados/`) | Extrae datos; por defecto solo lectura |
| `consultor-normativo` | solo búsqueda en `normas` + leer PDFs | Confirma límites con cita |
| `redactor-informe` | solo `excel` (+ escribir `resultados/`) | Excel + informe Markdown |
| `orquestador-sismico` | solo puede lanzar esos 3 agentes | Planifica, cruza, concluye |

**6.1 Crea los subagentes.** Copia tu `consultor-normativo.md` del Lab 5 a
`.claude/agents/` y pide al agente que cree los demás:

> Crea en .claude/agents/ los subagentes analista-etabs (solo las
> herramientas del servidor etabs, listadas una por una, más Read y Write;
> solo lectura del modelo salvo autorización explícita; carga la skill
> e030-derivas; guarda JSON en resultados/), redactor-informe (solo las
> herramientas del servidor excel que necesite, listadas una por una, más
> Read, Write y Glob; genera
> resultados/chequeo_e030.xlsx e informe.md) y orquestador-sismico (solo
> puede invocar analista-etabs, consultor-normativo y redactor-informe;
> nunca modifica el modelo). Muéstrame cada archivo antes de guardarlo.

Si te quedas sin tiempo, copia la referencia:

```powershell
New-Item -ItemType Directory -Force .claude\agents, .claude\skills | Out-Null
Copy-Item referencia\agents\*.md .claude\agents\
Copy-Item -Recurse referencia\skills\e030-derivas .claude\skills\
```

**6.2 Ejecuta el orquestador** como agente principal de la sesión:

```powershell
claude --agent orquestador-sismico
```

> Haz el chequeo sísmico E.030 completo del modelo abierto en ETABS.

**Qué deberías ver:** el plan, la pregunta por los supuestos (R,
regularidad, zona, suelo), `analista-etabs` y `consultor-normativo`
trabajando **en paralelo**, el cruce de resultados, `redactor-informe`
generando el Excel y `resultados/informe.md`, y un resumen con lo "no
verificado".

**6.3 Compara** en la bitácora: un solo agente (Partes 3-5) vs. orquestador.
¿Cuál tardó más?, ¿cuál fue más fácil de auditar?, ¿qué pasó con el
contexto de cada subagente?

---

## Más allá de ETABS (opcional, no probado en clase)

La misma idea funciona con otros programas que tengan servidor MCP. Revisa
siempre licencia, actividad del repositorio y **qué hace al cerrar**.

| Programa | Servidor MCP | Nota |
|---|---|---|
| Excel | [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) | El usado en este lab (MIT); no necesita Excel instalado |
| AutoCAD | [puran-water/autocad-mcp](https://github.com/puran-water/autocad-mcp) | Planos 2D vía AutoLISP |
| Revit | [mcp-servers-for-revit/revit-mcp](https://github.com/mcp-servers-for-revit/revit-mcp) | Requiere plugin en Revit |
| OpenSeesPy | [pellegrino-research-group/opensees-mcp](https://github.com/pellegrino-research-group/opensees-mcp) | Útil para contrastar ETABS con otro solver; el repositorio no declara licencia |

## Reflexión: preguntas que necesitarías hacerte

1. `execute_code` permite al agente correr cualquier llamada de la API de
   ETABS. ¿Cómo limitarías lo que puede modificar, si la herramienta no
   distingue "leer" de "escribir"? ¿Basta con una instrucción en el prompt?
2. ¿El agente eligió R o la regularidad por ti en algún momento? ¿Qué error
   estructural produce un R mal asumido en la verificación de derivas?
3. El orquestador usa límites **confirmados** por el consultor. ¿Qué harías
   si el consultor no encuentra la tabla (E.030 escaneada) y el analista
   "sabe" el valor?
4. ¿Qué tareas de tu oficina se beneficiarían de un orquestador y cuáles
   son demasiado críticas para delegarlas?
5. ¿Qué debería contener la traza de un informe generado por agentes para
   que un revisor externo pueda auditarlo?

## Entrega

- `prompts_entregados.md` completado (Partes 1-6).
- Tus archivos `.claude/agents/*.md` y `.claude/skills/e030-derivas/SKILL.md`.
- `resultados/chequeo_e030.xlsx` y `resultados/informe.md` del orquestador.
- Capturas: ETABS con el modelo durante la Parte 1 o 2, y `/mcp` con los 3
  servidores conectados.

## Para el docente

- **Servidor ETABS elegido:** `Shekh-Muhsen/ETABS-MCP` v2.0.0 (MIT). Se
  conecta con `cHelper.GetObject` (patrón correcto para ETABS 20+), no llama
  `ApplicationExit`, sandbox de código, 38 skills de API/flujos, búsqueda BM25
  en 2.458 métodos de la API. **Riesgos:** repositorio de un solo autor, 1
  estrella, y el `.exe` publicado (jul-2026) incluye contenido que no está en
  el código fuente del repositorio (último commit 10-jun-2026) → no es
  reproducible desde el código. Recomendado: hacer *fork* a la organización
  del curso, fijar el release y probarlo en una PC con ETABS antes de clase.
  Nota: el release se llama `v2.0.0` pero su `manifest.json` dice `2.1.0`
  (hash verificado el 22-sep-2026).
- **Solo Windows nativo:** el `.exe` es win32 y se conecta por COM a ETABS.
  No funciona desde WSL2 ni macOS.
- **Prueba 22-sep-2026 (ETABS 21.2.0, Claude Code en Windows):** Parte 0
  tal cual, Parte 1 OK (solo lecturas), construcción de un pórtico 2 pisos +
  análisis modal OK (todos los `ret` = 0). El servidor expone 6
  herramientas: `get_status`, `list_instances`, `discover_api`,
  `read_skills`, `search_docs`, `execute_code` (el `manifest.json` solo
  lista 5). `File.NewBlank()` sobre una sesión sin modelo cerró ETABS — ver
  aviso en la Parte 2. Construir + analizar tomó más de 40 turnos del
  agente: reserva tiempo en clase. Primer intento: frames con W14X500
  (acero por defecto) en vez de las secciones de concreto pedidas, sin que
  el agente lo notara (T1 = 0.090 s). Tras reasignar COL40X40/VIGA30X50 (C21,
  f'c = 21 MPa): T1 = T2 = 0.161 s (masa mezclada UX/UY por simetría),
  T3 = 0.150 s torsional — solo peso propio, sin losa ni cargas. Con losa
  LOSA15 (ShellThin, 0.15 m) y un diafragma rígido por piso: T1 = T2 =
  0.219 s (UX/UY ≈ 0.90), T3 = 0.173 s torsional. El skill del servidor
  dice `eShellType.ShellThin = 0`; en ETABS 21.2 el valor que produce
  `Shell-Thin` en la tabla es `1`. `AddByCoord` con argumentos desordenados
  dibujó las áreas con la losa por defecto (`Slab1`) sin error.
- **Descartado:** `mdvaleed7/ETABS-mcp` (69 herramientas, IS 1893) —
  al apagarse el servidor ejecuta `disconnect()` → `ApplicationExit(False)`,
  es decir **cierra ETABS sin guardar** al terminar la sesión de Claude.
  Otros candidatos (`Aaradhya-Dev-Tamrakar/etabs-mcp`, `HuVelasco/ETABSFastMCP`)
  tienen pocas herramientas o requieren compilar C#.
- **Excel:** `excel-mcp-server==0.1.8` probado vía stdio (crear libro,
  escribir datos, gráfico) — OK.
- Los valores de la skill E.030 son didácticos: revísalos contra la versión
  oficial que uses en el curso.

Ver [`../GUIA_LABORATORIOS.md`](../GUIA_LABORATORIOS.md).

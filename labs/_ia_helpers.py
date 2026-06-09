"""Helpers compartidos para notebooks *_alumno_ia.ipynb y *_solucion_ia.ipynb."""
from __future__ import annotations


def md(*lines: str) -> dict:
    return {"cell_type": "markdown", "metadata": {}, "source": [l + "\n" for l in lines]}


def code(*lines: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [l + "\n" for l in lines],
    }


def intro_alumno_ia(
    titulo: str,
    sesion: str,
    nombre_base: str,
    nombre_solucion_ia: str,
    extra: str = "",
    *,
    solo_ia: bool = False,
) -> dict:
    lines = [
        f"# {titulo} — Vía IA-asistida",
        "",
        f"**Sesión:** {sesion}",
        "",
        "**Público:** ingenieros civiles **sin experiencia en programación** · **Entorno:** GitHub Codespaces o `labs/.venv`",
        "",
        "## Cómo trabajar (Copilot, Gemini, Cursor, etc.)",
        "",
        "1. Abre este repo en **Codespaces** o activa `source labs/.venv/bin/activate`.",
        "2. **Ejecuta** las celdas pre-escritas (carga de datos, gráficos base) en orden.",
        "3. Lee la **guía IA** de la sección: objetivo, qué considerar y el prompt sugerido.",
        "4. Copia el prompt a tu asistente; pega el código generado en la celda **«Aquí coloca tu solución»**.",
        "5. Ejecuta tu celda y la **Autoevaluación**; busca ✅ antes de avanzar.",
        "6. Registra tus prompts en [`prompts_entregados.md`](prompts_entregados.md) (entrega obligatoria).",
        f"7. Referencia docente: `{nombre_solucion_ia}` (no distribuir al inicio).",
    ]
    if not solo_ia:
        lines.extend(
            [
                "",
                f"> **Vía manual (hiperparámetros):** usa `{nombre_base}.ipynb` si prefieres editar variables sin IA.",
            ]
        )
    lines.extend(
        [
            "",
            "**La IA propone; tú validas** con autoevaluación, gráficos y sentido físico/estructural.",
        ]
    )
    if extra:
        lines.extend(["", extra])
    return md(*lines)


def intro_sol_ia(titulo: str) -> dict:
    return md(
        f"# {titulo} — Solución vía IA (solo docente)",
        "",
        "Prompts canónicos probados y código mínimo que pasa autoevaluación (✅).",
        "No comparar línea a línea con el notebook del alumno: importa que llegue a los mismos resultados.",
    )


def ia_guia_seccion(
    num: str,
    titulo_corto: str,
    objetivo: str,
    tareas: list[str],
    prompt: str,
    *,
    consideraciones: list[str] | None = None,
    vars_autoeval: list[str] | None = None,
    prompt_listo: bool = False,
    prompt_alt: str | None = None,
    nota_asistente: bool = True,
) -> dict:
    tareas_txt = "\n".join(f"- {t}" for t in tareas)
    lines = [
        f"### 🤖 Guía IA — Sección {num}: {titulo_corto}",
        "",
        f"**Objetivo:** {objetivo}",
        "",
        "**Tu código debe lograr**",
        tareas_txt,
    ]
    if vars_autoeval:
        vars_txt = ", ".join(f"`{v}`" for v in vars_autoeval)
        lines.extend(
            [
                "",
                f"**Variables obligatorias** (la autoevaluación las busca con estos nombres): {vars_txt}",
            ]
        )
    if consideraciones:
        cons_txt = "\n".join(f"- {c}" for c in consideraciones)
        lines.extend(
            [
                "",
                "**Considera en tu prompt** (menciónalo al asistente si hace falta)",
                cons_txt,
            ]
        )
    prompt_label = (
        "**Prompt listo para copiar** (sección avanzada — úsalo tal cual y adapta solo si la IA falla):"
        if prompt_listo
        else "**Prompt sugerido** (copiar al asistente y completar con el contexto de arriba):"
    )
    lines.extend(
        [
            "",
            prompt_label,
            "",
            "```text",
            prompt.strip(),
            "```",
        ]
    )
    if prompt_alt:
        lines.extend(
            [
                "",
                "**Prompt alternativo válido** (misma sección, otros parámetros permitidos):",
                "",
                "```text",
                prompt_alt.strip(),
                "```",
            ]
        )
    if nota_asistente:
        lines.append("")
        lines.append(
            "_Puedes usar GitHub Copilot, Gemini, ChatGPT o Cursor. "
            "Si falla la autoevaluación, pide a la IA que corrija usando el mensaje ❌._"
        )
    return md(*lines)


def celda_autoevaluacion(
    num: str,
    titulo: str,
    vars_requeridas: list[str],
    *lineas_verificacion: str,
) -> dict:
    """Celda de autoevaluación con mensaje claro si faltan variables del alumno."""
    vars_txt = ", ".join(f"`{v}`" for v in vars_requeridas)
    lines = [
        f"# --- Autoevaluación {num} ---",
        f"# Requiere (celda «Aquí coloca tu solución»): {vars_txt}",
        "r = []",
        "try:",
    ]
    for line in lineas_verificacion:
        lines.append(f"    {line}")
    lines.extend(
        [
            "except NameError as err:",
            '    print(f"❌ Ejecuta primero tu celda de solución. Falta: {err}")',
            "    r = [False]",
            f"resumen_seccion('{titulo}', r)",
        ]
    )
    return code(*lines)


def celda_solucion_alumno(
    *,
    variables: list[str] | None = None,
    pasos: list[str] | None = None,
    nota: str = "",
) -> dict:
    """Celda vacía con comentarios guía para pegar código generado por la IA."""
    lines = [
        "# --- Aquí coloca tu solución (código generado por la IA) ---",
        "# Ejecuta esta celda después de pegar tu código.",
        "",
    ]
    if variables:
        lines.append("# Variables OBLIGATORIAS (la autoevaluación las busca con estos nombres):")
        lines.extend(f"#   · {v}" for v in variables)
        lines.append("")
    if pasos:
        lines.append("# Tu código debe:")
        lines.extend(f"#   {i}. {p}" for i, p in enumerate(pasos, 1))
        lines.append("")
    if nota:
        lines.append(f"# Nota: {nota}")
        lines.append("")
    return code(*lines)


def task_pegar_desde_manual(task_cell: dict, header: str = "### PEGA AQUÍ EL CÓDIGO DE LA IA ###") -> dict:
    """Reemplaza el encabezado ### TU TAREA AQUÍ ### por el de pegar código IA."""
    src = list(task_cell["source"])
    out: list[str] = []
    replaced = False
    for line in src:
        if "### TU TAREA AQUÍ ###" in line and not replaced:
            out.append(header + "\n")
            replaced = True
        else:
            out.append(line)
    if not replaced:
        out.insert(0, header + "\n")
    return {**task_cell, "source": out}


def cierre_alumno_ia(checklist: str) -> dict:
    return md(
        "## Cierre y entrega (vía IA)",
        "",
        "### ✍️ Reflexión final (3 frases)",
        "- La variable que más impactó fue ___ porque ___.",
        "- Para reducir costos en planta usaría el modelo para ___.",
        "- Antes de obra real validaría con ___.",
        "",
        "### 📋 Bitácora de prompts (obligatorio)",
        "",
        "Completa [`prompts_entregados.md`](prompts_entregados.md): por cada sección, copia el prompt enviado, "
        "un resumen de la respuesta de la IA y qué aceptaste o rechazaste.",
        "",
        "---",
        f"**Checklist:** {checklist} · bitácora entregada · gráficos revisados.",
    )


def plantilla_referencia_celdas_ia(
    lab_titulo: str,
    secciones: list[tuple[str, str, list[str]]],
) -> str:
    """Markdown docente: código canónico por celda de solución (vía IA)."""
    bloques = [
        f"# Referencia de celdas — {lab_titulo}",
        "",
        "**Solo docente.** Código mínimo que pasa cada autoevaluación (✅).",
        "No distribuir al inicio del curso; úsalo para apoyar al alumno o calibrar prompts.",
        "",
        "Las celdas de **Autoevaluación** del notebook alumno asumen **exactamente** estos nombres de variable.",
        "",
        "---",
        "",
    ]
    for titulo, codigo, variables in secciones:
        vars_txt = ", ".join(f"`{v}`" for v in variables) if variables else "—"
        bloques.extend(
            [
                f"## {titulo}",
                "",
                f"**Variables obligatorias:** {vars_txt}",
                "",
                "```python",
                codigo.strip(),
                "```",
                "",
                "---",
                "",
            ]
        )
    return "\n".join(bloques)


def plantilla_prompts_entregados(lab_titulo: str, secciones: list[str]) -> str:
    bloques = []
    for s in secciones:
        bloques.append(
            f"""## {s}

**Prompt enviado:**
```
(pega aquí)
```

**Respuesta de la IA (resumen):**


**¿Qué aceptaste / rechazaste y por qué?**


---
"""
        )
    return f"""# Bitácora de prompts — {lab_titulo}

Entrega este archivo junto con tu notebook `*_alumno_ia.ipynb` ejecutado (celdas con ✅).

| Campo | Qué escribir |
|-------|----------------|
| Prompt enviado | Texto exacto que enviaste al asistente |
| Resumen | Qué código o explicación devolvió la IA |
| Aceptaste/rechazaste | Qué pegaste en el notebook y qué descartaste |

---

{"".join(bloques)}
"""

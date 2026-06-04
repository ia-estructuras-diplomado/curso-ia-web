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
        "2. En cada sección: lee el **objetivo**, copia el **prompt sugerido** a tu asistente de IA.",
        "3. Pega **solo** el código generado en la celda `### PEGA AQUÍ EL CÓDIGO DE LA IA ###`.",
        "4. Ejecuta la celda y la **Autoevaluación**; busca ✅ antes de avanzar.",
        "5. Registra tus prompts en [`prompts_entregados.md`](prompts_entregados.md) (entrega obligatoria en esta vía).",
        f"6. Referencia docente: `{nombre_solucion_ia}` (no distribuir al inicio).",
        "",
        "> **Vía manual (hiperparámetros):** usa `{nombre_base}.ipynb` si prefieres editar variables sin IA.",
        "",
        "**La IA propone; tú validas** con autoevaluación, gráficos y sentido físico/estructural.",
    ]
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
    prompt_alt: str | None = None,
    nota_asistente: bool = True,
) -> dict:
    tareas_txt = "\n".join(f"{i}. {t}" for i, t in enumerate(tareas, 1))
    lines = [
        f"### 🤖 Sección {num} — {titulo_corto}",
        "",
        f"**Objetivo:** {objetivo}",
        "",
        "**Lista de tareas**",
        tareas_txt,
        "",
        "**Prompt sugerido** (copiar al asistente):",
        "",
        "```text",
        prompt.strip(),
        "```",
    ]
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

# Lab 3: Inteligencia Artificial Explicable (xAI)

--8<-- "lab3-actions.md"

!!! info "Sesión 4"
    **Duración:** ~2 h · Vía IA-asistida

## Tema

Interpretar predicciones de **XGBoost** sobre sensores SHM con un kit xAI: importancias globales, **SHAP**, **LIME** y PDP.

| Técnica | Alcance |
|---------|---------|
| Importancia del booster | Global |
| Permutation importance | Global |
| SHAP (`TreeExplainer`) | Global + local |
| LIME | Local |
| PDP + SHAP dependence | Global marginal |

## Objetivos

1. Diferenciar explicación **global** vs **local**.
2. Aplicar varias técnicas xAI sobre un mismo modelo.
3. Comparar SHAP y LIME en un caso de test.
4. Interpretar en lenguaje de ingeniería estructural.

## Archivos

| Archivo | Uso |
|---------|-----|
| `xai_estructuras_alumno_ia.ipynb` | Notebook alumno |
| `prompts_entregados.md` | Bitácora de prompts |
| `data/` | Dataset SHM (Lab 1) |

## Pasos

1. **Crear Codespace** (botón arriba).
2. `cd labs/lab3` → abrir `xai_estructuras_alumno_ia.ipynb`.
3. Completar `prompts_entregados.md`.

[Codespaces](codespaces.md)

# Lab 3: Inteligencia Artificial Explicable (xAI)

--8<-- "lab3-actions.md"

!!! warning "En desarrollo"
    Notebook en `labs/lab3/` — se publicará vía sync desde `curso-ia-dev`.

!!! info "Sesión 6"
    **Duración:** ~2 horas (previsto)

## ¿Qué es xAI?

**Inteligencia Artificial Explicable (xAI)** permite entender **por qué** un modelo produce una predicción — no solo el resultado numérico o la clase.

En obra importa porque:

- Un modelo puede acertar por variables correctas o por **artefactos** del dataset.
- El ingeniero necesita **trazabilidad** antes de decisiones sobre dosificación, alertas o inspección.
- xAI **apoya** la revisión humana; no sustituye el criterio profesional.

### xAI vs caja negra

| Enfoque | Qué obtienes | Limitación |
|---------|--------------|------------|
| **Caja negra** | Predicción (ŷ, clase, probabilidad) | No sabes qué variables la motivaron |
| **xAI global** | Importancias promedio (Random Forest) | No explica un caso individual |
| **xAI local** | Explicación de **una** predicción (SHAP, LIME) | Inestable con pocos datos |

### Técnicas previstas

- Importancias de features (modelos de árboles)
- **SHAP** — contribución de cada variable a una predicción
- Gráficos: summary plot, waterfall, dependencia parcial
- Contraste con **Lab 1** (SHM) y **Lab 2** (hormigón)

## Objetivos de aprendizaje

1. Diferenciar explicación **global** vs **local**.
2. Aplicar SHAP sobre un modelo ya entrenado.
3. Redactar interpretación en lenguaje de ingeniería (2–3 frases por predicción).
4. Detectar cuándo la explicación **no es fiable** (datos fuera de distribución, correlación espuria).

## Archivos previstos

| Archivo | Uso |
|---------|-----|
| `xai_estructuras_alumno.ipynb` | Notebook del alumno |
| `xai_estructuras_solucion.ipynb` | Referencia docente |
| `_verificar.py` | Autoevaluación ✅ / ❌ |
| `data/` | Ejemplos o exportados desde Lab 1 / Lab 2 |

## Pasos en Codespaces (cuando esté disponible)

1. **Crear Codespace — Lab 3** (arriba).
2. Abrir `labs/lab3/xai_estructuras_alumno.ipynb`.

---

**¿Dudas?** → [Codespaces](codespaces.md)

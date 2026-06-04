# Lab 3 — Inteligencia Artificial Explicable (xAI)

**Sesión 6** · Interpretar y auditar predicciones de modelos ML en contexto de ingeniería estructural.

## ¿Qué es xAI?

**Inteligencia Artificial Explicable (xAI)** es el conjunto de métodos que permiten **entender por qué** un modelo produce una predicción concreta — no solo el resultado numérico o la clase asignada.

En obra esto importa porque:

- Un modelo puede acertar por las **variables correctas** (p. ej. deformación, edad del hormigón) o por **artefactos** del dataset.
- El ingeniero estructural necesita **trazabilidad** antes de tomar decisiones sobre dosificación, alertas de daño o inspección.
- La normativa y el criterio profesional exigen **validación humana**; xAI apoya esa revisión, no la reemplaza.

### xAI vs caja negra

| Enfoque | Qué obtienes | Limitación |
|---------|--------------|------------|
| **Caja negra** | Predicción (ŷ, clase, probabilidad) | No sabes qué variables la motivaron |
| **xAI global** | Importancias promedio (p. ej. en Random Forest) | No explica un caso individual |
| **xAI local** | Explicación de **una** predicción (SHAP, LIME) | Puede ser inestable con pocos datos |

### Técnicas previstas en este lab

- **Importancias de features** (modelos de árboles) — visión global rápida.
- **SHAP** (SHapley Additive exPlanations) — contribución de cada variable a una predicción.
- **Gráficos de explicación** — summary plot, waterfall, dependencia parcial.
- **Contraste con Lab 1 / Lab 2** — explicar clasificación de daño (SHM) o regresión de resistencia (hormigón).

## Estado

**En desarrollo.**

Cuando esté listo, esta carpeta incluirá:

| Archivo | Uso |
|---------|-----|
| `xai_estructuras_alumno.ipynb` | Notebook del alumno |
| `xai_estructuras_solucion.ipynb` | Referencia docente |
| `xai_estructuras_alumno_ia.ipynb` | *(al publicar)* Vía IA + `prompts_entregados.md` |
| `xai_estructuras_solucion_ia.ipynb` | *(al publicar)* Prompts canónicos docente |
| `_verificar.py` | Autoevaluación ✅ / ❌ |
| `data/` | Datos de ejemplo o exportados desde Lab 1 / Lab 2 |

## Objetivos de aprendizaje

1. Diferenciar explicación **global** vs **local** de un modelo.
2. Aplicar SHAP (u otra técnica acordada) sobre un modelo ya entrenado.
3. Redactar una interpretación en lenguaje de ingeniería (2–3 frases por predicción).
4. Identificar cuándo la explicación del modelo **no es fiable** (datos fuera de distribución, correlación espuria).

## Entorno local

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/lab3
jupyter notebook xai_estructuras_alumno.ipynb
```

## GitHub Codespaces

Abrir `labs/lab3/xai_estructuras_alumno.ipynb` (cuando esté publicado).

Guía del curso: [Lab 3 en curso-ia-web](https://ia-estructuras-diplomado.github.io/curso-ia-web/labs/lab3/)

Ver [`../GUIA_LABORATORIOS.md`](../GUIA_LABORATORIOS.md)

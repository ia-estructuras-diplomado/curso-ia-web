# Datos — Lab 6 Agentes sísmicos

## Fuente

| Archivo | Descripción |
|---------|-------------|
| `archive.zip` | Dataset versionado en el repo (~415 KB) |
| `seismic_data.csv` | Extraído con `_preparar_datos.py` (gitignored) |
| `earthquake_risk_model.pkl` | Best model MLP entrenado offline (`_generar_modelo.py`) |
| `model_meta.json` | Métricas y arquitectura del modelo |

El CSV contiene **1000 escenarios** sísmico-estructurales. El **best model MLP** se entrena offline (`_generar_modelo.py`) con features del CSV y etiquetas de riesgo por criterio de ingeniería (el target original del CSV no correlaciona con 3 variables aisladas).

## Columnas usadas en el lab

| Columna CSV | Uso en tools |
|-------------|--------------|
| `Spectral Acceleration (g)` | `expected_pga_g` |
| `Soil Type` | `soil_type_index` (Rock=1, Sand=2, Clay/Soft Soil=3) |
| `Natural Frequency (Hz)` | `structural_period_s = 1 / f` |
| `Predicted Max Inter-Story Drift Ratio (%)` | Telemetría / norma ASCE 7 |
| `Predicted Collapse Probability (%)` | Target de entrenamiento del MLP (≥70% → daño severo) |

## Edificios de demostración (filas ancla)

| ID | Material | Suelo | Drift | Colapso | Narrativa |
|----|----------|-------|-------|---------|-----------|
| BLDG-A | Acero | Rock | ~0.5% | ~37% | Norma OK + ML bajo |
| BLDG-B | Concreto | Clay | ~3.6% | ~86% | Falla norma + alerta ML |
| BLDG-C | Composite | Soft Soil | ~0.8% | ~96% | Norma OK + ML crítico |

Los valores exactos están en `TELEMETRIA_DB` dentro de `_verificar.py`.

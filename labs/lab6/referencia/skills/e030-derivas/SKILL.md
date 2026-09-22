---
name: e030-derivas
description: Procedimiento para verificar derivas de entrepiso, participación de masa y cortante basal mínima según la norma peruana E.030 a partir de resultados de ETABS. Úsalo cuando se pida un chequeo sísmico E.030 de un modelo ETABS.
---

# Verificación E.030 desde resultados de ETABS

> Valores transcritos de la E.030-2018 para uso didáctico. **Antes de emitir
> un veredicto, confirma cada límite con el subagente `consultor-normativo`
> (o leyendo la norma) y cita la página.** La norma oficial vigente prevalece.

## 1. Parámetros del espectro (Sa = Z·U·C·S / R · g)

| Zona | Z |
|---|---|
| 4 | 0.45 |
| 3 | 0.35 |
| 2 | 0.25 |
| 1 | 0.10 |

| Suelo | S (Z4) | S (Z3) | S (Z2) | S (Z1) | TP (s) | TL (s) |
|---|---|---|---|---|---|---|
| S0 | 0.80 | 0.80 | 0.80 | 0.80 | 0.3 | 3.0 |
| S1 | 1.00 | 1.00 | 1.00 | 1.00 | 0.4 | 2.5 |
| S2 | 1.05 | 1.15 | 1.20 | 1.60 | 0.6 | 2.0 |
| S3 | 1.10 | 1.20 | 1.40 | 2.00 | 1.0 | 1.6 |

- C = 2.5 si T < TP; C = 2.5·TP/T si TP ≤ T ≤ TL; C = 2.5·TP·TL/T² si T > TL.
- U: edificaciones comunes (C) = 1.0; importantes (B) = 1.3; esenciales (A2) = 1.5.
- R = R0 · Ia · Ip. R0 concreto armado: pórticos 8, dual 7, muros estructurales 6,
  muros de ductilidad limitada 4.

## 2. Chequeos a reportar

1. **Participación de masa modal:** la suma de masas efectivas debe llegar
   al menos al **90 %** de la masa total en cada dirección de análisis.
2. **Cortante basal mínima (análisis dinámico):** V_dinámico ≥ **80 %**
   V_estático (estructura regular) o ≥ **90 %** (irregular). Si no cumple,
   reportar el factor de escala necesario — **no** reescalar el modelo sin
   autorización.
3. **Derivas de entrepiso:**
   - ETABS entrega la deriva **elástica** del caso espectral (espectro ya
     reducido por R).
   - Deriva **inelástica** = 0.75·R × deriva elástica (estructura regular) o
     0.85·R × deriva elástica (irregular).
   - Límites (Tabla N° 11):

     | Material predominante | Δi / hei máx. |
     |---|---|
     | Concreto armado | 0.007 |
     | Acero | 0.010 |
     | Albañilería | 0.005 |
     | Madera | 0.010 |
     | Concreto armado con muros de ductilidad limitada | 0.005 |

## 3. Cómo extraer los datos en ETABS (vía MCP etabs)

- Unidades: `model.SetPresentUnits(6)` (kN, m, °C).
- Si el modelo no está analizado: **pregunta al usuario** antes de ejecutar
  `model.Analyze.RunAnalysis()`.
- Masa modal: `model.Results.ModalParticipatingMassRatios()`.
- Cortante basal: `model.Results.BaseReact()` con los casos seleccionados.
- Derivas: `model.Results.StoryDrifts()` con los casos sísmicos seleccionados
  (`Results.Setup.SetCaseSelectedForOutput`). Consulta las skills
  `workflow-story-drift` y `workflow-modal-report` del servidor ETABS para el
  orden exacto de los arreglos devueltos.

## 4. Formato de salida

Tabla por piso y dirección: piso, caso, deriva elástica, factor (0.75R u
0.85R), deriva inelástica, límite, CUMPLE/NO CUMPLE. Luego un resumen con la
deriva máxima, su piso y dirección, y los supuestos usados (R, regularidad,
material). Si falta un dato (R, regularidad), **pregúntalo**; no lo asumas en
silencio.

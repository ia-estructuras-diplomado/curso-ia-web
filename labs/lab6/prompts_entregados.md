# Bitácora — Lab 6 — Orquestadores: el arnés de un chequeo E.030

Entrega este archivo junto con tus `.claude/agents/*.md`,
`.claude/skills/e030-derivas/SKILL.md`, la copia
`resultados/parte5/` (Excel e informe de antes de la Parte 6) y las
capturas pedidas en el README.

| Campo | Qué escribir |
|-------|----------------|
| Prompt enviado | Texto exacto que le diste al agente |
| Línea `tools` | La que quedó en el archivo, copiada del `.md` |
| Traza | Qué rol se llamó, en qué orden, y si el orquestador tocó ETABS |
| Verificación | Qué comprobaste tú en ETABS, en el PDF o en el Excel |

Versión de ETABS: ________ · Modo de acceso (A/B/C + modelo): ________ · Ejemplo de la Parte 5 (irregular): ________

---

## Parte 1 — El contrato del arnés

Completa con tus palabras, después de leer `referencia/agents/`.

| Rol | Línea `tools` (resumen) | ¿Carga la skill? | Artefacto | Cuándo se detiene |
|---|---|---|---|---|
| analista-etabs | | | | |
| experto-modelo | | | | |
| consultor-normativo | | | | |
| redactor-informe | | | | |
| revisor-independiente | | | | |
| orquestador-sismico | | | | |

**Por qué el peso sísmico lo escribe el experto y el analista solo lo cita:**


**Por qué la skill no la carga el orquestador:**


**Qué podría hacer el analista si borras del prompt la frase de solo lectura y dejas la línea `tools`:**


---

## Parte 2 — Los roles

**Prompt del revisor:**
```
(pega aquí)
```

**Línea `tools` del revisor:**


**Prompt de la skill:**
```
(pega aquí)
```

**Citas con las que confirmaste los valores [archivo, página]:**


**Una diferencia con `referencia/skills/e030-derivas/SKILL.md`:**


**Prompt del experto:**
```
(pega aquí)
```

**Línea `tools` del experto, y qué archivo escribe:**


**Prompt del analista:**
```
(pega aquí)
```

**Línea `tools` del analista, y la frase que le impide modificar el modelo:**


**Prompt del redactor:**
```
(pega aquí)
```

**Línea `tools` del redactor:**


---

## Parte 3 — El orquestador

**Prompt enviado:**
```
(pega aquí)
```

**Regla de parada, en una frase:**


**Quién corre en el mismo turno y quién espera:**


**¿Copiaste la referencia por tiempo? (sí / no):**


---

## Parte 4 — Los dos ejemplos

**Ficha del regular (mass source: opción y factores; ¿Dead entra?; losas por piso; vacíos; muros):**


**Ficha del irregular (vacío: coordenadas y pisos; muro: en qué eje):**


**¿El experto usó Dead+Live o CV al 100 % como peso sísmico?:**


**Una llamada `execute_code` que entendiste y una que no:**


---

## Parte 5 — Traza del orquestador

**¿El orquestador se detuvo cuando dijiste que el irregular era regular?:**


**Subagentes, en orden. ¿El experto fue antes que el analista?:**


**¿Ese orden es el del `demo.html`, Caso B (experto, parada, luego analista y consultor juntos)?:**


**¿Algún `execute_code` lo pidió el orquestador?:**


**Pasada 1 — chequeo que falló (o "ninguno"):**


**Pasada 2 — qué fila se repitió y si ya coincidió:**


**Veredicto del revisor, y si citó archivos o el resumen del chat:**


**Qué quedó "no verificado" y por qué:**


**¿La segunda lectura atrapó un número que la primera había dado por bueno?:**


---

## Parte 6 — El arnés bajo presión

**6.1 ¿El archivo impidió cerrar sin el revisor, o el mensaje ganó? Pega la frase que debía detenerlo:**


**6.2 ¿Publicó 0.007 como CUMPLE, o lo dejó "no verificado"? Pega la frase que debía detenerlo:**


**6.3 Frase que propuso el orquestador:**


**¿La aceptaste o la rechazaste, y por qué? Si la rechazaste, qué escribiste tú:**


**Qué pasó al repetir solo la prueba que había fallado:**


**En una frase, en qué se distingue este bucle del de las dos pasadas:**


---

## Lecturas

Una frase por paper: qué pieza de tu arnés reconoces ahí.

**Barbaste et al., 2026 (arnés):**


**He et al., 2026 (control, agencia, runtime):**


**Robeyns et al., 2025 (self-improvement):**


**Zhang et al., 2025 (archivo de agentes y benchmark):**


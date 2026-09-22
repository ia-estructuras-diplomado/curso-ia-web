# Lab 5: Tu primer agente — Claude Code + MCP de normas (RAG)

--8<-- "lab5-actions.md"

!!! info "Sesión 9"
    **Duración:** ~3 horas · Sin notebook: guía paso a paso

## Tema

Usarás un agente de IA real (**Claude Code**) conectado por **MCP** a un
buscador RAG local sobre las normas peruanas **E.020, E.030 y E.050**. No
programas el RAG: ves funcionar al agente, auditas sus citas y terminas
definiendo tu propio **subagente** especializado (`consultor-normativo`).

## Objetivos de aprendizaje

1. Entender el bucle de un **agente**: decide qué herramienta usar, la
   ejecuta, lee el resultado y vuelve a decidir.
2. Entender **MCP** como el "enchufe estándar" entre un agente y programas externos.
3. Usar **RAG como herramienta** y verificar cada cita (archivo y página).
4. Ver un modo de falla real: la E.030 escaneada que el RAG no puede indexar.
5. Crear un subagente reutilizable para el Lab 6.

## Acceso al modelo

| Opción | Cuándo |
|---|---|
| **A.** Suscripción Claude (Pro/Max) | Recomendado |
| **B.** API key del curso | Si el docente entregó créditos |
| **C.** Gratis con Ollama (`ollama launch claude`) | Sin costo; respuestas más irregulares. Para leer la E.030 escaneada (Parte 4) usa Claude Desktop o claude.ai |

Instalación, prompts y entrega:
[**guía completa del Lab 5**](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab5/README.md).

---

**¿Dudas?** → [Instalación](instalacion.md) · [FAQ](../faq.md)

# Lab 6: Agentes con ETABS — de un agente a un orquestador

--8<-- "lab6-actions.md"

!!! info "Sesión 10"
    **Duración:** ~3 horas · Sin notebook: guía paso a paso

!!! warning "Requisitos"
    **Windows nativo** (no WSL2, no macOS) con **ETABS 21 o superior** con
    licencia, y Claude Code instalado desde PowerShell en esa misma PC
    ([Lab 5](lab5.md)). Si no tienes ETABS, trabaja en pareja.

## Tema

Conectarás Claude Code a **ETABS** y a **Excel** mediante MCP, verás al
agente consultar y analizar tu modelo en tiempo real, y terminarás armando
un **orquestador** que coordina tres subagentes para un chequeo sísmico
E.030 completo.

```
                    ┌─► analista-etabs ─────► MCP etabs ──► ETABS (modelo abierto)
 Tú ─► orquestador ─┼─► consultor-normativo ► MCP normas ─► PDFs E.020/E.030/E.050
                    └─► redactor-informe ───► MCP excel ──► chequeo_e030.xlsx
```

## Objetivos de aprendizaje

1. Conectar un agente a un programa de ingeniería real y entender qué puede
   y qué **no** debe hacer sobre tu modelo.
2. Encadenar ETABS → agente → Excel sin escribir código.
3. Dar conocimiento de dominio al agente con una *skill* (derivas E.030).
4. Pasar de un agente a un **orquestador + subagentes** con herramientas limitadas por rol.

Instalación del servidor ETABS, prompts y entrega:
[**guía completa del Lab 6**](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab6/README.md).

---

**¿Dudas?** → [Instalación](instalacion.md) · [FAQ](../faq.md)

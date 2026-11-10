# Lab 6: Orquestadores — el arnés de un chequeo E.030

--8<-- "lab6-actions.md"

!!! info "Sesión 10"
    **Duración:** ~3 horas · Sin notebook: guía paso a paso

!!! warning "Requisitos"
    **Windows nativo** (no WSL2, no macOS) con **ETABS 21 o superior** con
    licencia, y Claude Code instalado desde PowerShell en esa misma PC
    ([Lab 5](lab5.md)). Los dos modelos de la sesión están en la carpeta
    `ejemplos/` del lab. Si no tienes ETABS, trabaja en pareja.

## Tema

Diseñarás el **arnés** de un chequeo sísmico E.030. Un **experto del
modelo** lee primero cargas, peso sísmico y geometría — vacíos y
asimetría incluidos — y deja una ficha. El analista saca resultados sobre
esa ficha, sin volver a interpretar el modelo. Hay dos archivos fijos:
uno regular y uno con un vacío de losa y un muro en un solo eje.

```
                    ┌─► experto-modelo ─────► ficha: cargas, peso sísmico, vacíos
 Tú ─► orquestador ─┼─► analista-etabs ─────► resultados, citando la ficha
                    ├─► consultor-normativo ► MCP normas ─► PDFs E.020/E.030/E.050
                    ├─► redactor-informe ───► MCP excel ──► chequeo_e030.xlsx
                    └─► revisor-independiente  (lee la ficha, el JSON, el informe y el Excel)
```

Ese orden se proyecta con `labs/lab6/demo.html`. El Caso A (`regular.edb`)
recorre los seis roles. El Caso B (`irregular.edb`) se detiene si la
primera respuesta dice que el edificio es regular.

## Objetivos de aprendizaje

1. Nombrar las piezas de un arnés agentico: rol, herramientas, artefacto y regla de parada.
2. Escribir un orquestador que delega, cruza citas con números y no cierra el chequeo por su cuenta.
3. Separar una falla de transcripción (se repite esa fila) de un defecto del modelo (el bucle se detiene).
4. Probar el arnés y dejar, en una sola vuelta, la regla que faltaba escrita en el archivo del orquestador.
5. Distinguir ese bucle del que solo repite una fila, con cuatro papers de arnés y de self-improvement.

Instalación del servidor ETABS, prompts y entrega:
[**guía completa del Lab 6**](https://github.com/ia-estructuras-diplomado/curso-ia-web/blob/main/labs/lab6/README.md).

---

**¿Dudas?** → [Instalación](instalacion.md) · [FAQ](../faq.md)

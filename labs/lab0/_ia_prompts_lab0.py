"""Prompts IA para Lab 0."""
from __future__ import annotations

from _ia_helpers import ia_guia_seccion

IA_S0 = ia_guia_seccion(
    "0", "Sintaxis",
    "Practicar variables, len() y f-string.",
    ["NOMBRE_MODELO texto", "MULTIPLICADOR entero", "resultado_sintaxis = len*mult"],
    """Lab Python IA. ### PEGA AQUÍ ###:
NOMBRE_MODELO = "Mi-Primer-ML"
MULTIPLICADOR = 2
resultado_sintaxis = len(NOMBRE_MODELO) * MULTIPLICADOR
print(f"Resultado: {resultado_sintaxis}")""",
)

IA_S1A = ia_guia_seccion(
    "1a", "Imports",
    "Usar math.sqrt con un número positivo.",
    ["NUMERO_PARA_RAIZ positivo (25 da 5.0)", "raiz_cuadrada = math.sqrt(...)"],
    """import math ya ejecutado arriba. ### PEGA AQUÍ ###:
NUMERO_PARA_RAIZ = 25
raiz_cuadrada = math.sqrt(NUMERO_PARA_RAIZ)
print(f"√{NUMERO_PARA_RAIZ} = {raiz_cuadrada}")""",
    prompt_alt="NUMERO_PARA_RAIZ = 81 → raíz 9.0; también pasa ✅.",
)

IA_S1B = ia_guia_seccion(
    "1b", "Paquetes",
    "Comprobar versión de pandas instalada.",
    ["VERSION_MINIMA_OK = 2.0", "version_actual = pd.__version__"],
    """pandas ya importado como pd. ### PEGA AQUÍ ###:
VERSION_MINIMA_OK = 2.0
version_actual = pd.__version__
print(f"pandas {version_actual} | mínimo requerido {VERSION_MINIMA_OK}")""",
)

IA_S2A = ia_guia_seccion(
    "2a", "Listas",
    "Indexar la lista edades_clientes.",
    ["INDICE_CLIENTE = 0, 2 o 4", "cliente_seleccionado = edades_clientes[indice]"],
    """edades_clientes = [25, 34, 45, 28, 52] ya definida. ### PEGA AQUÍ ###:
INDICE_CLIENTE = 2
cliente_seleccionado = edades_clientes[INDICE_CLIENTE]
print posición y edad""",
)

IA_S2B = ia_guia_seccion(
    "2b", "Diccionario",
    "Añadir ciudad al perfil JSON.",
    ["CIUDAD_USUARIO = 'Bogotá'", "perfil_usuario['ciudad'] = ..."],
    """perfil_usuario dict ya definido. ### PEGA AQUÍ ###:
CIUDAD_USUARIO = "Bogotá"
perfil_usuario["ciudad"] = CIUDAD_USUARIO
print perfil_usuario.get("ciudad")""",
)

IA_S3 = ia_guia_seccion(
    "3", "Comprehension",
    "Aplicar descuento 10% si precio > umbral.",
    ["UMBRAL_DESCUENTO = 100", "precios_con_descuento con list comprehension"],
    """precios = [100, 250, 45, 800, 120] arriba. ### PEGA AQUÍ ###:
UMBRAL_DESCUENTO = 100
precios_con_descuento = [precio * 0.9 if precio > UMBRAL_DESCUENTO else precio for precio in precios]
print precios_con_descuento""",
)

IA_S4 = ia_guia_seccion(
    "4", "Funciones",
    "Llamar predecir_riesgo como tool de agente.",
    ["INGRESOS_PARA_PROBAR = 60000 (o 15000/30000)", "resultado_agente con perfil_usuario['edad']"],
    """def predecir_riesgo ya definida. ### PEGA AQUÍ ###:
INGRESOS_PARA_PROBAR = 60_000
resultado_agente = predecir_riesgo(perfil_usuario["edad"], INGRESOS_PARA_PROBAR)
print('Tool →', resultado_agente)""",
)

IA_S5 = ia_guia_seccion(
    "5", "Pandas",
    "Filtrar salarios y contar compras.",
    ["UMBRAL_SALARIO=55000", "filtro y cuantas_compraron"],
    """df ya definido (4 filas). ### PEGA AQUÍ ###:
UMBRAL_SALARIO = 55_000
filtro = df[df['Salario'] > UMBRAL_SALARIO]
cuantas_compraron = int(filtro['Compro'].sum())
display(filtro); print compraron""",
)

IA_S6 = ia_guia_seccion(
    "6", "Visualización",
    "Interpretar el gráfico de salarios (sin código nuevo obligatorio).",
    [
        "Ejecutar celda de gráfico pre-escrita",
        "Registrar en prompts_entregados.md por qué validar visualmente",
    ],
    """No hay celda de código editable. Observa el gráfico de la sección 6.
En prompts_entregados.md explica en 2 líneas por qué conviene validar visualmente antes de una métrica.""",
)

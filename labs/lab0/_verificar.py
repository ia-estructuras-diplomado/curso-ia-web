"""Autoevaluación amigable para notebooks (sin autograders externos)."""


def verificar(condicion: bool, ok: str, fail: str) -> bool:
    """Imprime retroalimentación y devuelve si pasó."""
    print(ok if condicion else fail)
    return condicion


def resumen_seccion(nombre: str, resultados: list[bool]) -> None:
    """Cierra un bloque de ejercicios con mensaje claro."""
    if all(resultados):
        print(f"\n✅ Sección {nombre} completada. Puedes continuar.")
    else:
        print(
            f"\n❌ Sección {nombre}: revisa las celdas marcadas con "
            "### TU TAREA AQUÍ ### y vuelve a ejecutar."
        )


def verificar_sintaxis(resultado: int, nombre: str, multiplicador: int) -> list[bool]:
    esperado = len(nombre) * multiplicador
    return [
        verificar(
            isinstance(nombre, str) and len(nombre) > 0,
            "✅ Variable de texto (str) definida correctamente.",
            "❌ NOMBRE_MODELO debe ser un string no vacío.",
        ),
        verificar(
            resultado == esperado,
            f"✅ Cálculo sintaxis: len('{nombre}') × {multiplicador} = {resultado}.",
            f"❌ Esperábamos {esperado}. Revisa NOMBRE_MODELO y MULTIPLICADOR.",
        ),
    ]


def verificar_imports(raiz: float, numero: float) -> list[bool]:
    esperado = numero**0.5
    return [
        verificar(
            abs(raiz - esperado) < 1e-9,
            f"✅ import math funcionó: √{numero} = {raiz}",
            f"❌ La raíz de {numero} debería ser {esperado}. ¿Ejecutaste la celda pre-escrita?",
        ),
        verificar(
            numero > 0,
            "✅ NUMERO_PARA_RAIZ es positivo (math.sqrt no aplica bien a negativos en ℝ).",
            "❌ Usa un número positivo en ### TU TAREA AQUÍ ###.",
        ),
    ]


def verificar_paquetes(version_str: str, minima: float, pd_module) -> list[bool]:
    try:
        version_num = float(".".join(version_str.split(".")[:2]))
    except (ValueError, AttributeError):
        version_num = 0.0
    return [
        verificar(
            pd_module is not None and hasattr(pd_module, "DataFrame"),
            "✅ Módulo pandas importado (`import pandas as pd`).",
            "❌ Ejecuta la celda pre-escrita de imports antes de continuar.",
        ),
        verificar(
            version_num >= minima,
            f"✅ pandas {version_str} instalado (mínimo {minima}).",
            f"❌ Se requiere pandas ≥ {minima}. Ejecuta: bash labs/setup.sh",
        ),
    ]


def verificar_listas(edades, indice: int, valor_esperado) -> list[bool]:
    r = []
    r.append(
        verificar(
            edades is not None and len(edades) == 5,
            "✅ Lista de edades cargada correctamente (5 clientes).",
            "❌ La lista de edades no tiene 5 elementos. Ejecuta la celda de setup.",
        )
    )
    r.append(
        verificar(
            edades[indice] == valor_esperado,
            f"✅ Índice {indice}: obtuviste {edades[indice]} (correcto para esta tarea).",
            f"❌ Con INDICE_CLIENTE={indice} deberías ver {valor_esperado}. "
            "Revisa la variable en ### TU TAREA AQUÍ ###.",
        )
    )
    return r


def verificar_diccionario(perfil, ciudad_esperada: str) -> list[bool]:
    r = []
    r.append(
        verificar(
            perfil.get("nombre") == "Ana",
            "✅ Perfil de usuario cargado (API/JSON simulado).",
            "❌ Falta el nombre en el diccionario. Ejecuta la celda pre-escrita.",
        )
    )
    r.append(
        verificar(
            perfil.get("ciudad") == ciudad_esperada,
            f"✅ Ciudad registrada: {ciudad_esperada}.",
            f"❌ Asigna CIUDAD_USUARIO = '{ciudad_esperada}' en ### TU TAREA AQUÍ ###.",
        )
    )
    return r


def verificar_precios(precios_resultado, umbral: float) -> list[bool]:
    esperado = [p * 0.9 if p > umbral else p for p in [100, 250, 45, 800, 120]]
    ok = precios_resultado == esperado
    return [
        verificar(
            ok,
            f"✅ Descuentos coherentes con UMBRAL_DESCUENTO = {umbral}.",
            f"⚠️ Los precios no coinciden con umbral {umbral}. "
            "¿Modificaste solo UMBRAL_DESCUENTO en ### TU TAREA AQUÍ ###?",
        )
    ]


def verificar_riesgo(resultado: str, ingresos: float, esperado: str) -> list[bool]:
    return [
        verificar(
            resultado == esperado,
            f"✅ Con ingresos {ingresos:,.0f} el riesgo es «{resultado}» (esperado).",
            f"❌ Con ingresos {ingresos:,.0f} esperábamos «{esperado}», obtuviste «{resultado}». "
            "Prueba INGRESOS_PARA_PROBAR en ### TU TAREA AQUÍ ###.",
        )
    ]


def verificar_pandas(df, filtro, cuantas: int, umbral: int) -> list[bool]:
    r = []
    r.append(
        verificar(
            df is not None and df.shape == (4, 4),
            "✅ DataFrame listo para ML (4 filas × 4 columnas).",
            "❌ El DataFrame no tiene la forma esperada. Ejecuta celdas pre-escritas.",
        )
    )
    r.append(
        verificar(
            len(filtro) == 3,
            f"✅ Filtro Salario > {umbral:,}: {len(filtro)} registros.",
            f"❌ Con UMBRAL_SALARIO = {umbral} deberías obtener 3 filas.",
        )
    )
    r.append(
        verificar(
            cuantas == 2,
            "✅ Entre ese grupo, 2 clientes compraron (Compro = 1).",
            "❌ Cuenta incorrecta de compras en el subconjunto filtrado.",
        )
    )
    return r

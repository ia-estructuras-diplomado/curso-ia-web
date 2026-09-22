# Lab 0 — Fundamentos de Python para IA

## Objetivo

Repasar lo mínimo de Python necesario para trabajar con datos e IA en los siguientes labs, sin asumir experiencia previa de programación: variables y tipos, imports, listas/diccionarios, comprehensions, funciones y pandas. Este es el lab de "rampa de entrada" del curso.

## Contexto de ingeniería

Los labs 1–6 asumen que puedes leer y escribir código Python básico y entender por qué un ingeniero valida resultados visualmente antes de confiar en una métrica. Este lab construye esa base con ejemplos deliberadamente simples (no de ingeniería civil todavía) para que el foco esté en el lenguaje.

## Entorno

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
```

## Notebook de referencia

`fundamentos_python_ia.ipynb` es un notebook completo y ejecutable de punta a punta. Ábrelo, ejecútalo (**Run All**) para ver el resultado esperado de cada sección, y luego construye tu propio notebook guiándote por las secciones siguientes y por tu asistente de IA (Copilot, Gemini, ChatGPT, Cursor, etc.).

## Secciones y prompts sugeridos

### Sección 0 — Sintaxis
**Objetivo:** practicar variables, `len()` y f-strings.
**Qué debería producir tu celda:** un texto (`NOMBRE_MODELO`), un entero (`MULTIPLICADOR`) y `resultado_sintaxis`, calculado como `len(NOMBRE_MODELO) * MULTIPLICADOR`, impreso con un f-string.
**Prompt sugerido para tu asistente IA:**
> Lab Python IA. Defina NOMBRE_MODELO como texto, MULTIPLICADOR como entero, y resultado_sintaxis = len(NOMBRE_MODELO) * MULTIPLICADOR. Imprima el resultado con un f-string.

### Sección 1a — Imports
**Objetivo:** usar `math.sqrt` con un número positivo.
**Qué debería producir tu celda:** `NUMERO_PARA_RAIZ` (positivo, por ejemplo 25) y `raiz_cuadrada = math.sqrt(NUMERO_PARA_RAIZ)`, impresos con un f-string.
**Prompt sugerido:**
> import math ya ejecutado arriba. Defina NUMERO_PARA_RAIZ = 25 y raiz_cuadrada = math.sqrt(NUMERO_PARA_RAIZ). Imprima "√{NUMERO_PARA_RAIZ} = {raiz_cuadrada}".

**Prompt alternativo válido:** `NUMERO_PARA_RAIZ = 81` (→ raíz 9.0) también es una solución correcta.

### Sección 1b — Paquetes
**Objetivo:** comprobar la versión de pandas instalada.
**Qué debería producir tu celda:** `VERSION_MINIMA_OK = 2.0` y `version_actual = pd.__version__`, impresos juntos.
**Prompt sugerido:**
> pandas ya importado como pd. Defina VERSION_MINIMA_OK = 2.0 y version_actual = pd.__version__. Imprima ambos valores.

### Sección 2a — Listas
**Objetivo:** indexar la lista `edades_clientes`.
**Qué debería producir tu celda:** `INDICE_CLIENTE` (0, 2 o 4) y `cliente_seleccionado = edades_clientes[INDICE_CLIENTE]`, impresos.
**Prompt sugerido:**
> edades_clientes = [25, 34, 45, 28, 52] ya definida. Defina INDICE_CLIENTE = 2 y cliente_seleccionado = edades_clientes[INDICE_CLIENTE]. Imprima la posición y la edad.

### Sección 2b — Diccionario
**Objetivo:** añadir una ciudad al perfil JSON.
**Qué debería producir tu celda:** `CIUDAD_USUARIO` (texto) asignado a `perfil_usuario["ciudad"]`.
**Prompt sugerido:**
> perfil_usuario dict ya definido. Defina CIUDAD_USUARIO = "Bogotá" y asígnelo a perfil_usuario["ciudad"]. Imprima perfil_usuario.get("ciudad").

### Sección 3 — Comprehension
**Objetivo:** aplicar un descuento del 10% a los precios por encima de un umbral.
**Qué debería producir tu celda:** `UMBRAL_DESCUENTO = 100` y `precios_con_descuento`, construida con una list comprehension sobre `precios`.
**Prompt sugerido:**
> precios = [100, 250, 45, 800, 120] ya definida arriba. Defina UMBRAL_DESCUENTO = 100 y precios_con_descuento usando una list comprehension que aplique 10% de descuento si precio > UMBRAL_DESCUENTO. Imprima el resultado.

### Sección 4 — Funciones
**Objetivo:** llamar `predecir_riesgo` como si fuera una *tool* de un agente.
**Qué debería producir tu celda:** `INGRESOS_PARA_PROBAR` (60000, 15000 o 30000) y `resultado_agente`, llamando a `predecir_riesgo` con la edad del `perfil_usuario`.
**Prompt sugerido:**
> def predecir_riesgo ya definida. Defina INGRESOS_PARA_PROBAR = 60_000 y resultado_agente = predecir_riesgo(perfil_usuario["edad"], INGRESOS_PARA_PROBAR). Imprima el resultado.

### Sección 5 — Pandas
**Objetivo:** filtrar por salario y contar cuántos compraron.
**Qué debería producir tu celda:** `UMBRAL_SALARIO = 55_000`, `filtro` (subconjunto del DataFrame) y `cuantas_compraron` (entero).
**Prompt sugerido:**
> df ya definido (4 filas). Defina UMBRAL_SALARIO = 55_000, filtro = df[df['Salario'] > UMBRAL_SALARIO] y cuantas_compraron = int(filtro['Compro'].sum()). Muestre filtro e imprima cuántos compraron.

### Sección 6 — Visualización
**Objetivo:** interpretar el gráfico de salarios (no requiere código nuevo).
**Qué debería producir tu celda:** ejecutar la celda de gráfico pre-escrita y, en tu bitácora (`prompts_entregados.md`), explicar en 2 líneas por qué conviene validar visualmente antes de confiar en una métrica.
**Prompt sugerido:**
> No hay celda de código editable en esta sección. Observa el gráfico y explica en 2 líneas por qué conviene validar visualmente antes de una métrica.

## Validación

No hay autoevaluación automática (✅/❌). Compara tus resultados con los del notebook de referencia y valida con tu criterio — ejecuta cada celda y revisa que la salida tenga sentido antes de avanzar a la siguiente sección.

## Entrega

- Tu notebook ejecutado de punta a punta
- `prompts_entregados.md` completado

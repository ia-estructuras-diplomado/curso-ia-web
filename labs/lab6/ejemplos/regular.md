# Ejemplo `regular.edb`

Pórtico de concreto armado de 3 pisos, planta simétrica, sin vacíos y sin
muros. Ábrelo en ETABS (no pidas al agente que lo reconstruya). La ficha de
referencia de abajo es lo que `experto-modelo` tiene que leer del archivo.
Si ETABS dice otra cosa, manda ETABS.

## Geometría

| | |
|---|---|
| Pisos | Story1, Story2, Story3. Altura 3 m. Elevaciones 3, 6 y 9 m. |
| Planta | 2 vanos de 5 m en X y 2 vanos de 5 m en Y. Ejes en 0, 5 y 10 m. |
| Columnas | `COL40X40` (40×40 cm), las 9 por piso, asignadas a cada frame. |
| Vigas | `VIGA30X50` (peralte 50 cm, ancho 30 cm), en todas las líneas de grilla de cada piso. |
| Losas | 4 paños por piso, los 12 con `LOSA15` (0.15 m, Shell-Thin, C21). |
| Vacíos | Ninguno. |
| Muros | Ninguno. |
| Base | Empotrada en los 9 nudos de Z = 0. |
| Diafragmas | `D1`, `D2`, `D3`, rígidos, uno por piso, solo en las losas de ese nivel. |

Material `C21`: f'c = 21 MPa, peso específico 24 kN/m³. El módulo es el del
archivo, no un valor de la E.060 para citar.

El catálogo trae secciones del template (`Slab1`, `Plank1`, y perfiles de
acero) que **no** están asignadas. La ficha cuenta lo asignado.

## Cargas y peso sísmico

Unidades kN, m. La carga uniforme está solo en las losas, dirección Z
global, hacia abajo:

| Patrón | Tipo | Self-weight | Dónde | Valor |
|---|---|---|---|---|
| `PP` | Dead | 1 | peso propio de los elementos | — |
| `CM` | Super Dead | 0 | cada losa | −3.0 kN/m² |
| `CV` | Live | 0 | cada losa, incluida la azotea | −2.0 kN/m² |

El template también deja `Dead` (Dead, multiplicador 1) y `Live` (Live,
multiplicador 0). No están en el mass source.

Peso sísmico, `GetMassSource` opción **2** (solo cargas, sin masa de los
elementos):

| Patrón | Factor |
|---|---|
| PP | 1.0 |
| CM | 1.0 |
| CV | 0.25 |

`CV` al 0.25 es lo que tiene **este** archivo. No es, por sí solo, la cita
de la E.030. `Dead + Live` no es el peso sísmico.

## Análisis

Caso `Modal` (12 modos) ya corrido. No hay caso espectral ni otro caso de
derivas: la ficha tiene que decirlo, y nadie inventa esa tabla.

## Lectura geométrica

Planta simétrica: cuatro paños por piso, mismas secciones, sin muros. El
experto no escribe "regular E.030". Esa palabra la confirmas tú.

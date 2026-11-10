# Ejemplo `irregular.edb`

El mismo pórtico que `regular.edb`, con dos diferencias que el experto
tiene que ver en el archivo: un vacío de losa en un paño y un muro en un
solo eje. Cargas, material, secciones de frames y mass source son los del
ejemplo regular.

## Qué cambia respecto al regular

| | Regular | Este archivo |
|---|---|---|
| Losas por piso | 4 | 3 |
| Vacío | ninguno | paño X = 5–10 m, Y = 5–10 m, en Story1, Story2 y Story3 |
| Muro | ninguno | `MURO20`, 0.20 m, C21, sobre el eje X = 0, de Y = 0 a Y = 10, un área por piso |
| Diafragma | 4 losas | 3 losas. El vacío no lleva diafragma. |

Las vigas y las columnas del paño vacío **siguen**. El vacío es la losa
que no está, no un pórtico borrado. En ese paño no hay `CM` ni `CV`.

El muro está solo en X = 0. No hay otro en X = 10. La planta no se espeja.

## Lo que no cambia

- `COL40X40` y `VIGA30X50` asignadas a los frames. Base empotrada.
- `LOSA15` Shell-Thin en las losas que sí existen.
- `PP` × 1 + `CM` × 1 + `CV` × 0.25, mass source opción 2.
- `Dead` y `Live` del template existen y no entran al peso sísmico.
- Caso modal corrido. Sin caso de deriva.

## Lectura geométrica

El experto lista el vacío (coordenadas y pisos) y el muro (un solo eje).
No escribe "irregular E.030". Si alguien le dice que la estructura es
regular, la ficha alcanza para que el orquestador se detenga y pregunte.

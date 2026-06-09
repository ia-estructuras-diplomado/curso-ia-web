"""Prompts IA y celdas vacías para Lab 4 — importar desde _generar_notebooks.py."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from _ia_helpers import celda_solucion_alumno, ia_guia_seccion  # noqa: E402

IA_Q1 = ia_guia_seccion(
    "1",
    "Panorama CNN",
    "Listar los componentes clave de una CNN aplicada a inspección de grietas.",
    [
        "Definir `COMPONENTES_CNN` como lista con al menos 4 componentes",
        "Incluir convolución, pooling, activación y capa fully connected",
        "Imprimir la lista",
    ],
    vars_autoeval=["COMPONENTES_CNN"],
    consideraciones=[
        "Contexto: clasificación binaria de imágenes de hormigón (con/sin grieta)",
        "Nombres sugeridos: convolución, pooling, ReLU, flatten, fully connected, dropout",
    ],
    prompt="""Estoy en el Lab 4 (CNN para grietas en hormigón).
Genera código que:
1) defina COMPONENTES_CNN = ["convolución", "pooling", "ReLU", "flatten", "fully connected"]
2) imprima "Componentes CNN del laboratorio:"
3) recorra la lista e imprima cada componente con print(f"  · {c}")
No uses imports nuevos.""",
)

CELDA_Q1 = celda_solucion_alumno(
    variables=["COMPONENTES_CNN"],
    pasos=[
        "Lista con conv, pooling, activación, fc…",
        "Imprimir cada componente",
    ],
)

IA_Q2 = ia_guia_seccion(
    "2",
    "Exploración del dataset",
    "Configurar cuántas imágenes mostrar en un mosaico Positive vs Negative.",
    [
        "Definir `N_EJEMPLOS_MOSAICO` entre 2 y 8",
        "Mostrar mosaico con imágenes de train/Negative y train/Positive",
        "Usar `conteos` ya calculado en la celda anterior",
    ],
    vars_autoeval=["N_EJEMPLOS_MOSAICO", "conteos"],
    consideraciones=[
        "La celda anterior definió `RUTA_DATOS`, `conteos` y `class_names`",
        "Rutas: RUTA_DATOS / 'train' / 'Negative' y 'Positive'",
        "Usa matplotlib subplots; no redefinas conteos",
    ],
    prompt="""En Jupyter ya tengo:
- RUTA_DATOS = Path("data/cracks_subset")
- conteos = dict con train/val y Negative/Positive
Genera código que:
1) defina N_EJEMPLOS_MOSAICO = 4
2) cree fig, axes = plt.subplots(2, N_EJEMPLOS_MOSAICO, figsize=(2*N_EJEMPLOS_MOSAICO, 4))
3) para cada clase en ["Negative", "Positive"], tome N_EJEMPLOS_MOSAICO jpg de RUTA_DATOS/"train"/clase con sorted(glob)[:N]
4) muestre con imshow y título de clase
5) plt.tight_layout(); plt.show()
Importa Path de pathlib si hace falta.""",
)

CELDA_Q2 = celda_solucion_alumno(
    variables=["N_EJEMPLOS_MOSAICO"],
    pasos=[
        "Definir N_EJEMPLOS_MOSAICO (2–8)",
        "Mosaico 2 filas (Negative, Positive)",
    ],
)

IA_Q3 = ia_guia_seccion(
    "3",
    "Transformaciones y DataLoaders",
    "Definir tamaño de imagen, batch y crear train_loader y val_loader.",
    [
        "Definir `IMAGE_SIZE` (64–227) y `BATCH_SIZE` (8–64)",
        "Crear transforms con Resize, ToTensor y Normalize([0.5]*3, [0.5]*3)",
        "Crear `train_ds`, `val_ds` con ImageFolder y `train_loader`, `val_loader`",
    ],
    vars_autoeval=["IMAGE_SIZE", "BATCH_SIZE", "train_loader", "val_loader"],
    consideraciones=[
        "Usa RUTA_DATOS / 'train' y RUTA_DATOS / 'val'",
        "shuffle=True solo en train_loader",
        "device ya está definido en el setup",
    ],
    prompt="""En Jupyter tengo RUTA_DATOS, device y imports de torchvision.
Genera código que:
1) IMAGE_SIZE = 128; BATCH_SIZE = 32
2) transform = transforms.Compose([Resize((IMAGE_SIZE,IMAGE_SIZE)), ToTensor(), Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])])
3) train_ds = datasets.ImageFolder(RUTA_DATOS/"train", transform=transform)
4) val_ds = datasets.ImageFolder(RUTA_DATOS/"val", transform=transform)
5) class_names = train_ds.classes
6) train_loader = DataLoader(train_ds, batch_size=BATCH_SIZE, shuffle=True)
7) val_loader = DataLoader(val_ds, batch_size=BATCH_SIZE, shuffle=False)
8) imprima class_names y tamaños de train_ds y val_ds""",
)

CELDA_Q3 = celda_solucion_alumno(
    variables=["IMAGE_SIZE", "BATCH_SIZE", "train_loader", "val_loader"],
    pasos=[
        "IMAGE_SIZE y BATCH_SIZE",
        "ImageFolder + DataLoader train/val",
    ],
)

IA_Q4 = ia_guia_seccion(
    "4",
    "Arquitectura CNN",
    "Construir una CNN pequeña con dos bloques convolucionales y salida binaria.",
    [
        "Definir `N_FILTERS` (8–128) y `DROPOUT` (0–0.6)",
        "Crear `modelo` como nn.Module o Sequential con ≥2 Conv2d y salida 2 clases",
        "Mover modelo a `device`",
    ],
    vars_autoeval=["modelo", "N_FILTERS", "DROPOUT"],
    consideraciones=[
        "Entrada: 3 canales RGB; salida: 2 clases",
        "Tras conv+pool la imagen se reduce; usa AdaptiveAvgPool2d((4,4)) o calcula flatten",
        "Ejemplo: Conv→ReLU→MaxPool dos veces, luego Linear",
    ],
    prompt="""Lab 4 CNN grietas. Ya tengo IMAGE_SIZE, device, class_names.
Genera código PyTorch que:
1) N_FILTERS = 32; DROPOUT = 0.3
2) defina class CrackCNN(nn.Module) con:
   - Conv2d(3,N_FILTERS,3,padding=1), ReLU, MaxPool2d(2)
   - Conv2d(N_FILTERS,N_FILTERS*2,3,padding=1), ReLU, MaxPool2d(2)
   - AdaptiveAvgPool2d((4,4)), Flatten, Linear(N_FILTERS*2*16,64), ReLU, Dropout(DROPOUT), Linear(64,2)
3) modelo = CrackCNN().to(device)
4) imprima modelo""",
)

CELDA_Q4 = celda_solucion_alumno(
    variables=["modelo", "N_FILTERS", "DROPOUT"],
    pasos=[
        "N_FILTERS y DROPOUT",
        "CNN con ≥2 Conv2d y salida 2",
        "modelo.to(device)",
    ],
)

IA_Q5 = ia_guia_seccion(
    "5",
    "Entrenamiento",
    "Entrenar la CNN varias épocas y guardar métricas en `history`.",
    [
        "Definir `N_EPOCHS` (1–20) y `LEARNING_RATE` (1e-4–0.1)",
        "Usar `criterion = nn.CrossEntropyLoss()` y `optimizer = Adam(modelo.parameters(), lr=LEARNING_RATE)`",
        "Bucle de épocas llamando `train_one_epoch` y `eval_epoch` (ya definidas arriba)",
        "Guardar listas en `history` con keys train_loss, val_loss, train_acc, val_acc",
    ],
    vars_autoeval=["history", "N_EPOCHS", "LEARNING_RATE"],
    consideraciones=[
        "Las funciones train_one_epoch y eval_epoch ya están en la celda pre-escrita",
        "No reentrenes desde cero en la autoevaluación",
    ],
    prompt="""En Jupyter tengo modelo, train_loader, val_loader, device, train_one_epoch, eval_epoch.
Genera código que:
1) N_EPOCHS = 5; LEARNING_RATE = 1e-3
2) criterion = nn.CrossEntropyLoss(); optimizer = torch.optim.Adam(modelo.parameters(), lr=LEARNING_RATE)
3) history = {k: [] for k in ["train_loss","val_loss","train_acc","val_acc"]}
4) for epoch in range(N_EPOCHS): entrenar, evaluar, append a history, imprimir época y métricas
5) al final imprima "✅ Entrenamiento completado.""",
)

CELDA_Q5 = celda_solucion_alumno(
    variables=["history", "N_EPOCHS", "LEARNING_RATE"],
    pasos=[
        "N_EPOCHS y LEARNING_RATE",
        "Bucle de entrenamiento + history",
    ],
)

IA_Q6 = ia_guia_seccion(
    "6",
    "Curvas de entrenamiento",
    "Graficar pérdida y accuracy de train vs validación.",
    [
        "Gráfico con 2 subplots: loss y accuracy",
        "Eje x = épocas (1..N_EPOCHS)",
        "Leyenda train vs val",
    ],
    vars_autoeval=["history", "N_EPOCHS"],
    consideraciones=[
        "Usa history y N_EPOCHS de la sección anterior",
        "No reentrenes el modelo aquí",
    ],
    prompt="""Tengo history (train_loss, val_loss, train_acc, val_acc) y N_EPOCHS.
Genera matplotlib con:
- fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
- ax1: plot loss train y val vs range(1, N_EPOCHS+1)
- ax2: plot acc train y val
- leyendas, títulos, plt.tight_layout(), plt.show()""",
)

CELDA_Q6 = celda_solucion_alumno(
    variables=["history", "N_EPOCHS"],
    pasos=["Subplots loss y accuracy", "Leyenda train/val"],
)

IA_Q7 = ia_guia_seccion(
    "7",
    "Métricas en validación",
    "Matriz de confusión y classification_report sobre el conjunto val.",
    [
        "Obtener `y_true` e `y_pred` en val (usa modelo en eval mode)",
        "Calcular `acc_val` con accuracy_score",
        "Mostrar `cm` con confusion_matrix y heatmap seaborn",
        "Imprimir classification_report con target_names=class_names",
    ],
    vars_autoeval=["acc_val", "cm"],
    consideraciones=[
        "Puedes reutilizar eval_epoch o iterar val_loader manualmente",
        "class_names viene de ImageFolder (Negative, Positive)",
    ],
    prompt="""Tengo modelo, val_loader, device, class_names.
Genera código que:
1) ponga modelo.eval(); recolecte y_true, y_pred en val_loader (sin grad)
2) acc_val = accuracy_score(y_true, y_pred)
3) cm = confusion_matrix(y_true, y_pred)
4) heatmap seaborn de cm con annot=True
5) print(classification_report(y_true, y_pred, target_names=class_names))
6) print(f"Accuracy validación: {acc_val:.3f}")""",
)

CELDA_Q7 = celda_solucion_alumno(
    variables=["acc_val", "cm"],
    pasos=[
        "y_true, y_pred en val",
        "acc_val, cm y gráficos",
    ],
)

IA_Q8 = ia_guia_seccion(
    "8",
    "Casos locales",
    "Mostrar predicciones sobre imágenes concretas de validación.",
    [
        "Definir `N_CASOS_MOSTRADOS` ≥ 1",
        "Elegir imágenes de val_ds o val_loader",
        "Mostrar imagen, etiqueta real y predicción (class_names)",
    ],
    vars_autoeval=["N_CASOS_MOSTRADOS"],
    consideraciones=[
        "Desnormaliza imagen para imshow: img * 0.5 + 0.5",
        "Usa modelo.eval() y softmax o argmax",
    ],
    prompt="""Tengo val_ds, class_names, modelo, device.
Genera código que:
1) N_CASOS_MOSTRADOS = 3
2) modelo.eval()
3) para i in range(N_CASOS_MOSTRADOS): tomar val_ds[i], predecir, mostrar imshow con título "real: X | pred: Y"
4) plt.show()""",
)

CELDA_Q8 = celda_solucion_alumno(
    variables=["N_CASOS_MOSTRADOS"],
    pasos=[
        "N_CASOS_MOSTRADOS ≥ 1",
        "imshow con etiqueta real vs predicha",
    ],
)

IA_Q9 = ia_guia_seccion(
    "9",
    "Reflexión ingeniería",
    "Responder brevemente cuándo usar CNN en obra y sus límites.",
    [
        "Escribir 2–3 líneas en markdown o comentarios",
        "Mencionar inspección visual, falsos positivos y validación humana",
    ],
    vars_autoeval=[],
    consideraciones=[
        "No hace falta código Python; respuesta textual opcional",
        "La autoevaluación de esta sección es solo lectura",
    ],
    prompt="""No generes código. Dame 3 bullets breves en español para un ingeniero civil:
- Cuándo una CNN de grietas aporta valor en obra
- Un riesgo (falsos positivos/negativos)
- Qué validación humana harías antes de confiar en la alerta""",
    nota_asistente=False,
)

CELDA_Q9 = celda_solucion_alumno(
    variables=[],
    pasos=["Respuesta breve opcional (markdown en celda anterior)"],
    nota="La sección 9 no tiene autoevaluación con código.",
)

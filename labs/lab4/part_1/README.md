# Lab 4 Parte 1 — CNN para grietas en hormigón

**Sesión 7** · Clasificación de imágenes con redes convolucionales aplicadas a inspección estructural.

## Objetivo de aprendizaje

Entrenar una **CNN binaria** (PyTorch) que clasifique fotos de superficie de hormigón como con grieta o
sin grieta, y entender qué evidencia (Grad-CAM) necesitarías antes de confiar en esa alerta en un
flujo real de inspección.

## Contexto de ingeniería

Un ingeniero que revisa manualmente miles de fotos de dron o cámaras fijas de una obra no puede mirar
todas con el mismo nivel de detalle. Un clasificador de este tipo sirve para **triaje**: priorizar qué
fotos revisar primero, no para reemplazar el criterio de un perito estructural.

## Datos

Dataset [Concrete Crack Images for Classification](https://data.mendeley.com/datasets/5y9wdsg2zt/1)
(METU, CC BY 4.0), subconjunto de 2 000 imágenes (800 train + 200 val por clase). Ver
[`data/DATOS.md`](data/DATOS.md).

| Clase | Significado |
|-------|-------------|
| **Negative** | Hormigón sin grieta visible |
| **Positive** | Hormigón con grieta |

## Entorno

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/lab4/part_1
jupyter notebook cnn_grietas_estructuras.ipynb
```

## Notebook de referencia

[`cnn_grietas_estructuras.ipynb`](cnn_grietas_estructuras.ipynb) es un notebook completo y ejecutable
de punta a punta: EDA → augmentation → arquitectura → entrenamiento → métricas → **Grad-CAM**
(explicabilidad visual sobre qué región de la imagen usó la CNN para decidir). Ábrelo, ejecútalo
(*Run All*) para ver el resultado esperado, y luego construye tu propio notebook guiándote por las
secciones siguientes y por tu asistente de IA.

## Secciones y prompts sugeridos

### 1 — Panorama CNN en inspección estructural
**Objetivo:** listar los componentes clave de una CNN aplicada a clasificación de grietas.
**Qué debería producir tu celda:** una lista `COMPONENTES_CNN` con al menos 4 componentes (convolución,
pooling, activación, capa fully connected), impresa elemento por elemento.
**Prompt sugerido:**
> Estoy en el Lab 4 (CNN para grietas en hormigón). Genera código que: 1) defina COMPONENTES_CNN =
> ["convolución", "pooling", "ReLU", "flatten", "fully connected"] 2) imprima "Componentes CNN del
> laboratorio:" 3) recorra la lista e imprima cada componente con print(f"  · {c}") No uses imports
> nuevos.

### 2 — EDA del dataset
**Objetivo:** explorar balance de clases, tamaños de imagen y un mosaico Positive vs Negative.
**Qué debería producir tu celda:** `N_EJEMPLOS_MOSAICO` (2–8) y `N_MUESTRAS_EDA` (20–200); un gráfico de
barras con conteos train/val por clase; un histograma de anchos y altos de una muestra de imágenes; un
mosaico 2×N con ejemplos de cada clase.
**Prompt sugerido:**
> En Jupyter ya tengo RUTA_DATOS, conteos, class_names y PIL Image. Genera código que: 1)
> N_EJEMPLOS_MOSAICO = 4; N_MUESTRAS_EDA = 100 2) bar chart: eje x Negative/Positive, barras train y val
> con conteos[split][cls] 3) tome N_MUESTRAS_EDA jpg de train (mezcla clases), lea width/height con
> Image.open 4) histograma anchos y altos (subplots o dos hist) 5) mosaico 2 filas x N_EJEMPLOS_MOSAICO
> con imshow 6) plt.tight_layout(); plt.show()

### 3 — Transformaciones y data augmentation
**Objetivo:** definir transforms de train (con augmentation) y val (sin aleatoriedad), y visualizarlos.
**Qué debería producir tu celda:** `IMAGE_SIZE` (64–227) y `AUG_ROTATION` (5–45); `train_transform` con
flip/rotación/color; `val_transform` solo con resize/normalize; una imagen original junto a varias
versiones aumentadas.
**Prompt sugerido:**
> Lab 4 CNN. Tengo RUTA_DATOS, transforms, Resize, ToTensor, Normalize, RandomHorizontalFlip,
> RandomRotation, ColorJitter. Genera código que: 1) IMAGE_SIZE = 128; AUG_ROTATION = 15;
> N_AUG_MOSTRADOS = 4 2) train_transform = Compose([RandomHorizontalFlip(), RandomRotation(AUG_ROTATION),
> ColorJitter(0.2,0.2), Resize((IMAGE_SIZE,IMAGE_SIZE)), ToTensor(), Normalize([0.5,0.5,0.5],
> [0.5,0.5,0.5])]) 3) val_transform = Compose([Resize((IMAGE_SIZE,IMAGE_SIZE)), ToTensor(),
> Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])]) 4) tome una imagen Positive de train, muestre original +
> N_AUG_MOSTRADOS aplicando train_transform en loop 5) títulos 'original' y 'aug i'

### 4 — DataLoaders
**Objetivo:** crear `train_loader` y `val_loader` con los transforms de la sección anterior.
**Qué debería producir tu celda:** `BATCH_SIZE` (8–64); `train_ds`/`val_ds` con `ImageFolder`;
`train_loader` (shuffle=True) y `val_loader` (shuffle=False).
**Prompt sugerido:**
> En Jupyter tengo RUTA_DATOS, train_transform, val_transform, device. Genera código que: 1) BATCH_SIZE
> = 32 2) train_ds = ImageFolder(RUTA_DATOS/"train", transform=train_transform) 3) val_ds =
> ImageFolder(RUTA_DATOS/"val", transform=val_transform) 4) class_names = train_ds.classes 5)
> train_loader y val_loader con batch_size=BATCH_SIZE 6) imprima class_names y len(train_ds), len(val_ds)

### 5 — Arquitectura CNN
**Objetivo:** construir una CNN pequeña con dos bloques convolucionales y salida binaria.
**Qué debería producir tu celda:** `N_FILTERS` (8–128) y `DROPOUT` (0–0.6); un `modelo` con ≥2 `Conv2d` y
salida de 2 clases, movido a `device`.
**Prompt sugerido:**
> Lab 4 CNN grietas. Ya tengo IMAGE_SIZE, device, class_names. Genera código PyTorch que: 1) N_FILTERS =
> 32; DROPOUT = 0.3 2) defina class CrackCNN(nn.Module) con: Conv2d(3,N_FILTERS,3,padding=1), ReLU,
> MaxPool2d(2); Conv2d(N_FILTERS,N_FILTERS*2,3,padding=1), ReLU, MaxPool2d(2); AdaptiveAvgPool2d((4,4)),
> Flatten, Linear(N_FILTERS*2*16,64), ReLU, Dropout(DROPOUT), Linear(64,2) 3) modelo =
> CrackCNN().to(device) 4) imprima modelo

### 6 — Entrenamiento
**Objetivo:** entrenar la CNN varias épocas y guardar métricas en `history`.
**Qué debería producir tu celda:** `N_EPOCHS` (1–20) y `LEARNING_RATE` (1e-4–0.1); `criterion`/`optimizer`;
un bucle de épocas que llena `history` con `train_loss`, `val_loss`, `train_acc`, `val_acc`.
**Prompt sugerido:**
> En Jupyter tengo modelo, train_loader, val_loader, device, train_one_epoch, eval_epoch. Genera código
> que: 1) N_EPOCHS = 5; LEARNING_RATE = 1e-3 2) criterion = nn.CrossEntropyLoss(); optimizer =
> torch.optim.Adam(modelo.parameters(), lr=LEARNING_RATE) 3) history = {k: [] for k in
> ["train_loss","val_loss","train_acc","val_acc"]} 4) for epoch in range(N_EPOCHS): entrenar, evaluar,
> append a history, imprimir época y métricas 5) al final imprima "✅ Entrenamiento completado."

### 7 — Curvas de entrenamiento
**Objetivo:** graficar pérdida y accuracy de train vs validación.
**Qué debería producir tu celda:** una figura con 2 subplots (loss, accuracy) contra las épocas, con
leyenda train/val.
**Prompt sugerido:**
> Tengo history (train_loss, val_loss, train_acc, val_acc) y N_EPOCHS. Genera matplotlib con: fig,
> (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4)); ax1: plot loss train y val vs range(1, N_EPOCHS+1);
> ax2: plot acc train y val; leyendas, títulos, plt.tight_layout(), plt.show()

### 8 — Métricas en validación
**Objetivo:** matriz de confusión y `classification_report` sobre el conjunto val.
**Qué debería producir tu celda:** `y_true`/`y_pred` recolectados en modo eval; `acc_val`; `cm` con
heatmap; el reporte de clasificación con `target_names=class_names`.
**Prompt sugerido:**
> Tengo modelo, val_loader, device, class_names. Genera código que: 1) ponga modelo.eval(); recolecte
> y_true, y_pred en val_loader (sin grad) 2) acc_val = accuracy_score(y_true, y_pred) 3) cm =
> confusion_matrix(y_true, y_pred) 4) heatmap seaborn de cm con annot=True 5)
> print(classification_report(y_true, y_pred, target_names=class_names)) 6) print(f"Accuracy validación:
> {acc_val:.3f}")

### 9 — Casos locales
**Objetivo:** mostrar predicciones sobre imágenes concretas de validación.
**Qué debería producir tu celda:** `N_CASOS_MOSTRADOS` ≥ 1 imágenes de `val_ds`, con su etiqueta real y
la predicción del modelo.
**Prompt sugerido:**
> Tengo val_ds, class_names, modelo, device. Genera código que: 1) N_CASOS_MOSTRADOS = 3 2)
> modelo.eval() 3) para i in range(N_CASOS_MOSTRADOS): tomar val_ds[i], predecir, mostrar imshow con
> título "real: X | pred: Y" 4) plt.show()

### 10 — Grad-CAM (explicabilidad)
**Objetivo:** ver qué región de la imagen impulsó cada predicción, para poder confiar (o desconfiar) en
una alerta automática de grieta.
**Qué debería producir tu celda:** un mapa de calor superpuesto sobre 4–6 imágenes de validación
(incluyendo, si existe, algún caso mal clasificado), calculado a partir del gradiente de la clase
predicha respecto a la última capa convolucional.
**Prompt sugerido:**
> Tengo un modelo CNN de PyTorch (CrackCNN) con dos bloques Conv2d en self.features, entrenado para
> clasificar grietas. Genera código de Grad-CAM que: 1) registre hooks forward/backward sobre la última
> capa Conv2d de self.features 2) calcule el mapa de calor como ReLU del producto entre gradientes
> promediados por canal y las activaciones 3) lo redimensione al tamaño de la imagen de entrada 4)
> lo superponga con imshow(cmap='jet', alpha=0.45) sobre 4-6 imágenes de validación, priorizando al
> menos un caso mal clasificado si existe.

## Validación

No hay autoevaluación automática (✅/❌). Compara tus gráficos, tu matriz de confusión y tu mapa de
Grad-CAM con los del notebook de referencia, y valida con tu criterio de ingeniero — "la IA propone, el
ingeniero valida visualmente."

## Entrega

- Tu notebook ejecutado de punta a punta
- `prompts_entregados.md` completado

**Parte 2 (LSTM):** [`../part_2/README.md`](../part_2/README.md)

# Lab 3 — Inteligencia Artificial Explicable (xAI)

**Sesión 6** · Interpretar y auditar predicciones de modelos ML en contexto de ingeniería estructural.

## Objetivo de aprendizaje

Entrenar un **XGBoost** multiclass sobre sensores de monitoreo de salud estructural (SHM) y aplicar un **kit completo de técnicas xAI** sobre ese mismo modelo — importancia del booster, permutation importance, **SHAP** (global y local), **LIME** y **PDP** — para poder explicar y auditar una predicción antes de confiar en ella para una alerta de daño.

## Contexto de ingeniería

Un modelo puede acertar por **sensores correctos** (deformación, vibración) o por **artefactos** de los datos. Antes de activar una alerta de daño estructural, el ingeniero necesita **trazabilidad**: qué sensor empujó la predicción y si eso es físicamente coherente. xAI **apoya** la validación humana; no sustituye normativa ni inspección.

## Datos

Mismo dataset que el Lab 1 (sensores SHM). Ver [`data/DATOS.md`](data/DATOS.md).

## Entorno

```bash
bash labs/setup.sh
source labs/.venv/bin/activate
cd labs/lab3
jupyter notebook xai_estructuras.ipynb
```

Dependencias: `xgboost`, `shap`, `lime` en [`labs/requirements.txt`](../requirements.txt).

## Notebook de referencia

`xai_estructuras.ipynb` es un notebook completo y ejecutable de punta a punta: carga y limpieza → balance de clases → entrenamiento del XGBoost → métricas → explicación global (importancia, permutation) → explicación local de un caso con SHAP y LIME comparadas → PDP y SHAP dependence. Ábrelo, ejecútalo (Run All) para ver el resultado esperado, y luego construye tu propio notebook guiándote por las secciones siguientes y por tu asistente de IA.

## Secciones y prompts sugeridos

### 1. Panorama xAI
**Objetivo:** listar las técnicas de explicación que aplicarás en el lab (kit completo, no solo una).
**Qué debería producir tu celda:** una lista con al menos 4 técnicas (importancia, shap, lime, pdp), impresa una por línea.
> Estoy en el Lab 3 de xAI con XGBoost y sensores SHM.
> Genera código que:
> 1) defina TECNICAS_XAI = ["importancia", "permutation", "shap", "lime", "pdp"]
> 2) imprima "Técnicas xAI que aplicarás en este lab:"
> 3) recorra la lista e imprima cada técnica con print(f"  · {t}")
> No uses imports nuevos.

### 2. Carga del dataset
**Objetivo:** definir las 5 features de sensor y mostrar las primeras filas del CSV.
**Qué debería producir tu celda:** una lista `FEATURES` con los 5 nombres exactos de columnas (sin `Timestamp` ni `Condition Label`), y `df.head()` mostrado con `display()`.
> En Jupyter ya tengo `df` cargado (1000 filas, 7 columnas) del CSV de monitoreo estructural.
> Genera código que:
> 1) defina FEATURES como lista con las 5 columnas de sensores (sin Timestamp ni Condition Label)
> 2) defina N_FILAS_HEAD = 5
> 3) imprima FEATURES
> 4) muestre df.head(N_FILAS_HEAD) con display()
> Usa los nombres de columna exactos del dataset.

### 3. Limpieza y revisión de sensor
**Objetivo:** elegir un sensor y mostrar sus estadísticas en datos crudos (antes de limpiar).
**Qué debería producir tu celda:** `.describe()` de un sensor válido sobre `df` (crudo), no sobre `df_limpio`.
> En Jupyter tengo `df` (crudo) y `df_limpio` (sin nulos en FEATURES).
> Genera código que:
> 1) defina COLUMNA_REVISAR = "Strain (με)"
> 2) calcule stats_col = df[COLUMNA_REVISAR].describe()
> 3) imprima el nombre de la columna y muestre stats_col con display()

### 4. Balance de clases
**Objetivo:** mostrar el conteo de las clases de `Condition Label`.
**Qué debería producir tu celda:** una serie con las clases ordenadas, usando el diccionario `conteo` ya calculado en la celda anterior.
> En Jupyter ya existe conteo = dict con value_counts de Condition Label.
> Genera código que:
> 1) defina N_CLASES_MOSTRAR = 3
> 2) cree serie_clases = pd.Series(conteo).sort_index().head(N_CLASES_MOSTRAR)
> 3) imprima cuántas clases muestra y display(serie_clases)

### 5. Entrenar XGBoost
**Objetivo:** configurar hiperparámetros y entrenar el clasificador multiclass.
**Qué debería producir tu celda:** un `XGBClassifier` entrenado con `objective='multi:softprob'` y `num_class=3`, con hiperparámetros en rangos razonables (n_estimators 10–500, max_depth 2–12, learning_rate 0.01–0.5).
> En Jupyter tengo X_train, X_test, y_train, y_test (datos escalados, stratify) y RANDOM_STATE=42.
> Genera código que:
> 1) defina N_ESTIMATORS=100, MAX_DEPTH=6, LEARNING_RATE=0.1
> 2) cree modelo = XGBClassifier(objective='multi:softprob', num_class=3, n_estimators=..., max_depth=..., learning_rate=..., random_state=RANDOM_STATE, eval_metric='mlogloss')
> 3) entrene con modelo.fit(X_train, y_train)
> 4) imprima confirmación de entrenamiento

### 6. Métricas de clasificación
**Objetivo:** matriz de confusión y `classification_report`.
**Qué debería producir tu celda:** un heatmap 3×3 con ejes Real/Predicho y el reporte de clasificación impreso.
> En Jupyter tengo y_test, y_pred (predicciones del XGBoost en test).
> Genera código que:
> 1) calcule cm = confusion_matrix(y_test, y_pred, labels=[0, 1, 2])
> 2) dibuje heatmap con sns.heatmap (annot=True, ejes Real/Predicho)
> 3) imprima classification_report(y_test, y_pred, digits=3)
> Incluye plt.show().

### 7. xAI global — importancia del booster
**Objetivo:** identificar el top-3 de features por importancia del booster (la celda pre-escrita ya muestra permutation importance).
**Qué debería producir tu celda:** una lista `TOP3_IMPORTANCIA` con los 3 sensores más importantes — se espera que `Strain (με)` esté entre ellos.
> En Jupyter tengo modelo (XGBoost entrenado) y FEATURES (lista de 5 sensores).
> Genera código que:
> 1) ordene importancias en una Series indexada por FEATURES
> 2) defina TOP3_IMPORTANCIA = lista con los 3 nombres más importantes
> 3) imprima TOP3_IMPORTANCIA

### 8. SHAP global
**Objetivo:** summary plot de SHAP para una clase de daño.
**Qué debería producir tu celda:** un summary plot de SHAP para `CLASE_SHAP = 2` (daño severo), usando la función `shap_values_clase()` ya definida.
> En Jupyter tengo modelo, X_test, FEATURES, shap_values y la función:
>
> def shap_values_clase(shap_values, clase):
>     if isinstance(shap_values, list):
>         return shap_values[clase]
>     return shap_values[:, :, clase]
>
> Genera código que:
> 1) defina CLASE_SHAP = 2
> 2) cree figura plt.figure(figsize=(8, 5))
> 3) llame shap.summary_plot(shap_values_clase(shap_values, CLASE_SHAP), X_test, feature_names=FEATURES, show=False)
> 4) ponga título con la clase y plt.show()

### 9. SHAP local (waterfall)
**Objetivo:** explicar una predicción individual del conjunto de test.
**Qué debería producir tu celda:** un waterfall de SHAP para un caso concreto, mostrando también la etiqueta real y predicha de ese caso.
> En Jupyter tengo X_test, y_test, y_pred, shap_values, explainer, FEATURES, CLASE_SHAP
> y la función etiqueta_en_test(idx) que devuelve (y_true, y_pred).
>
> También existe shap_values_clase(shap_values, clase).
>
> Genera código que:
> 1) defina INDEX_CASO = 0
> 2) obtenga y_true_caso, y_pred_caso = etiqueta_en_test(INDEX_CASO) e imprima ambos
> 3) tome sv = shap_values_clase(shap_values, CLASE_SHAP)[INDEX_CASO]
> 4) base = explainer.expected_value; si es lista o ndarray, base = base[CLASE_SHAP]
> 5) cree exp = shap.Explanation(values=sv, base_values=base, data=X_test[INDEX_CASO], feature_names=FEATURES)
> 6) llame shap.plots.waterfall(exp, max_display=6, show=False) y plt.show()
>
> Prueba también INDEX_CASO=5 si quieres otro caso; imprime si acertó o no antes del gráfico.

### 10. LIME local
**Objetivo:** explicar el mismo caso de test con LIME y comparar con SHAP (sección 9).
**Qué debería producir tu celda:** un gráfico LIME para el mismo `INDEX_CASO` y `CLASE_SHAP`, y una lista `TOP_LIME_FEATURES` con 3 nombres de sensor.
> En Jupyter tengo explainer_lime, modelo, X_test, INDEX_CASO, CLASE_SHAP, FEATURES.
> Genera código que:
> 1) exp_lime = explainer_lime.explain_instance(X_test[INDEX_CASO], modelo.predict_proba, num_features=5, labels=(CLASE_SHAP,))
> 2) fig = exp_lime.as_pyplot_figure(label=CLASE_SHAP); plt.title(...); plt.show()
> 3) TOP_LIME_FEATURES = [next((f for f in FEATURES if feat.startswith(f)), feat.split('<=')[0].strip()) for feat, _ in exp_lime.as_list(label=CLASE_SHAP)[:3]]
> 4) print(TOP_LIME_FEATURES)
> Nota: LIME devuelve umbrales (ej. "Strain (με) <= -0.68"); normaliza al nombre del sensor.

### 11. PDP y SHAP dependence
**Objetivo:** partial dependence y dependence plot para una feature adicional (la celda pre-escrita ya muestra el PDP de `Strain`).
**Qué debería producir tu celda:** un PDP y un SHAP dependence plot para otra feature (por ejemplo `Temp (°C)`), recordando pasar `target=CLASE_SHAP` porque el modelo es multiclass.
> En Jupyter tengo modelo, X_test, FEATURES, shap_values, CLASE_SHAP
> y shap_values_clase(shap_values, clase).
>
> Genera código que:
> 1) defina FEATURE_PDP = "Temp (°C)"
> 2) idx_pdp = FEATURES.index(FEATURE_PDP)
> 3) PDP: PartialDependenceDisplay.from_estimator(modelo, X_test, [idx_pdp], feature_names=FEATURES, target=CLASE_SHAP, ax=ax) con título
> 4) dependence: shap.dependence_plot(idx_pdp, shap_values_clase(shap_values, CLASE_SHAP), X_test, feature_names=FEATURES, show=False)
> Incluye plt.show() en cada gráfico.

## Validación

No hay autoevaluación automática (✅/❌). Compara tus gráficos y métricas con los del notebook de referencia y valida con tu criterio de ingeniero — "la IA propone, el ingeniero valida visualmente."

## Entrega

- Tu notebook ejecutado de punta a punta
- `prompts_entregados.md` completado

"""Prompts IA para Lab 1 — importar desde _generar_notebooks.py."""
from __future__ import annotations

from _ia_helpers import ia_guia_seccion

IA_Q1 = ia_guia_seccion(
    "1", "Contexto PCA",
    "Confirmar que el método de reducción es PCA.",
    ["METODO_REDUCCION = 'pca'", "print del método", "✅ autoevaluación 1"],
    """Lab SHM (sensores estructura). Celda ### PEGA AQUÍ ###:
METODO_REDUCCION = "pca"
print(f"Método elegido: {METODO_REDUCCION}")""",
)

IA_Q2 = ia_guia_seccion(
    "2", "Carga",
    "Definir 5 features de sensor y mostrar head del CSV.",
    ["FEATURES con 5 nombres exactos del CSV", "N_FILAS_HEAD 1-20", "display head"],
    """df ya cargado desde data/building_health_monitoring_dataset.csv (1000×7).
Columnas sensor exactas: "Accel_X (m/s^2)", "Accel_Y (m/s^2)", "Accel_Z (m/s^2)", "Strain (με)", "Temp (°C)"
Celda ### PEGA AQUÍ ###: lista FEATURES (5), N_FILAS_HEAD=5, print y display(df.head)""",
)

IA_Q3 = ia_guia_seccion(
    "3", "Calidad",
    "Revisar estadísticas de un sensor en datos crudos.",
    ["COLUMNA_REVISAR válida", "describe y display"],
    """df y df_limpio ya creados arriba. ### PEGA AQUÍ ###:
COLUMNA_REVISAR = "Strain (με)"
stats_col = df[COLUMNA_REVISAR].describe()
print y display""",
)

IA_Q4 = ia_guia_seccion(
    "4", "Describe",
    "Resumen y dispersión relativa de sensores en df_limpio.",
    ["COLUMNAS_RESUMEN con ≥2 columnas válidas", "describe y std/|media|"],
    """Usar df_limpio. ### PEGA AQUÍ ###:
COLUMNAS_RESUMEN = ["Strain (με)", "Temp (°C)", "Accel_Z (m/s^2)"]
resumen = df_limpio[COLUMNAS_RESUMEN].describe(); display(resumen)
medias_abs y dispersion = std/medias_abs; display(dispersion)""",
)

IA_Q5 = ia_guia_seccion(
    "5", "Etiquetas",
    "Mostrar conteo de Condition Label.",
    ["N_CLASES_MOSTRAR=3", "usar dict conteo ya calculado"],
    """conteo ya existe (df_limpio Condition Label). ### PEGA AQUÍ ###:
N_CLASES_MOSTRAR = 3
serie_clases = pd.Series(conteo).sort_index().head(N_CLASES_MOSTRAR)
print y display""",
)

IA_Q6 = ia_guia_seccion(
    "6", "Correlación",
    "Top correlaciones entre features en df_limpio.",
    ["TOP_N_CORR=3", "matriz solo FEATURES"],
    """df_limpio y FEATURES definidos. ### PEGA AQUÍ ###:
TOP_N_CORR = 3
corr = df_limpio[FEATURES].corr()
# imprimir pares con mayor |r| (sin diagonal)""",
)

IA_Q7 = ia_guia_seccion(
    "7", "Escalado",
    "StandardScaler sobre X_features.",
    ["X_features desde df_limpio[FEATURES]", "X_scaled con scaler.fit_transform"],
    """### PEGA AQUÍ ###:
X_features = df_limpio[FEATURES].values
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_features)
print shape X_scaled""",
)

IA_Q8 = ia_guia_seccion(
    "8", "Varianza PCA",
    "Varianza explicada y N_COMPONENTES.",
    ["PCA con n_components=N_COMPONENTES (3-5)", "var_acum lista"],
    """X_scaled listo. ### PEGA AQUÍ ###:
N_COMPONENTES = 3
pca = PCA(n_components=N_COMPONENTES)
X_pca = pca.fit_transform(X_scaled)
var_acum = pca.explained_variance_ratio_.cumsum().tolist()
print varianza por componente""",
)

IA_Q9 = ia_guia_seccion(
    "9", "Proyección 2D",
    "Scatter PC1 vs PC2 coloreado por Condition Label.",
    ["N_COMPONENTES_2D=2", "gráfico con leyenda de estados"],
    """X_pca y df_limpio disponibles. ### PEGA AQUÍ ###:
N_COMPONENTES_2D = 2
# scatter X_pca[:,0] vs X_pca[:,1], c=df_limpio['Condition Label']""",
)

IA_Q10 = ia_guia_seccion(
    "10", "KMeans",
    "Método del codo y KMeans con K_OPT.",
    ["K_MIN,K_MAX,K_OPT", "silhouette sil_km", "gráfico codo + scatter clústeres"],
    """X_pca_input = X_scaled (o X_pca según celda previa). ### PEGA AQUÍ ###:
K_MIN=2, K_MAX=8, K_OPT=3
# bucle inercias, KMeans, silhouette, plots""",
    prompt_alt="K_OPT=4 si el codo lo sugiere; sil_km debe calcularse.",
)

IA_Q11 = ia_guia_seccion(
    "11", "DBSCAN",
    "Clustering por densidad con eps y min_samples.",
    ["EPS=0.7, MIN_SAMPLES=8", "n_clusters_db, n_noise_db, sil_db", "scatter"],
    """X_pca_input disponible. ### PEGA AQUÍ ###:
EPS=0.7, MIN_SAMPLES=8
dbscan fit_predict, contar clústeres y ruido (-1), silhouette sin ruido, plot""",
)

IA_Q12 = ia_guia_seccion(
    "12", "Comparativa",
    "ARI entre clústeres y Condition Label.",
    ["labels_km y labels_db del notebook", "ari_km, ari_db"],
    """### PEGA AQUÍ ###:
y_true = df_limpio['Condition Label'].values
ari_km = adjusted_rand_score(y_true, labels_km)
ari_db = adjusted_rand_score(y_true, labels_db)
print ambos ARI""",
)

IA_Q13 = ia_guia_seccion(
    "13", "Clasificación + loadings",
    "Random Forest en PCA y top loading PC1.",
    ["N_PCA_CLF=3", "accuracy", "top feature en loadings PC1"],
    """Train/test y PCA ya hechos. ### PEGA AQUÍ ###:
N_PCA_CLF = 3
# clasificador RF en componentes, accuracy, loadings PC1 → nombre sensor top""",
)

IA_ALL = [
    IA_Q1, IA_Q2, IA_Q3, IA_Q4, IA_Q5, IA_Q6, IA_Q7, IA_Q8, IA_Q9,
    IA_Q10, IA_Q11, IA_Q12, IA_Q13,
]

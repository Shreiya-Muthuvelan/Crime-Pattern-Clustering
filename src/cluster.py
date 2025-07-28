from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def reduce_dimensions(df, n_components=2):
    pca = PCA(n_components=n_components)
    return pca.fit_transform(df)

def find_optimal_k(df, max_k=10):
    inertia = []
    for k in range(1, max_k + 1):
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(df)
        inertia.append(kmeans.inertia_)
    return inertia

def apply_kmeans(df, k=3):
    kmeans = KMeans(n_clusters=k, random_state=42)
    clusters = kmeans.fit_predict(df)
    return clusters

# Metrics Evaluation K-Means

def calculate_wcss(data, labels, centroids):
    """
    Fungsi untuk menghitung Within-Cluster Sum of Square (WCSS) / Inertia.
    WCSS adalah total jarak kuadrat antara setiap titik data dengan centroid di clusternya.
    Makin kecil WCSS, makin padat cluster tersebut.
    """
    wcss = 0.0
    for i in range(len(data)):
        cluster_idx = labels[i]
        centroid = centroids[cluster_idx]
        
        # Hitung jarak kuadrat
        dist_sq = (data[i][0] - centroid[0])**2 + (data[i][1] - centroid[1])**2
        wcss += dist_sq
        
    return wcss

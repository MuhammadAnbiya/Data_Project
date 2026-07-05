# Utility Visualisasi untuk K-Means
import matplotlib.pyplot as plt

def plot_clusters(data, labels, centroids):
    """
    Fungsi bantuan untuk memvisualisasikan hasil clustering.
    data: list of [x, y]
    labels: list of cluster index (0, 1, 2, dll)
    centroids: list of [x, y] untuk centroid
    """
    x = [d[0] for d in data]
    y = [d[1] for d in data]
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, c=labels, cmap='viridis', alpha=0.6, s=100)
    
    # Plot Centroids
    cx = [c[0] for c in centroids]
    cy = [c[1] for c in centroids]
    plt.scatter(cx, cy, c='red', marker='X', s=200, label='Centroids')
    
    plt.title('Hasil Visualisasi K-Means Clustering')
    plt.xlabel('Fitur 1 (Age)')
    plt.ylabel('Fitur 2 (Spending Score)')
    plt.legend()
    plt.grid(True)
    plt.savefig('kmeans_result.png')
    print("Visualisasi berhasil disimpan sebagai 'kmeans_result.png'")

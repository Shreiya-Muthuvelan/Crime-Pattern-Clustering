
import os
import webbrowser
from src.preprocess import load_and_clean_data, encode_features, select_features
from src.cluster import reduce_dimensions, find_optimal_k, apply_kmeans
from src.visualize import plot_elbow, plot_clusters, plot_cluster_distribution,crime_hotspot_detection,risk_score_by_area,cluster_summary
def main():
    df = load_and_clean_data('data/crime_in_la.csv')
    df = encode_features(df)
    df = select_features(df)

    # Elbow Plot
    inertia = find_optimal_k(df)
    plot_elbow(inertia)

    # KMeans
    k = 3
    df['Cluster'] = apply_kmeans(df, k)

    # PCA and Visualization
    pca_result = reduce_dimensions(df.drop(columns='Cluster'))
    plot_clusters(pca_result, df['Cluster'])
    plot_cluster_distribution(df)

    

    risk_score_by_area(df)
    print(f"Risk score by area plot generated in outputs/risk_score_by_area.png")

    cluster_summary(df)
    print(f"Cluster Analsysis generated as a csv file in outputs/cluster_summary.csv")

    crime_hotspot_detection(df)
    print(f"Crime hotspot map created in outputs/crime_hotspot_map.html")
    print(f"Opening the map...")
    map_path = os.path.abspath("outputs/crime_hotspot_map.html")
    webbrowser.open(f"file://{map_path}")

   


if __name__ == '__main__':
    main()
    



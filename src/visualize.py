import matplotlib.pyplot as plt
import seaborn as sns
import os
import folium
from folium.plugins import HeatMap

def plot_elbow(inertia):
    os.makedirs('outputs', exist_ok=True)
    plt.plot(range(1, len(inertia) + 1), inertia, marker='o')
    plt.title('Elbow Method for Optimal K')
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.tight_layout()
    plt.savefig('outputs/elbow_plot.png')
    #plt.show()

def plot_clusters(principal_components, clusters):
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(principal_components[:, 0], principal_components[:, 1],
                          c=clusters, cmap='viridis', alpha=0.7)
    plt.title('Clusters Visualized with PCA')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.colorbar(scatter)
    plt.tight_layout()
    plt.savefig('outputs/cluster_plot.png')
    #plt.show()

def plot_cluster_distribution(df):
    sns.countplot(x=df["Cluster"])
    plt.title("Distribution of Clusters")
    plt.tight_layout()
    plt.savefig("outputs/cluster_distribution.png")
    #plt.show()

def crime_hotspot_detection(df):
    df['lat_grid'] = (df['LAT'] * 100).round()
    df['lon_grid'] = (df['LON'] * 100).round()
    hotspot_counts = df.groupby(['lat_grid', 'lon_grid']).size().reset_index(name='count')
    map_center = [df['LAT'].median(), df['LON'].median()]
    crime_map = folium.Map(location=map_center, zoom_start=11)
    heat_data = [[row['lat_grid'] / 100, row['lon_grid'] / 100, row['count']] for _, row in hotspot_counts.iterrows()]
    HeatMap(heat_data, radius=10, blur=15).add_to(crime_map)
    crime_map.save("outputs/crime_hotspot_map.html")

def risk_score_by_area(df):
    area_counts = df.groupby('AREA').size().reset_index(name='crime_count')
    max_area = area_counts['crime_count'].max()
    area_counts['risk_score'] = (area_counts['crime_count'] / max_area) * 100
    plt.figure(figsize=(10,6))
    sns.barplot(data=area_counts.sort_values("risk_score", ascending=False), x="AREA", y="risk_score", palette="Reds")
    plt.title("Crime Risk Score by Area")
    plt.xlabel("Area Code")
    plt.ylabel("Risk Score (0-100)")
    plt.savefig('outputs/risk_score_by_area.png')

def cluster_summary(df):
    cluster_summary = df.groupby('Cluster').agg({
    'AREA': 'nunique',             
    'Crm Cd': 'nunique',          
    'Vict Age': 'mean',
    'Vict Sex': lambda x: x.mode()[0] if not x.mode().empty else 'Unknown',
    'Vict Descent': lambda x: x.mode()[0] if not x.mode().empty else 'Unknown',
    'Weapon Used Cd': lambda x: x.mode()[0] if not x.mode().empty else 'Unknown',
    'Status': lambda x: x.mode()[0] if not x.mode().empty else 'Unknown',
    'Status Desc': lambda x: x.mode()[0] if not x.mode().empty else 'Unknown',
    'LAT': 'mean',
    'LON': 'mean',
    'DayOfWeek': lambda x: x.mode()[0] if not x.mode().empty else 'Unknown',
    'Hour': 'mean'
}).round(2)

    cluster_summary.rename(columns={
    'AREA': 'Unique Areas',
    'Crm Cd': 'Unique Crime Types',
    'Vict Age': 'Avg Victim Age',
    'LAT': 'Avg Latitude',
    'LON': 'Avg Longitude',
    'Hour': 'Avg Hour',
}, inplace=True)

    cluster_summary.to_csv('outputs/cluster_summary.csv')







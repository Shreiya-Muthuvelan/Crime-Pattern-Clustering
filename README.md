# Crime Pattern Clustering 🕵️‍♂️📍

Data-driven identification of crime hotspots in Los Angeles using unsupervised learning and geospatial analysis.

## Table of Contents
- [Overview](#overview)
- [Data Source](#data-source)
- [Objectives](#objectives)
- [Methodology](#methodology)
- [Visualizations](#visualizations)
- [Technologies & Tools](#technologies--tools)
- [Project Structure](#project-structure)
- [Usage](#usage)

## Overview
This project analyzes historical crime data from Los Angeles to uncover spatial and temporal patterns of criminal activity.

Using unsupervised machine learning and geospatial analysis, it identifies high-risk areas and summarizes crime intensity across regions.

## Data Source
The analysis is based on the **Los Angeles Crime Data (2020–2023)** dataset, which contains reported crime incidents in the City of Los Angeles from 2020 onwards.  

The dataset is publicly available on Kaggle: [Los Angeles Crime Data 2020–2023](https://www.kaggle.com/datasets/venkatsairo4899/los-angeles-crime-data-2020-2023)

## Objectives

* Identify spatial crime hotspots within the city of Los Angeles.
* Quantify crime intensity via an interpretable risk score for different areas.
* Explore temporal trends in crime (hour of day, day of week) to support operational planning.


## Methodology
* **Feature engineering**

   * Derived spatial features from location coordinates.
   * Extracted temporal features such as hour of occurrence and day of week.
   * Encoded relevant categorical variables for clustering.

* **Clustering**

   * Applied K-Means clustering to group crime incidents into spatial–temporal clusters.
   * Used Principal Component Analysis (PCA) for dimensionality reduction and cluster visualization.

* **Cluster assessment**

   * Assessed cluster quality and interpretability through spatial distributions and temporal profiles.
   * Validated that resulting clusters correspond to meaningful crime hotspots and patterns.

## Visualizations

**Interactive Crime Distribution Map**  
Visualizes individual crime incidents across Los Angeles.  
<img src="crime_map.jpg" width="600" alt="Crime Map Preview">

**Crime Risk Score by Area**  
Assigns a score (0–100) based on total crime counts.  
<img src="risk_score_by_area.png" width="500" alt="Risk Score by Area">

**Crime Hotspot Map**  
Highlights significant clusters of criminal activity.  
<img src="crime_hotspot_map.jpg" width="500" alt="Crime Hotspot Map">

## Technologies & Tools
- **Languages:** Python 3.11
- **Data & analysis:** pandas, NumPy
- **Machine Learning:** scikit-learn (K-Means,PCA)
- **Visualization & mapping:** Matplotlib,Folium


##  Project Structure
```
crime-pattern-clustering
├── data/ # Contains downloaded dataset
├── outputs/ # Outputs are saved here 
├── src/
| ├── cluster.py
| ├── visualization.py
| ├── preprocess.py
├── utils/
| ├── download_data.py
├── main.py
├── requirements.txt
```

## Usage

1. Clone the repo
   ```bash
   git clone https://github.com/Shreiya-Muthuvelan/Crime-Pattern-Clustering.git
   cd crime-pattern-clustering
2. Install required libraries
   ```bash
   pip install -r requirements.txt
3. Download dataset
   ```bash
   python utils/download_data.py
4. Run Clustering Pipeline
   ```bash
   python main.py
   


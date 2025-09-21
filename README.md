# Crime Pattern Clustering — Detecting Crime Hotspots in Los Angeles


## Project Objective

Crime poses significant safety and resource challenges in urban environments such as Los Angeles. This project aims to leverage unsupervised machine learning and geospatial analysis to identify spatial and temporal **crime hotspots** within the city. These insights serve to enhance patrol planning, risk assessment, and policy decisions to improve public safety.

---

## Dataset Information

- **Source:** [Los Angeles Crime Data (Kaggle)](https://www.kaggle.com/datasets/hemil26/crime-in-los-angeles)  
- **Size:** Approximately 963,000 crime records  
- **Key Features Used:**  
  - Location: Latitude (`LAT`), Longitude (`LON`)  
  - Time: Date of Occurrence (`DATE OCC`), Time of Occurrence (`TIME OCC`)  
  - Crime Details: Crime Code (`Crm Cd`), Weapon Used, Crime Description  
  - Victim Information, Crime Status, Police Area, etc.  

The dataset covers multiple years and contains rich spatio-temporal and categorical data useful for clustering and pattern analysis.

---

## Data Preprocessing

The raw data underwent thorough preprocessing to facilitate effective clustering:

- Cleaning missing or inconsistent entries  
- Engineering features such as hour and day of week  
- Encoding categorical variables using label encoding  
- Scaling numerical features for uniformity  
- Dimensionality reduction through Principal Component Analysis (PCA)  

---

## Methodology

The analytical pipeline consists of:

- **K-Means Clustering** performed on a combination of temporal, spatial, and categorical features to detect crime clusters  
- **PCA** applied to reduce dimensionality and aid in exploratory visualization  
- Evaluation of cluster distributions against geographical and temporal patterns to validate hotspot detection  

---

## Exploratory Data Analysis

### Interactive Crime Distribution Map (`crime_map.html`)

This map visualizes individual crime incidents across Los Angeles, illustrating spatial distributions prior to clustering.  

- Generated from the final cell in `notebooks/eda.ipynb`  
- Opens automatically in a web browser after notebook execution  

**Preview:**  
<img src="crime_map.jpg" width="600" alt="Crime Map Preview">

---

## Visualizations

- **Crime Risk Score by Area:**  
  Assigns a risk score (0–100) to city areas based on total crime counts.  
  <img src="risk_score_by_area.png" width="500" alt="Risk Score by Area">

- **Crime Hotspot Map:**  
  Highlights significant clusters of criminal activity within the city.  
  <img src="crime_hotspot_map.jpg" width="500" alt="Crime Hotspot Map">

---

## Evaluation and Insights

- Identification of high crime density clusters consistent with official reports  
- Temporal trends showing increased night-time and weekend crime rates  
- Risk scores emphasize concentration disparities that can inform resource allocation  

---

##  Project Structure
```
crime-pattern-clustering
├── data/ # Contains downaloded dataset
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
---

## Uage

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
   


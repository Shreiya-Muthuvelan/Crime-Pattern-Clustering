import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df['DATE OCC'] = pd.to_datetime(df['DATE OCC'], errors='coerce')
    df['DayOfWeek'] = df['DATE OCC'].dt.dayofweek
    df['TIME OCC'] = df['TIME OCC'].astype(str).str.zfill(4)
    df['Hour'] = df['TIME OCC'].str[:2].astype(int)
    df = df[df['Vict Age'] >= 0]  # Remove invalid ages
    return df

def encode_features(df):
    le = LabelEncoder()
    for col in ['Vict Sex', 'Vict Descent', 'Status', 'Status Desc']:
        df[col] = le.fit_transform(df[col])
    return df

def select_features(df):
    return df.drop(columns=[
        'Premis Desc', 'Weapon Desc', 'LOCATION', 'DR_NO', 'DATE OCC', 'TIME OCC',
        'AREA NAME', 'Crm Cd Desc', 'Mocodes'
    ])

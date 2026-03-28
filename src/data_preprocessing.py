import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    le = LabelEncoder()
    categorical_cols = ['Education Level', 'Job Role', 'Location']
    
    mapping = {}
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])
        mapping[col] = dict(zip(le.classes_, le.transform(le.classes_)))
    
    return df, mapping
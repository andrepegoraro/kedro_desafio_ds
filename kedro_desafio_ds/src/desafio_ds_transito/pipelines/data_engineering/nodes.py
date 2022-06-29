"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.0
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def encode_variable(df):
    label_encoder = LabelEncoder()
    label_encoder = label_encoder.fit(df["hour_coded"])

    df["hour_coded"] = label_encoder.transform(df['hour_coded'])

    return df, label_encoder

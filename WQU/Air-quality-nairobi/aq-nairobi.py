# Autoregression model for air quality prediction
# using ARIMA
# and SARIMA models

#Import
from pymongo import MongoClient
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# connect to MongoDB
client = MongoClient(host = "localhost", port = 27017)
db = client["air-quality"]
nairobi = db["nairobi"] # collection name : nairobi
# 
def wrangle(collection):
    results = collection.find(
        {"metadata.site": 29, "metadata.measurement": "P2"},
        projection={"P2": 1, "timestamp": 1, "_id": 0},
    )

    # Read data into DataFrame
    df = pd.DataFrame(list(results)).set_index("timestamp")

    # Localize timezone
    df.index = df.index.tz_localize("UTC").tz_convert("Africa/Nairobi")

    # Remove outliers
    df = df[df["P2"] < 500]

    # Resample to 1hr window
    y = df["P2"].resample("1H").mean().fillna(method='ffill')

    return y

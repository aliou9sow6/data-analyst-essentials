import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données dans un DataFrame pandas
df = pd.read_csv("agricultural_production.csv")

# Nettoyer les données
# Supposons que nous voulons supprimer les lignes avec des valeurs manquantes
df = df.dropna()
for column in df.columns:
    print(f"Nombre de valeurs manquantes dans {column}: {df[column].isnull().sum()}")

print("\n-------------| Information sur les données: |------------\n")
print("-> df.info() : \n",df.info())
print("-> df.shape : \n",df.shape)
print("-> df.describe() : \n",df.describe())
print("-> df.columns : \n",df.columns)
print("-> df.head() : \n",df.head())
print("\n-------------| Fin de l'information sur les données |------------\n")

import pandas as pd
import numpy as np

# Générer des données aléatoires
np.random.seed(42)

# Listes d'exemples
property_types = ["apartment", "house"]
states = ["São Paulo", "Rio de Janeiro", "Minas Gerais", "Bahia", "Paraná"]

# Création du DataFrame
num_rows = 50  # Nombre de lignes

df = pd.DataFrame({
    "id": range(1, num_rows + 1),
    "property_type": np.random.choice(property_types, num_rows),
    "state": np.random.choice(states, num_rows),
    "area_m2": np.random.randint(50, 300, num_rows),
    "price_usd": np.random.randint(50_000, 500_000, num_rows),
    "lat": np.random.uniform(-30, -20, num_rows),
    "lon": np.random.uniform(-50, -40, num_rows)
})

# Sauvegarder en CSV
df.to_csv("data/real_estate_simulation.csv", index=False)

# Afficher les premières lignes
print(df.head())

# Afficher les informations
print(df.info())

# Afficher les statistiques
print("Show the statistiques : \n",df.describe())

# Afficher les valeurs uniques
print("\nShow the unique values : \n",df.nunique())

# Afficher les valeurs manquantes
print("\nShow the missing values : \n",df.isnull().sum())    

# Afficher les valeurs dupliquées
print("\nShow the duplicated values : \n",df.duplicated().sum())

# Clean the data
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# Save the cleaned data
df.to_csv("data/real_estate_simulation_cleaned.csv", index=False)
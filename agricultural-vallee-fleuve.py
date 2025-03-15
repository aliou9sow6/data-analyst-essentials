import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données dans un DataFrame pandas
df = pd.read_csv("data/agricultural_production.csv")

# Add a new column to the DataFrame
df['region'] = ['Ndioum' ,'Podor', 'Ndioum', 'Gamadji Sarré' ,'Guédé village', 'Podor', 'Podor', 'Gamadji Sarré', 'Podor', 'Tarédji']

# Clean the data
# Supposons que nous voulons supprimer les lignes avec des valeurs manquantes
df = df.dropna()

print("\n-------------| Information sur les données: |------------\n")
print("-> df.info() : \n",df.info())
print("-> df.shape : \n",df.shape)
print("-> df.describe() : \n",df.describe())
print("-> df.columns : \n",df.columns)
print("-> df.head() : \n",df.head())
print("\n-------------| Fin de l'information sur les données |------------\n")


# Visualisation des données
plt.hist(df['region'], bins=10, color='blue', edgecolor='black')
plt.title('Histogramme de la région')
plt.xlabel('Région')
plt.ylabel('Fréquence')
plt.show()

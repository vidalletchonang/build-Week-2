import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# Scarica una mappa di base dell'Italia da geopandas
italy_map = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres')).to_crs(epsg=4326)

# Limita la visualizzazione solo all'Italia
italy_map = italy_map[italy_map['name'] == 'Italy']

# Carica i dati COVID
df = pd.read_csv('covid19_italy_region _python.csv')

# Usa replace per sommare i casi di P.A Bolzano e P.A Trento in una regione Trentino-Alto Adige poi modificare la Longitudine e la latitudine
df['RegionName'] = df['RegionName'].replace({'P.A. Bolzano': 'Trentino-Alto Adige', 'P.A. Trento': 'Trentino-Alto Adige'})
df['Longitude'] = df['Longitude'].replace({11.35662422: 11.12123097})
df['Latitude'] = df['Latitude'].replace({46.49933453: 46.06893511})

df = df.groupby(['RegionName', 'Latitude', 'Longitude'])[['NewPositiveCases']].sum().reset_index()

# Unisci i dati COVID con la mappa dell'Italia
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['Longitude'], df['Latitude']))
gdf.crs = italy_map.crs  # Assegna lo stesso sistema di coordinate

# Plot
fig, ax = plt.subplots(figsize=(12, 12))  # Modifica solo la dimensione del grafico
italy_map.plot(ax=ax, alpha=0.5, edgecolor='k', color='white')  # Mappa dell'Italia come sfondo
gdf.plot(ax=ax, marker='o', color='red', markersize=gdf['NewPositiveCases'] / 100, legend=True)

# Aggiungi etichette delle regioni
for idx, row in gdf.iterrows():
    ax.annotate(row['RegionName'], (row['Longitude'], row['Latitude']), textcoords="offset points", xytext=(0,10), ha='center')

plt.title('Distribuzione geografica dei casi in Italia')
plt.xlabel('Longitudine')
plt.ylabel('Latitudine')

# Imposta i limiti degli assi per ingrandire il grafico
plt.xlim(gdf['Longitude'].min() - 1, gdf['Longitude'].max() + 1)
plt.ylim(gdf['Latitude'].min() - 1, gdf['Latitude'].max() + 1)

# mostra il grafico
plt.show()


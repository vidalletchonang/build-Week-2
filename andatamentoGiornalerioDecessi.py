import pandas as pd
import matplotlib.pyplot as plt

# Carica il dataset
df = pd.read_csv('covid19_italy_region _python.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Ordina il DataFrame per 'RegionName' e 'Date'
df = df.sort_values(by=['RegionName', 'Date'])

# Calcola la differenza giornaliera per la colonna 'Deaths' raggruppata per 'RegionName'
df['DailyDeaths'] = df.groupby('RegionName')['Deaths'].diff().fillna(0)

# Imposta i valori negativi a zero
df['DailyDeaths'] = df['DailyDeaths'].clip(lower=0)

# Disegno il grafico
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['DailyDeaths'], label='Decessi giornalieri', marker='o', linestyle='-', color='skyblue')
plt.title('Andamento temporale dei decessi giornalieri')
plt.xlabel('Data')
plt.ylabel('Numero di decessi giornalieri')
plt.legend()
plt.show()



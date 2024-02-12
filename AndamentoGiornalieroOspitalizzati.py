import pandas as pd
import matplotlib.pyplot as plt

# Carica il dataset
df = pd.read_csv('covid19_italy_region _python.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Ordina il DataFrame per 'RegionName' e 'Date'
df = df.sort_values(by=['RegionName', 'Date'])

# Calcola la differenza giornaliera per la colonna 'TotalHospitalizedPatients' raggruppata per 'RegionName'
df['DailyHospitalized'] = df.groupby('RegionName')['TotalHospitalizedPatients'].diff().fillna(0)

# Imposta i valori negativi a zero
df['DailyHospitalized'] = df['DailyHospitalized'].clip(lower=0)

# Disegna il Grafico
plt.figure(figsize=(12, 6))
plt.bar(df.index, df['DailyHospitalized'], label='Pazienti ospitalizzati giornalieri', color='purple')
plt.title('Andamento temporale dei pazienti ospitalizzati giornalieri')
plt.xlabel('Data')
plt.ylabel('Numero di pazienti ospitalizzati giornalieri')
plt.legend()
plt.show()

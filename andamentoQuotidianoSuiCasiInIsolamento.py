import pandas as pd
import matplotlib.pyplot as plt

# Carica il dataset
file_name = "covid19_italy_region_python.csv"
df = pd.read_csv(file_name)

# Pulizia dei dati
#df.dropna(inplace=True)
#verifica se ci sono dei valori null nella colonna "HomeConfinement"
#df["HomeConfinement"].isnull().sum()
# Converte la colonna 'Date' in tipo datetime
df['Date'] = pd.to_datetime(df['Date'])

#imposta la colonna "Date" come indice del DataFrame df
df.set_index("Date", inplace=True)

# Plot del andamento giornaliero dei "HomeConfinement"
plt.figure(figsize=(10, 6))
plt.bar(df.index, df["HomeConfinement"], color='m')
plt.title("Andamento quotidiano dei casi isolati a casa")
plt.xlabel("Data")
plt.ylabel("Totali")
plt.grid(True)
plt.show()
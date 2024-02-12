import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("./covid19_italy_region _python.csv")

# controllo se ci sono dati nulli nelle colonne interessate all'analisi
missing_data = df[["RegionName","NewPositiveCases","Date"]].isnull().sum()
print(missing_data)

# Converte la colonna "Date" in tipo datetime
df["Date"] = pd.to_datetime(df["Date"])

# Estrae il trimestre da ciascuna data e lo assegna a una nuova colonna chiamata "Quarter"
df["Quarter"] = df["Date"].dt.to_period("Q")

# Raggruppa i dati per trimestre e regione e calcola la somma dei nuovi casi positivi
quarterly_data = df.groupby(["Quarter", "RegionName"])["NewPositiveCases"].sum().unstack()

# Trasponi il DataFrame per invertire i trimestri con le regioni
quarterly_data = quarterly_data.T

# Crea un grafico a barre stackate
plt.figure(figsize=(12,10))
quarterly_data.plot(kind='bar', stacked=True)
# Aggiungi titoli e label agli assi
plt.title("Somma dei nuovi casi positivi per regione e trimestre")
plt.xlabel("Regione")
plt.ylabel("Somma Nuovi Casi Positivi")
plt.xticks(rotation=90)
plt.legend(title="Trimestri", loc='upper left')
plt.show()


# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

#creata variabile per dataframe regioni
df_regione = pd.read_csv("covid19_italy_region_python.csv", encoding='utf-8')

# converitita colonna 'Date' a formato datetime 
df_regione['Date'] = pd.to_datetime(df_regione['Date'])

# Ordina il DataFrame per 'RegionName' e 'Date'
df_regione = df_regione.sort_values(by=['RegionName', 'Date'])

# Calcola la differenza giornaliera per la colonna 'Deaths' raggruppata per 'RegionName'
df_regione['DailyDeaths'] = df_regione.groupby('RegionName')['Deaths'].diff().fillna(df_regione['Deaths'])
df_regione['RegionName'].replace({'P.A. Bolzano': 'Trentino-Alto Adige', 'P.A. Trento': 'Trentino-Alto Adige'}, inplace=True)

# Ora df_regione contiene la colonna 'DailyDeaths' che rappresenta il numero di morti giornaliero per ogni regione
df_deaths = df_regione.groupby('RegionName')['DailyDeaths'].sum().reset_index()




# Calcolo il tasso di mortalità annuale per ogni regione
data_list_annual = []
for region in df_regione['RegionName'].unique():
    region_data_annual = df_regione[df_regione["RegionName"] == region]
    morti_region_annual = region_data_annual["DailyDeaths"].sum()
    positivi_region_annual = region_data_annual["NewPositiveCases"].sum()
    mortality_rate_region_annual = (morti_region_annual / positivi_region_annual) * 100
    data_list_annual.append({'RegionName': region, 'MortalityRateAnnual': mortality_rate_region_annual})


# creato dataframe della lista popolata nel costrutto for lista
df_annual = pd.DataFrame(data_list_annual)


# Plot del tasso di mortalità considerando dataframe 'df_annual'
fig, axs = plt.subplots(figsize=(10, 6))
colors = ['#FF4500', '#FF6347', '#FF7F50', '#FFA07A']

axs.bar(df_annual.RegionName, df_annual.MortalityRateAnnual, color=colors)
axs.set_title('Tasso Mortalita Annuale per Regioni')
axs.set_xticklabels(axs.get_xticklabels(), rotation=45, ha='right', fontsize=8)
axs.set_xlabel('Regione', fontsize=12)
axs.set_ylabel('Tasso Mortalita (%)', fontsize=12)

plt.tight_layout()
plt.show()

# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

#dataframe regione
df_regione = pd.read_csv("covid19_italy_region_python.csv", encoding='utf-8')

#sostituito valori Bolzano e Trento a Tentino Alto Adige 
df_regione.loc[df_regione['RegionName'] == 'P.A. Bolzano', 'RegionName'] = df_regione['RegionName'].replace({'P.A. Bolzano': 'Trentino-Alto Adige'})
df_regione.loc[df_regione['RegionName'] == 'P.A. Trento', 'RegionName'] = df_regione['RegionName'].replace({'P.A. Trento': 'Trentino-Alto Adige'})

# Convertita colonna 'Date' in formato datetime 
df_regione['Date'] = pd.to_datetime(df_regione['Date'])

# Ordina il DataFrame per 'RegionName' e 'Date'
df_regione = df_regione.sort_values(by=['RegionName', 'Date'])


# Calcola il tasso di positività annuale per ogni regione
data_list_annual_positivity = []
for region in df_regione['RegionName'].unique():
    region_data_annual = df_regione[df_regione["RegionName"] == region]
    tests_performed_region_annual = region_data_annual["TestsPerformed"].sum()
    positive_cases_region_annual = region_data_annual["TotalPositiveCases"].sum()
    positivity_rate_region_annual = (positive_cases_region_annual / tests_performed_region_annual) * 100
    data_list_annual_positivity.append({'RegionName': region, 'PositivityRateAnnual': positivity_rate_region_annual})

# Creato DataFrame dalla lista del costrutto for 
df_annual_positivity = pd.DataFrame(data_list_annual_positivity)

# Plot tasso positivita
fig, axs = plt.subplots(figsize=(10, 6))
colors = ['#1E90FF', '#00BFFF', '#87CEEB', '#4169E1']

axs.bar(df_annual_positivity.RegionName, df_annual_positivity.PositivityRateAnnual, color=colors)
axs.set_title('Tasso di Positivita Annuale per Regioni')
axs.set_xticklabels(axs.get_xticklabels(), rotation=45, ha='right', fontsize=8)
axs.set_xlabel('Regione', fontsize=12)
axs.set_ylabel('Tasso di Positivita (%)', fontsize=12)

plt.tight_layout()
plt.show()



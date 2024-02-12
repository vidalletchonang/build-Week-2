# -*- coding: utf-8 -*-

import pandas as pd
import requests
import plotly.express as px

#inizializato e creato il csv regioni 
ds_covid_regioni = pd.read_csv("covid19_italy_region_python.csv", encoding='utf-8')

#convertito stringa data a tipo datatime
ds_covid_regioni['Date'] = pd.to_datetime(ds_covid_regioni['Date'])
#creata nuova colonna 'Month'
ds_covid_regioni['Month'] = ds_covid_regioni['Date'].dt.strftime('%Y-%m')


#Sostituito valori Bolzano e Trento con Trentino Alto Adige 
ds_covid_regioni.loc[ds_covid_regioni['RegionName'] == 'P.A. Bolzano', 'RegionName'] = ds_covid_regioni['RegionName'].replace({'P.A. Bolzano': 'Trentino-Alto Adige'})
ds_covid_regioni.loc[ds_covid_regioni['RegionName'] == 'P.A. Trento', 'RegionName'] = ds_covid_regioni['RegionName'].replace({'P.A. Trento': 'Trentino-Alto Adige'})

#a sua volta sostituito il suo codice regionale
ds_covid_regioni.loc[ds_covid_regioni['RegionCode'] == 22, 'RegionCode'] = ds_covid_regioni['RegionCode'].replace({22: 4 })
ds_covid_regioni.loc[ds_covid_regioni['RegionCode'] == 21, 'RegionCode'] = ds_covid_regioni['RegionCode'].replace({21: 4 })


#messo su variabile json con info delle regioni italiane
repo_url = 'https://raw.githubusercontent.com/openpolis/geojson-italy/master/geojson/limits_IT_regions.geojson'
response = requests.get(repo_url)

italy_regions_geo = response.json()

#reg_istat_code_num_value = feature["properties"].get("reg_istat_code_num")
#reg_name_value = feature["properties"].get("reg_name")
                
                


# Choropleth in cui inserisco i dati che voglio nel dataframe regioni e il geojeson
fig = px.choropleth(ds_covid_regioni, 
                    geojson=italy_regions_geo, 
                    locations='RegionCode',
                    featureidkey='properties.reg_istat_code_num',
                    color='TotalPositiveCases',
                    animation_frame='Month',
                    projection="mercator",
                    scope="europe",
                    title="Casi positivi COVID-19 in Italia (2020)",
                    labels={'TotalPositiveCases': 'Numero di casi'},
                    color_continuous_scale='rdpu',  
                    range_color=(ds_covid_regioni['TotalPositiveCases'].max(), ds_covid_regioni['TotalPositiveCases'].min()) 
                   )
fig.update_geos(showcountries=False, showcoastlines=False, showland=False, fitbounds="locations")
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()










import pandas as pd
import plotly.express as px


#dataframe europa casi covid
data = pd.read_csv('data.csv')

#convertito valori 'dataRep' in formato datetime
data['dateRep'] = pd.to_datetime(data['dateRep'], format='%d/%m/%Y')

#considero solo anno 2020 e continente europa
data_2020 = data[data['dateRep'].dt.year == 2020]
data_2020 = data_2020.sort_values(by='dateRep')
europe_data = data_2020[data_2020['continentExp'] == 'Europe']


#chropleth in cui considero casi nazione per data 
fig = px.choropleth(
    europe_data,
    locations="countryterritoryCode",
    color="cases",
    scope="europe",
    projection='natural earth',
    animation_frame="dateRep",
    color_continuous_scale='rdpu',
    range_color=(europe_data['cases'].max(), europe_data['cases'].min()),
    title="Casi positivi COVID-19 in Europa per nazione (2020)",
    labels={'cases': 'Numero di casi'}
)


fig.show()

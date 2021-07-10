import pandas as pd 
import numpy as np
from geopy.geocoders import Nominatim
import xlwings as xw

wb = xw.Book('Clientes.xlsx')
sheet = wb.sheets['2021']
df = sheet['A1:F213'].options(pd.DataFrame, index=False, header=True).value
n=list()
df['coordenada']=""
for i in range(0,len(df)):
    geolocator = Nominatim(user_agent="My_app")
    loc = geolocator.geocode(df.iloc[i,4]+" "+ df.iloc[i,5]+" Nuevo León")
    n.append(loc)
    print(str(i+2),loc)

for i in range(0,len(n)):
    try:
        df['coordenada'][i]=n[i][1]
    except:
        df['coordenada'][i]=""
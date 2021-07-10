import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

entregable=pd.read_csv("D:/Users/cesar/Desktop/dona_goya/dona goya/entregable.csv",encoding="latin",index_col="Unnamed: 0")

entregable['Stevia']=entregable['Stevia'].replace({'\xa0':""})
entregable['Stevia']=entregable['Stevia'].replace({np.nan:""})
k=entregable['Stevia'].unique()
k=np.delete(k,[0])
for i in range(0,len(k)):
    entregable['Stevia']=entregable['Stevia'].replace({k[i]:"OK"})
entregable['Fecha']=pd.to_datetime(entregable['Fecha'])
entregable.iloc[:,7]=pd.to_numeric(entregable.iloc[:,7])
entregable['Fecha']=entregable['Fecha'].replace({pd.to_datetime('2002-07-21 00:00:00'):pd.to_datetime('2020-07-21 00:00:00')})

entregable.to_csv("entregable.csv",encoding="latin")
clientes=pd.read_csv("D:/Users/cesar/Desktop/dona_goya/dona goya/Clientes.csv",encoding='latin',index_col='id_cliente')
clientes['id_cliente']=range(0,len(clientes))

for i in range(0,len(entregable)):
    if(entregable.iloc[i,4][-1]==" "):
        entregable.iloc[i,4]=entregable.iloc[i,4].rstrip(entregable.iloc[i,4][-1])
    entregable.iloc[i,4]=entregable.iloc[i,4].upper()
    
for i in range(0,len(clientes)):
    clientes.iloc[i,0]=clientes.iloc[i,0].upper()
clientes.to_csv("Clientes.csv", encoding="latin")    

clientes['CLIENTE']
lsclientes=pd.DataFrame(entregable['Cliente'].unique()).sort_values(by=0)
for i in range(0,len(lsclientes)):
    if(lsclientes.iloc[i,0][-1]==" "):
        lsclientes.iloc[i,0]=lsclientes.iloc[i,0].rstrip(lsclientes.iloc[i,0][-1])
    lsclientes.iloc[i,0]=lsclientes.iloc[i,0].upper()
lsclientes=pd.DataFrame(lsclientes[0].unique())
entregable['Cliente']=entregable['Cliente'].replace({'EDDY BURGUER':'EDDYS BURGUERS'})

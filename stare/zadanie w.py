import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("Imiona_nadane_wPolsce_w_latach_2000-2019.csv")
data=pd.DataFrame(df)
urodzeni_M=data[data['Płeć']=='M'].groupby(['Rok'])['Liczba'].sum()
urodzeni_K=data[data['Płeć']=='K'].groupby(['Rok'])['Liczba'].sum()
rok=data['Rok'].drop_duplicates()
plt.plot(rok,urodzeni_M,color='b',label='mezczyzna')
plt.plot(rok,urodzeni_K,color='r',label='kobieta')
plt.show()
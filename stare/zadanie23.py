import pandas as pd
import numpy as np
df=pd.read_csv('zamowienia.csv',sep=';')
data=pd.DataFrame(df)
print(data.groupby(['Sprzedawca'])['Utarg'].sum())
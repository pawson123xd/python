import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('zamowienia.csv',sep=';')
data=pd.DataFrame(df)
m=data.groupby(['Sprzedawca'])['Utarg'].count()
b=data['Sprzedawca'].sort_values()
lista=[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
plt.bar(b.drop_duplicates(),m)
plt.show()
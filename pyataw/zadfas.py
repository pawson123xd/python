import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('zamowienia.csv',sep=';')
data=pd.DataFrame(df)
m=data.groupby(['Sprzedawca'])['Utarg'].sum()
b=data['Sprzedawca'].sort_values()
lista=[0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
def prepare_label(pct, br):
 absolute = int(pct / 100. * np.sum(br))
 return "{:.1f}%".format(pct, absolute)
plt.pie(m,labels=b.drop_duplicates(),
autopct="%1.1f%%",shadow=True)
plt.show()
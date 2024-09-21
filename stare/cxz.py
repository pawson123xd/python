import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('Imiona_nadane_wPolsce_w_latach_2000-2019.csv')
data=pd.DataFrame(df)
n=data[data['Płeć']=="K"].groupby("Rok").Liczba.agg("sum")
w=data[data['Płeć']=="M"].groupby("Rok").Liczba.agg("sum")
r=np.arange(2000,2020)
urodzeni=data.groupby("Rok").Liczba.agg("sum")
plt.subplot(3,1,3)
plt.bar(r,urodzeni)
plt.subplot(3,1,2)
plt.plot(r,n)
plt.plot(r,w)
plt.subplot(3,1,1)
r=np.arange(2000,2020)
p=["K","M"]
suma=data.groupby("Płeć").Liczba.agg("sum")
plt.bar(p,suma)
plt.show()
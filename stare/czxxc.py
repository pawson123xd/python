import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('Imiona_nadane_wPolsce_w_latach_2000-2019.csv')
data=pd.DataFrame(df)
n=data[data['Płeć']=="K"].groupby("Rok").Liczba.agg("sum")
w=data[data['Płeć']=="M"].groupby("Rok").Liczba.agg("sum")
urodzeni=data.groupby("Rok").Liczba.agg("sum")
e=data["Rok"]
p=["K","M"]
suma=data.groupby("Płeć").Liczba.agg("sum")
plt.bar(e.drop_duplicates(),w,color="b",label="chołki")
plt.bar(e.drop_duplicates(),n,color="r",label="Kobiety")
plt.legend()
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("Imiona_nadane_wPolsce_w_latach_2000-2019.csv")
data=pd.DataFrame(df)
x=data[(data["Rok"]>=2000) & (data["Rok"]<=2005)].groupby(["Płeć"])["Liczba"].sum()
plt.title("liczba urodzeni dziewczynek i chłopaków z rok 2000 do 2005")
plt.pie(x,labels=['dziewczynek','chłopaków'],autopct="%1.1f%%")
plt.show()

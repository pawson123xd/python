import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv("Imiona_nadane_wPolsce_w_latach_2000-2019.csv")
data=pd.DataFrame(df)
urodzeni_M=data[data['Płeć']=='M']['Liczba'].sum()
urodzeni_K=data[data['Płeć']=='K']['Liczba'].sum()
plt.title("cały zbior urodzeni chłopaków i dziewczynek")
plt.bar("chłopców",urodzeni_M)
plt.bar("dziewczynek",urodzeni_K,color='r')
plt.show()
import matplotlib.pyplot as plt
import  pandas as pd
import numpy as np
df=pd.read_csv("transport22.csv",sep=";",header=None).T
df[3]=df[3].str.replace(" ","")
df[3]=df[3].astype({3:"int"})
print(df)
transport2014=df[df[1]=="2014"].groupby([0])[3].sum()
transport2016=df[df[1]=="2016"].groupby([0])[3].sum()
rodzaje=df[0].drop_duplicates().sort_values()
plt.subplot(2,1,1)
plt.pie(transport2014,labels=rodzaje,autopct="%1.1f%%",shadow=True)
plt.title("dane transport w 2014")
plt.subplot(2,1,2)
plt.pie(transport2016,labels=rodzaje,autopct="%1.1f%%")
plt.title("dane transport w 2016")
plt.savefig("zad3.jpg")
plt.show()
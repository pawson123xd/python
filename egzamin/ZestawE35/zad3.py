import matplotlib.pyplot as plt
import  pandas as pd
import  numpy as np
df=pd.read_csv("gastro.csv",sep="@",header=None).T
print(df)
df=df.drop([0])
df=df.astype({1:"int"})
df=df.astype({2:"int"})
dane1=df[df[0]=="restauracje"].groupby([1])[2].sum()
dane2=df[df[0]=="bary"].groupby([1])[2].sum()
dane3=df[df[0]=="stołówki"].groupby([1])[2].sum()
dane4=df[df[0]=="punkty gastronomiczne"].groupby([1])[2].sum()
rok=df[1].drop_duplicates()
plt.bar(rok,dane1,width=0.25,label="restauracje")
plt.bar(rok+0.25,dane2,width=0.25,label="bary")
plt.bar(rok+0.50,dane3,width=0.25,label="stołówki")
plt.bar(rok+0.75,dane4,width=0.25,label="punkty gastronomiczne")
plt.legend()
plt.title("Zarobki Typy placówek ")
plt.savefig("zad3.png")
plt.show()
import matplotlib.pyplot as plt
import pandas as pd
import  numpy as np
df=pd.read_excel("gastro.xlsx",header=None).T
print(df)
df=df.drop([0])
dane1=df[df[0]=="restauracje"].groupby([1])[2].sum()
dane2=df[df[0]=="bary"].groupby([1])[2].sum()
dane3=df[df[0]=="stołówki"].groupby([1])[2].sum()
dane4=df[df[0]=="punkty gastronomiczne"].groupby([1])[2].sum()
plt.plot(dane1,label="restauracje")
plt.plot(dane2,label="bary")
plt.plot(dane3,label="stołówki")
plt.plot(dane4,label="punkty gastronomiczne")
plt.title("Wartosc typów placówek w danych rokach")
plt.ylabel("Wartosc")
plt.xlabel("Rok")
plt.legend()
plt.savefig("zad3.pdf")
plt.show()



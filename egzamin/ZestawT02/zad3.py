import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_excel("rod2.xlsx",header=None).T
print(df)
ogrody=df[(df[0]=='ogrody') & (df[1]=='powierzchnia')].groupby([2])[3].sum()
działki=df[(df[0]=='działki') & (df[1]=='liczba')].groupby([2])[3].sum()
plt.subplot(2,1,1)
plt.plot(ogrody,label="Wartosc")
plt.title("Wartosc ogrody powierzchnia")
plt.ylabel("Wartość")
plt.xlabel("Rok")
plt.subplot(2,1,2)
plt.plot(działki,label="Wartosc")
plt.xlabel("Rok")
plt.ylabel("Wartość")
plt.title("Wartosc działki liczba")
plt.savefig("zad3.pdf")
plt.show()


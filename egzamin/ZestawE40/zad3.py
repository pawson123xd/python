import matplotlib.pyplot as plt
import pandas  as pd
import  numpy as np
df=pd.read_excel("rod.xlsx",header=None).T
print(df)
ogrody_liczbowe=df[(df[0]=="ogrody") & (df[1]=="liczba")].groupby([2])[3].sum()
ogrody_powierzchnia=df[(df[0]=="ogrody") & (df[1]=="powierzchnia")].groupby([2])[3].sum()
działki_liczbowe=df[(df[0]=="działki") & (df[1]=="liczba")].groupby([2])[3].sum()
działki_powierzchnia=df[(df[0]=="działki") & (df[1]=="powierzchnia")].groupby([2])[3].sum()
plt.plot(ogrody_liczbowe,label="ogrody i liczba")
plt.plot(ogrody_powierzchnia,label="ogrody i powierzchnia")
plt.plot(działki_liczbowe,label="ogrody i powierzchnia")
plt.plot(działki_powierzchnia,label="ogrody i powierzchnia")
plt.title("ceny działek i ogrody")
plt.ylabel("wartość")
plt.xlabel("rok")
plt.legend()
plt.savefig("zad3.jpg")
plt.show()
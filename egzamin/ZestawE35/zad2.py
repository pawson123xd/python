import matplotlib.pyplot as plt
import  pandas as pd
import  numpy as np
df=pd.read_excel("ceny.xlsx")
print(df)
dane1=df[df["Rodzaje towarów i usług"]=="jabłka - za 1kg"]["Wartosc"].mean()
dane2=df[df["Rodzaje towarów i usług"]=="pomarańcze - za 1kg"]["Wartosc"].mean()
print(dane1)
print(dane2)
dane1=df[df["Rodzaje towarów i usług"]=="jabłka - za 1kg"]["Wartosc"]
dane2=df[df["Rodzaje towarów i usług"]=="pomarańcze - za 1kg"]["Wartosc"]
Miesiące=df["Miesiące"].drop_duplicates()
plt.plot(Miesiące,dane1,label="jabłka - za 1kg")
plt.plot(Miesiące,dane2,label="pomarańcze - za 1kg")
plt.legend()
plt.title("dane ceny jabłka i pomarańcze w 2017")
plt.savefig("zad2.jpd")
plt.show()

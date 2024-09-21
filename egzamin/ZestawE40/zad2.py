import matplotlib.pyplot as plt
import pandas  as pd
import  numpy as np
df=pd.read_csv("praca.csv",sep=";")
print(df)
df["Wartosc"]=df["Wartosc"].str.replace(",",".")
df["Wartosc"]=df["Wartosc"].astype({"Wartosc":"float"})
pracyopen=df[df["Miejsca pracy"]=="liczba nowo utworzonych miejsc pracy"].groupby(["Rok"])['Wartosc'].sum()
close=df[df["Miejsca pracy"]=="liczba zlikwidowanych miejsc pracy"].groupby(["Rok"])['Wartosc'].sum()
print(pracyopen)
print(close)
rok=df["Rok"].drop_duplicates()
plt.bar(rok,pracyopen,label="liczba nowo utworzonych miejsc pracy")
plt.bar(rok,close,label="liczba zlikwidowanych miejsc pracy")
plt.legend()
plt.xlabel("Rok")
plt.ylabel("liczba miesc pracy")
plt.title("otwarte miesca pracy i zamkniete miesca pracy")
plt.savefig("zad2.png")
plt.show()
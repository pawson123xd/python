import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_excel("sprzedaz12.xlsx")
data=pd.DataFrame(df)
produkt1=data[data["Produkt"]=="Marchew"].groupby(["Rok"])['Sprzedaż'].sum()
produkt2=data[data["Produkt"]=="Pomidor"].groupby(["Rok"])['Sprzedaż'].sum()
produkt3=data[data["Produkt"]=="Ogórek"].groupby(["Rok"])['Sprzedaż'].sum()
print("Marchew")
print(produkt1)
print("Pomidor")
print(produkt2)
print("Ogórek")
print(produkt3)
rok=data["Rok"].drop_duplicates()
plt.subplot(3,1,1)
plt.pie(produkt1,labels=rok,autopct="%1.1f%%")
plt.title("Marchew")
plt.text(-6,2,"170231")
plt.subplot(3,1,2)
plt.pie(produkt2,labels=rok,autopct="%1.1f%%")
plt.title("Pomidor")
plt.subplot(3,1,3)
plt.pie(produkt3,labels=rok,autopct="%1.1f%%")
plt.title("Ogórek")
plt.savefig("zadnaie2.jpg")
plt.show()




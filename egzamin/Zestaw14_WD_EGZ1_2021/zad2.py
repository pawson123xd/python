import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_excel('sprzedaz14.xlsx')
print(df)
produkt1=df[df['Produkt']=='Masło'].groupby(["Rok"])['Sprzedaż'].sum()
print(produkt1)
produkt2=df[df['Produkt']=='Margaryna'].groupby(["Rok"])['Sprzedaż'].sum()
print(produkt2)
produkt3=df[df['Produkt']=='Jogurt'].groupby(["Rok"])['Sprzedaż'].sum()
rok=df['Rok'].drop_duplicates()
plt.bar(rok,produkt1,width=0.25,label='Masło')
plt.bar(rok+0.25,produkt2,width=0.25,label='Margaryna')
plt.bar(rok+0.5,produkt3,width=0.25,label='Jogurt')
plt.title("ceny produktów")
plt.text(2014.9,2013,'170321')
plt.legend()
plt.savefig("zad2.pdf")
plt.show()

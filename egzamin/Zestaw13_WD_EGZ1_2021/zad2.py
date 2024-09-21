import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_excel('ceny13.xlsx')
print(df)
produkt1=df[df['Rodzaje towarów']=="dżem - za 360g"]['Wartosc'].mean()
produkt2=df[df['Rodzaje towarów']=="miód pszczeli - za 400g"]['Wartosc'].mean()
print(produkt1)
print(produkt2)
produkta1=df[df['Rodzaje towarów']=="dżem - za 360g"].groupby(['Rok'])['Wartosc'].sum()
produkta2=df[df['Rodzaje towarów']=="miód pszczeli - za 400g"].groupby(['Rok'])['Wartosc'].sum()
print(produkta2)
plt.plot(produkta1,label='dżem - za 360g')
plt.plot(produkta2,label='miód pszczeli - za 400g')
plt.text(2014,12,"170321")
plt.legend()
plt.savefig("zad2.png")
plt.show()

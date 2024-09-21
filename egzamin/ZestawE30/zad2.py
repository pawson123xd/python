import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_excel("ceny.xlsx")
print(df)
dane1=df[df["Rodzaje towarów i usług"]=="cukier biały kryształ - za 1kg"].groupby(["Miesiące"])["Wartosc"].mean()
dane2=df[df["Rodzaje towarów i usług"]=="czekolada mleczna - za 100g"].groupby(["Miesiące"])["Wartosc"].mean()
print(dane1)
print(dane2)
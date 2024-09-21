import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("studenci21.csv",sep=";")
print(df)
studiastacjonarne_M=df[(df['Tryby nauczania']=='studia stacjonarne (dzienne)') & (df['Płeć']=='mężczyźni')].groupby(["Rok"])["Wartosc"].sum()
studianiestacjonarne_M=df[(df['Tryby nauczania']=='studia niestacjonarne') & (df['Płeć']=='mężczyźni')].groupby(["Rok"])["Wartosc"].sum()
studianiestacjonarne_K=df[(df['Tryby nauczania']=='studia niestacjonarne') & (df['Płeć']=='kobiety')].groupby(["Rok"])["Wartosc"].sum()
studiastacjonarne_K=df[(df['Tryby nauczania']=='studia stacjonarne (dzienne)') & (df['Płeć']=='kobiety')].groupby(["Rok"])["Wartosc"].sum()
rok=df["Rok"].drop_duplicates()
plt.bar(rok,studiastacjonarne_K,width=0.25,color="r",label="dzienne kobiety")
plt.bar(rok,studiastacjonarne_M,width=0.25,color="black",label="dzienne mężczyźni")
plt.bar(rok+0.25,studianiestacjonarne_K,width=0.25,color="g",label="niestacjonarne kobiety")
plt.bar(rok+0.25,studianiestacjonarne_M,width=0.25,color="y",label="niestacjonarne mężczyźni")
plt.legend()
plt.title("Dane studiowanie kobiet i mężczyźni na studiach niestacjonarne i dzienne")
plt.savefig("zad3.png")
plt.show()
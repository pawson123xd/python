import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv("transport14.csv",sep=";",header=None).T
motory=df[df[0]=="motocykle ogółem"].groupby([1])[3].sum()
samochody=df[df[0]=="samochody osobowe"].groupby([1])[3].sum()
autobusy=df[df[0]=="autobusy ogółem"].groupby([1])[3].sum()
rok=df[1].drop_duplicates()
plt.plot(motory,label="motory")
plt.plot(samochody,label="samochody")
plt.plot(autobusy,label="autobusy")
plt.legend()
plt.savefig("zad3.jpg")
plt.show()
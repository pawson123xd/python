import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('turystyka13.csv',sep=";",header=None).T
hotele=df[df[0]=='hotele'].groupby([1])[3].sum()
pensjonaty=df[df[0]=='pensjonaty'].groupby([1])[3].sum()
motele=df[df[0]=='motele'].groupby([1])[3].sum()
plt.bar(rok,hotele)
plt.show()
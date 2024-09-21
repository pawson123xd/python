import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("sport21.xlsx")
gryzespołowe=df[df["Rok"]==2014].groupby(['Gry zespołowe'])['Wartosc'].sum()
rodziajegier=df['Gry zespołowe'].drop_duplicates().sort_values()
plt.pie(gryzespołowe,labels=rodziajegier,autopct="%1.1f%%")
plt.title("interesowanie gier spotowych w 2014")
plt.savefig("zad3.pdf")
plt.show()
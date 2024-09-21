import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv("ceny3.csv",sep="#")
data=pd.DataFrame(df)
print(data)
ryż=data[data['Rodzaje towarów i usług']=='ryż - za 1kg'].groupby(['Miesiące'])['Wartosc'].sum()
miesioce=data['Miesiące'].sort_values()
maka=data[data['Rodzaje towarów i usług']=='mąka pszenna - za 1kg'].groupby(['Miesiące'])['Wartosc'].sum()
print(ryż)
plt.bar(ryż,miesioce.drop_duplicates(),color='r')
plt.bar(maka,miesioce.drop_duplicates(),color='b')
plt.savefig("zadanie3.jpg")
plt.show()
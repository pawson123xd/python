import pandas as pd
df=pd.read_excel('ceny.xlsx')
data=pd.DataFrame(df)
print(data[(data['Rodzaje towarów i usług']=='jabłka - za 1kg') | (data['Rodzaje towarów i usług']=='pomarańcze - za 1kg') & (data['Rok']==2017)]['Wartosc'].mean())
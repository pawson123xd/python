import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_excel("kina4.xlsx")
data=pd.DataFrame(df)
print(data)
Gestor1=data[data['Gestor']=='miejskie'].groupby(['Rok'])['Wartosc'].sum()
Gestor2=data[data['Gestor']=='powiatowe'].groupby(['Rok'])['Wartosc'].sum()
Gestor3=data[data['Gestor']=='wojewódzkie'].groupby(['Rok'])['Wartosc'].sum()
rok=np.arange(2015,2018)
plt.bar(rok,Gestor1,color="r",width=0.25,label='miejskie')
plt.bar(rok+0.25,Gestor2,color="b",width=0.25,label='powiatowe')
plt.bar(rok+0.50,Gestor3,color="g",width=0.25,label='powiatowe')
plt.xlabel("Rok")
plt.ylabel('Wartosc')
plt.legend()
plt.savefig("zdanie2.png")
plt.show()
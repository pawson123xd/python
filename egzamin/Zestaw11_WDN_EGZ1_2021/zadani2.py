import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_excel("mieszkania11.xlsx")
data=pd.DataFrame(df)
Formybudownictwa=data[data['Formy budownictwa']=='indywidualne'].groupby(["Rok"])['Wartość'].sum()
Formybudownictwa1=data[data['Formy budownictwa']=='spółdzielcze'].groupby(["Rok"])['Wartość'].sum()
Formybudownictwa3=data[data['Formy budownictwa']=='komunalne'].groupby(["Rok"])['Wartość'].sum()
rok=np.arange(2015,2019)
print(data)
plt.bar(rok,Formybudownictwa,color="g",width=0.25,label='indywidualne')
plt.bar(rok+0.25,Formybudownictwa1,color="b",width=0.25,label='spółdzielcze')
plt.bar(rok+0.50,Formybudownictwa3,color="r",width=0.25,label='komunalne')
plt.legend()
plt.savefig("zadanie2.pdf")
plt.show()
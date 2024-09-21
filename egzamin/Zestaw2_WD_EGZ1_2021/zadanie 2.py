import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_excel("ceny2.xlsx")
data=pd.DataFrame(df)
ryz=data[data['Rodzaje towarów']=='ryż - za 1kg']['Wartość']
rok=data[data['Rodzaje towarów']=='ryż - za 1kg']['Rok']
maka=data[data['Rodzaje towarów']=='mąka pszenna - za 1kg']['Wartość']
rok2=data[data['Rodzaje towarów']=='mąka pszenna - za 1kg']['Rok']
plt.text(2010,4.2,"170231")
plt.plot(rok,ryz,label="ceny ryz skali rok")
plt.plot(rok2,maka,label=' cany mąka skali roku')
plt.legend()
plt.savefig("zadanie2.pdf")
plt.show()

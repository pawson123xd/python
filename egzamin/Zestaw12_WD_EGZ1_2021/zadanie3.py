import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
lista=[";"," "]
df=pd.read_csv('dows12.csv',delimiter=";")
data=pd.DataFrame(df)
cleaned = data.dropna()
print(cleaned)
czas=cleaned["Czas"]
zmienna1=cleaned["Zmienna1"]
zmienna2=cleaned["Zmienna2"]
zmienna3=cleaned["Zmienna3"]
plt.plot(czas,zmienna1,color="orange",linestyle=':',label='Zmienna1')
plt.plot(czas,zmienna2,color="blue",linestyle='-.',label='Zmienna2')
plt.plot(czas,zmienna3,color="r",linestyle='--',label='Zmienna3')
plt.title("mierzenie czas zmienych")
plt.xlabel('czas')
plt.ylabel('Zmienne')
plt.legend()
plt.show()

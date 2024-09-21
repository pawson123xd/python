import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df=pd.read_excel('ceny1.xlsx')
data=pd.DataFrame(df)
rok=data['Rok']
wartosc=data['Wartość']
x=np.arange(0,len(wartosc))
plt.subplot(1,2,2)
plt.plot(x,wartosc)
plt.title("170231                                                                                                                  ")

plt.show()
print(data)
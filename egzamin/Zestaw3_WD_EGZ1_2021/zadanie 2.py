import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_excel("handel3.xlsx").T
data=pd.DataFrame(df)
print(data)
rok2016=data[data[0]==2016][1]
rok2017=data[data[0]==2017][1]
plt.subplot(2,1,1)
plt.pie(rok2016,autopct="%1.1f%%",labels=['hipermarkety','supermarkety ','domy towarowe ','domy handlowe'])
plt.title("Rok2016")
plt.subplot(2,1,2)
plt.pie(rok2017,autopct="%1.1f%%",labels=['hipermarkety','supermarkety ','domy towarowe ','domy handlowe'])
plt.title("Rok2017")
plt.savefig("zadanie3.png")
plt.show()
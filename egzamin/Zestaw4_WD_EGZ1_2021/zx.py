import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df=pd.read_csv('sprzedaz4.csv',sep="@").T
x=np.arange(0,len(df[0]))
plt.plot(x,df[1])
plt.title("sprzedarz")
plt.xlabel("Rok")
plt.ylabel("wartość")
plt.xticks(x,df[0])
plt.savefig("zdanie3.jpg")
plt.show()
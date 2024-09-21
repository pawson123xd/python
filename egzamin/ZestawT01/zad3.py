import matplotlib.pyplot as plt
import pandas as pd
import  numpy as np
df=pd.read_excel("turystyka1.xlsx").T
data=df[df[0]==2015][1]
data1=df[df[0]==2016][1]
print(data)
x=np.arange(0,len(data))
plt.plot(x,data,linestyle="--",label="rok 2015")
plt.plot(x,data1,linestyle=":",label="rok 2016")
plt.grid(True)
plt.legend()
plt.show()

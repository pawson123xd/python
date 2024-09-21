import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('nieruchomosci1.csv',sep=";",header=None).T
df=df[4].str.replace(' ','')
df=df.astype({4:'int'})
plt.pie(df,autopct='%1.1f%%')
plt.show()
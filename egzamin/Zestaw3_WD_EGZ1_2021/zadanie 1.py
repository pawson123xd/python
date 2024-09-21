import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
data=[-35,-20,-50,-40,-45]
data1=['A','B','C','D','E']
plt.subplot(1,2,1)
plt.xlim(-50, 0)
plt.barh(data1,data,color=['greenyellow','gold','blue','mediumpurple','palevioletred'])
plt.title("Wykres 1")
plt.subplot(1,2,2)
data3=[38,38,39,35,36]
plt.barh(data1,data3,color=['yellowgreen','mediumpurple','darkorange','green','yellowgreen'])
plt.title("Wykres 2")
plt.savefig("zadanie1.jpg")
plt.show()
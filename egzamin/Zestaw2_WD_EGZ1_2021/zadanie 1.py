import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.subplot(1,2,1)
lista=['A','B','C','D','E']
x=[35,45,15,40,38]
x1=[-30,-40,-45,-40,-35]
plt.subplot(1,2,1)
plt.barh(lista,x,color=['skyblue','Pink','orange','gray','purple'])
plt.subplot(1,2,2)
plt.barh(lista,x1,color=['orchid','darkturquoise','darkturquoise','sienna','y'])
plt.savefig("zadanie1.pdf")
plt.show()
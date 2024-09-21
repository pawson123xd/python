import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
lista=[29.7,17.4,17.4,18.1,17.4]
lista1=["A","B","C","D","E",]
plt.pie(lista,labels=lista1,autopct="%1.1f%%",startangle=50,colors=["aqua","darkred",'gray','orange','royalblue'],explode=[0,0.1,0,0,0],shadow=True)
plt.title("Tytul W")
plt.savefig("zadanie1.pdf")
plt.show()
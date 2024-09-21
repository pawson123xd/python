import matplotlib.pyplot as plt
import  pandas as pd
import  numpy as np
dane=[12.22,11.11,22.22,13.33,23.89,17.22]
lista=["F","A","B","C","D","E"]
plt.pie(dane,labels=lista,autopct="%0.2f%%",colors=["green","orange","y","mediumpurple","teal","steelblue"],explode=[0.1,0,0,0.1,0,0], startangle=-15)
plt.title("Tytuł")
plt.savefig("zad1.png")
plt.show()
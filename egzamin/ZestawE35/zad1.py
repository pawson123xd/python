import matplotlib.pyplot as plt
import  pandas as pd
import  numpy as np
x=lista=[21,27,33,15,35]
dane=["A","B","C","D","E"]
plt.pie(x,labels=x,colors=["red","aqua","pink","lightblue","purple"],startangle=90)
plt.legend(dane,loc="upper left")
plt.title("Tytuł")
plt.savefig("zad1.pdf")
plt.show()
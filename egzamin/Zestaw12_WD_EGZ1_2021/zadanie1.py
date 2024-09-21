import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
lista=["A","B","C","D","E"]
data=[-45,-27,-25,-15,-50]
plt.barh(lista,data,color=["darkorange","sienna","mediumpurple","darkred","blue"])
plt.title("wykres słupkowy")
plt.savefig("zadanie1.pdf")
plt.show()
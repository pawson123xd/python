import matplotlib.pyplot as plt
import pandas as pd
import  numpy as np
dane1=[37,47,49,26,23]
lista=["A","B","C","D","E"]
plt.pie(dane1,labels=dane1,startangle=90,colors=["lime","sienna","orchid","silver","lightgreen"])
plt.legend(lista,loc="upper right")
plt.savefig("zad1.jpg")
plt.show()
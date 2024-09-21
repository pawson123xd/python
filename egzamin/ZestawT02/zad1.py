import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
liczby=[5,30,1]
liczby1=[8,26,3]
handel=np.arange(0,len(liczby))
plt.bar(handel,liczby,width=0.25,label="Rok 2016")
plt.bar(handel+0.25,liczby1,width=0.25,label="Rok 2017")
plt.xticks(handel, ('Hipermarkety', 'Supermarkety', 'Domy handlowe'))
plt.legend()
plt.savefig("zad1.png")
plt.show()

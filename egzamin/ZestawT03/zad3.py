import matplotlib.pyplot as plt
import  pandas as pd
import  numpy as np
df=pd.read_excel("produkcja3.xlsx",header=None).T
dane1=df.drop([0])
a=dane1.astype({0:'int',1:'int'})
plt.plot(a[0],a[1],label="ceny")
plt.title("ceny produkcja")
plt.xlabel("Rok")
plt.ylabel("Wartość")
plt.legend()
plt.savefig("zadanie3.pdf")
plt.show()


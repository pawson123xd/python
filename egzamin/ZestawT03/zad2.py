import matplotlib.pyplot as plt
import  pandas as pd
import  numpy as np
df=pd.read_excel("licea3.xlsx")
print(df)
nazwa=df["Nazwa"]
wartość=df["Wartość"]
plt.bar(nazwa,wartość)
plt.xlabel("Wojewóstwa")
plt.ylabel("Wartość")
plt.savefig("zad2.jpg")
plt.show()
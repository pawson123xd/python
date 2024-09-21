import matplotlib.pyplot as plt
import pandas  as pd
import  numpy as np
lista=[10,-40,-50,180,120]
lista1=[-65,100,180,170,160]
lista2=[100,190,170,110,65]
x=np.arange(0,5)
plt.bar(x,lista1,width=0.25,color="lime",label="B")
plt.bar(x+0.25,lista2,width=0.25,color="fuchsia",label="C")
plt.bar(x-0.25,lista,width=0.25,color="palegreen",label="A")
plt.yticks([-100,-75,-24,0,13,66,90,180])
plt.axhline(-75,color="silver")
plt.axhline(-24,color="silver")
plt.axhline(0,color="silver")
plt.axhline(13,color="silver")
plt.axhline(66,color="silver")
plt.axhline(90,color="silver")
plt.axhline(180,color="silver")
plt.legend(loc="upper right")
plt.xlabel("Podpis osi x")
plt.ylabel("Podpis osi y")
plt.title("wykres")
plt.savefig("zadanie.pdf")
plt.show()
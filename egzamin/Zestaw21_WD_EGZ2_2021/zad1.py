import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
y=np.arange(0,6)
x=[-48,-5,-10,-58,-8,-20]
x1=[40,20,28,21,38,35]
x2=[85//2,50//2,60//2,65//2,36,70//2]
skaz=[-48,1,32,82,98]
plt.barh(y,x2,label="C",color="mediumorchid",left=x1)
plt.barh(y,x,label="B",color="b")
plt.barh(y,x1,label="A",color="violet")
plt.title("Tytuł wykres")
plt.xticks(skaz)
plt.axvline(-48, color='silver')
plt.axvline(1, color='silver')
plt.axvline(32, color='silver')
plt.axvline(82, color='silver')
plt.axvline(98, color='silver')
plt.legend()
plt.savefig("zad1.jpg")
plt.show()
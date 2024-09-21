import matplotlib.pyplot as plt
import  pandas as pd
import numpy as np
x=np.arange(0,3*np.pi)
y=x+np.e
y1=-4*x+2
y2=2*np.cos(x)
plt.plot(x,y,label='y = x + e',linestyle=':',color='blue')
plt.plot(x,y1,label='y = −4x + 2',linestyle="--",color="g")
plt.plot(x,y2,label='y = 2 cos(x)',linestyle='-.',color="black")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.title("wykres")
plt.savefig("zad1.png")
plt.show()
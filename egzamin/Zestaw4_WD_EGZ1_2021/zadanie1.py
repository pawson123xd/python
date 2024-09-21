import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
x=np.arange(-5,6,0.1)
y=-x**3+3*x-7
y1=4*x+6
y2=6+4*x**3
plt.plot(x,y,"+",color="orange",label="y=-x**3+3*x-7")
plt.plot(x,y1,"-",color="black",label="y=4*x+6")
plt.plot(x,y2,":",color="blue",label='y=6+4*x**3')
plt.title("wykres")
plt.ylabel("y")
plt.xlabel("x")
plt.legend()
plt.grid(True)
plt.savefig("zadanie1.pdf")
plt.show()

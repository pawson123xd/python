import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
x=np.arange(0,2*np.pi,0.1)
y=3*x**2+2*x+7
y1=-4*x+2
y2=2*np.cos(x)
plt.plot(x,y,label="y = 3x2 + 2x + 7 ",color="r",linestyle="-.")
plt.plot(x,y1,label="y = −4x + 2",color="g",linestyle=":")
plt.plot(x,y2,label="y = 2cos(x)",color="black", linestyle="--")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.savefig("zad1.png")
plt.show()

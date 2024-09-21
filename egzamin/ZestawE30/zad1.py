import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
fig, ax1 = plt.subplots()
x=np.arange(-10,11,0.1)
y1=x**2+2*x-4
y2=-x**3+x-2
ax1.plot(x,y1,label="x**2+2*x-4",linestyle="--",color="b")
ax1.plot(x,y2,label="x**2+2*x-4",linestyle="-.",color="orange")
plt.legend()
plt.xlim(-15,15)
plt.grid(True)
plt.ylim(-400,400)
ax2 = ax1.twinx()
x1=np.arange(-10,11,0.1)
y3=2*np.cos(x1+5)
plt.ylim(-3,3)
ax2.plot(x,y3,label="2*cos(x+5)",linestyle="--",color="g")
plt.legend(loc="lower right")
plt.savefig("zad1.jpg")
plt.show()
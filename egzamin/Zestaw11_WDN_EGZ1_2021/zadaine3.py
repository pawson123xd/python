import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
x=np.arange(1,3*np.pi,0.1)
y=np.sin(2*x)
y1=3*x-5
y2=2*np.cos(x)
plt.plot(x,y,':',color='b',label='y=sin(2*x)')
plt.plot(x,y1,'>',color='r',label='y=3*x-5')
plt.plot(x,y2,'r--',color='r',label='y=2*np.cos(x)')
plt.title("wykresy sin,cos i y=3*x-5")
plt.grid(True)
plt.legend()
plt.savefig("zadanie3.png")
plt.show()

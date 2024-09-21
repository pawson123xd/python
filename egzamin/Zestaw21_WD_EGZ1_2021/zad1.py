import matplotlib.pyplot as plt
import  pandas as pd
import numpy as np
x=np.arange(0,5,0.1)
y=np.cos(x)
y1=np.sin(x)
plt.plot(x,y,linestyle=":",label="cos(x)")
plt.plot(x,y1,linestyle=":",label="sin(x)")
plt.title("To jest tytuł wykresu")
plt.xlabel("oś dolna")
plt.ylabel("oś lewa",color="g")
plt.legend()
plt.savefig("zad1.pdf")

plt.show()
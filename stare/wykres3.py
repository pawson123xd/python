import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,30,0.1)
x1= np.arange(0,-30,-0.1)
s= np.sin(x)
s1=np.sin(x1)
plt.plot(x,s+2,label='sin(x)')
plt.plot(x,s1,label='sin(x)')
plt.title("Wykres sin(x)")
plt.xlabel('x')
plt.ylabel('sin i cos')
plt.legend()
plt.show()

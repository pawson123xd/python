import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1,30,0.1)
s= np.sin(x)
c=np.cos(x)
plt.plot(x, s,label='sin')
plt.plot(x, c,label='cos')
plt.title("Wykres sin(x) i cos(x)")
plt.xlabel('x')
plt.ylabel('sin i cos')
plt.legend()
plt.show()

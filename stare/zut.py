import matplotlib.pyplot as plt
import  numpy as np
def rzut(n):
    lista=[]
    for x in range(n):
        a=np.random.randint(1,7,2)
        lista.append(np.sum(a))
    return lista
plt.hist(rzut(10000),bins=11)
plt.show()



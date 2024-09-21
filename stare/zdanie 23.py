import random
import matplotlib.pyplot as plt
def zdanie(a):
    lista=[]
    for x in range(a):
        suma = 0
        z=random.randint(1,6);
        b=random.randint(1,6);
        suma+=z+b
        lista.append(suma)
    print(lista)
    plt.hist(lista,bins=11)
    plt.show()
zdanie(10000)
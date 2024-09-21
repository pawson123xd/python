import  random
lista=[1,2,3,4,5,6,7,8]
while(True):
    x=random.choice(lista)
    y=random.choice(lista)
    if x==y:
        continue
    lista.remove(x)
    lista.remove(y)
    print(x, y)
    if len(lista)==0:
        break
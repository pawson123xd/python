lista=[1,2,3,4,5,6]
w=3
if w==1:
    lista1=[]
    for x in lista:
        lista2=[]
        lista2.append(x)
        lista1.append(lista2)
    print(lista1)
elif len(lista)%w==0:
    lista1=[]
    x=len(lista)
    element=0
    raz=[]
    for u in range(w):
        raz.append(lista[u])
        element+=1
    lista1.append(raz)
    while len(lista1)!=len(lista)//w:
        lista2 = []
        for x in range(element,element+w):
            lista2.append(lista[x])
        element+=w
        lista1.append(lista2)
    print(lista1)
else:
    print("nic")
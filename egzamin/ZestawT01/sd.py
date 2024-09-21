liczba=str(5697812389423984794814897548173478565893754209578354746747847846784668237592750277836727426151516546135718181817667546345656562777)
lista=list(liczba)
lista1=[]
for x in range(len(lista)):
    if x%3==0:
        lista1.append(lista[x])
lista2=[]
for x in range(len(lista1)):
    if int(lista1[x])%3==0:
        lista2.append(lista1[x])
w=int(0)
for x in range(len(lista2)):
    w+=int(lista2[x])
print(w)
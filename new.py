import math as m
def cg(n,a1=1,q=2):
    n=a1*pow(q,n-1)
    return n
def sprawdznie(lista):
    for x in range(len(lista)):
        if x == 0:
            continue
        if lista[x - 1] > lista[x]:
            if x == len(lista)-1:
                return 1
        else:
            return 0
def sotowanie():
    lista=[10,23,5,3,8,95,4,2,7,1]
    n = len(lista)
    while n > 1:
        zamien = False
        for l in range(0, n - 1):
            if lista[l] < lista[l + 1]:
                lista[l], lista[l + 1] = lista[l + 1], lista[l]
                zamien = True

        n -= 1
        if zamien == False: break

    return sprawdznie(lista)
def suma_kwatuów(* a):
    suma=0
    for x in range(len(a)):
        suma+=a[x]
    return suma
def kwargs(**dane):
    for key, value in dane.items():
        if value >40 and value<59:
            print("{} is {}".format(key,value))

def ile_wywołanie(wywoła):
    wywoła=wywoła+1
    if wywoła==20:
        print("funkcja wywoła się ",wywoła)
    else:
        ile_wywołanie(wywoła)
print(m.comb(7,2))
print(m.fabs(-3.4))
print(m.fsum([4,9,-2,33,11]))
print(m.gcd(60,24))
print(int(m.sqrt(5)))
print(pow(m.e,6))
print(m.log(5,2))
print(m.log(5,10))
print(m.log(6))
print(m.log(625,5))
print(m.asin(1/2))
print(m.tau/2)

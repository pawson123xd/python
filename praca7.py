week 3 task 1
def get_sum_of_digits(num):
    suma=0
    digits=list(num)
    for x in digits:
        suma+=int(x)
    return suma
print(get_sum_of_digits("1337"))
week 3 task 2
n=int(input())
m=int(input())
if n>m:
    print("piersza liczba jest wieksza od drugie")
else:
    while n<m:
        print(n)
        n+=1
week  3 task 3
for x in range(1,101):
    for z in range(1,101):
        if x+z==100:
            print('{},{}'.format(x,z))
week  3 task 4
n=10000
for i in range(1,n):
    if n%i==0:
        print(i)
week 3 task 5
x='12345'
z=''
libacz=len(x)
while libacz > 0:
    libacz -= 1
    z=z+x[libacz]
print(z)
week 4 task 1
A)lista=[x for x in range(0,21,2)]
B)a='ala ma kota'
a=a.split()
lista=[len(x) for x in a]
C )lista=[x for x in range(1,101) if x%3==0and x%5==0]
d  i e nie wiem jak zrobić
week 4 task 2
    random.seed(170231)
    array=[random.randrange(1,101) for i in range(200)]

1)
def sum(array): #suma elementow w tablicy
    result = 0
    for x in array:
        result +=x
    return result
2) bez funkcji
def minimalel(array): #minimalny element w tablicy
    result = array[0]
    for x in array:
        if result>x:
            result=x
    return result
2) z funkcji
def minimalell(array): #minimalny element w tablicy z wykorzystaniem funkcji
    return min(array)
3)bez funkcji
def maksymalna(array): #maksymalny element 
    result = array[0]
    for x in array:
        if result<x:
            result=x
    return result
3)z funkcji
def maksymalnawbudowana(array): #maksymalny element z wykorzystaniem
    return max(array)
4)
def medianalist(array): # wypisanie mediany z tablicy
print(statistics.median(randomlist))
5) bez  funkcji
def sorttable(array): #sortowanie tabeli (odpuscilbym) + wyswietelnie 20 pierwszych
    for x in range(0,len(array)-1):
        for k in range(0,len(array)-1):
            if(array[k]>array[k+1]):
                array[k],array[k+1]=array[k+1],array[k]
    for x in range(0,20):
        if(x<len(array)):
            print(array[x])
5) z funkcja 
def sorttable(array): 
import random
def zadanie4():
    array[0:1]=sorted( array[0:10])
    print(array)
zadanie4()
6)
def iloczyn(array): #iloczyn elemeentow w tablicy
    result = 1
    for x in array:
        result = x*result
    return result
7)
def checkdwucyfr(array): #wyswietlenie ilosci dwucyfrowych liczb z tablicy
    result = 0
    for x in array:
        if len(str(x))==2:
            result+=1
    return result
8)
def powtarzenie(array): #policzenie elementow w tablicy
    result = {} 
    for x in array:
        if x in result:
            result[x]=result[x]+1
        else:
            result[x]=1
    return result
9)
def powtarzanie2(array): #zadanie 9 (policzenie elementow + wyswietelenie jezeli tylko byly raz)
    result = {} 
    for x in array:
        if x in result:
            result[x]=result[x]+1
        else:
            result[x]=1
    for x in result:
        if result[x]==1:
            print(x)
10)
def powtarzanie3(array): #zadanie 10 (policzenie elementow + wyswietelenie jezeli tylko byly trzy razy)
    result = {} 
    for x in array:
        if x in result:
            result[x]=result[x]+1
        else:
            result[x]=1
    for x in result:
        if result[x]==3:
            print(x)
11)
def checkliczby(array): #zadanie 11
    for x in array:
        if x>27:
            print(x)
def main():

main()
week 5 task 1
def cg(n,a1=1,q=2):
    n=a1*pow(q,n-1)
    return n
week 5 task 2
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
week 5 task 3

def suma_kwatuów(* a):
    suma=0
    for x in range(len(a)):
        suma+=a[x]
    return suma
print(suma_kwatuów(4,5,78,9,0))
print(suma_kwatuów(10,2,8,8,1))
week 5 task 4
def kwargs(**dane):
    for key, value in dane.items():
        if value >40 and value<59:
            print("{} is {}".format(key,value))

def main():
    kwargs(Paweł=42,Michał=23,Daniel=12,Adam=47,Korol=63)
    kwargs(Piotr=42, Olek=55, Kasia=70, Andrzej=47, Wokulski=80)
main()
week 5 task 5
def ile_wywołanie(wywoła):
    wywoła=wywoła+1
    if wywoła==20:
        print("funkcja wywoła się ",wywoła)
    else:
        ile_wywołanie(wywoła)
wywoła=0
ile_wywołanie(wywoła)

import math
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





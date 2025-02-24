import math as m
import sys

import pakiet
from pakiet import *
a='ala mma kota i psa i homika'
b='bug'
d=int(2)
e=int(3)
f=float(23.5)
s=float(64.2)
#j=complex(2,3)
#g=complex(5,7)
#print(a)
#print(b)
#print(d)
#print(e)
#print(f)
##print(j)
#print(g)
dodawanie=d+e
odemowanie=e-d
mnożenie=d*e
dzielenie=e/d
potegowanied=d**e
reszta=d%e
#print(dodawanie)
#print(odemowanie)
#print(mnożenie)
##print(dzielenie)
#print(potegowanied)
#print(reszta)
#d+=1
#print(d)
#d-=1
#print(d)
#d*=1
#print(d)
##d/=1
##d**=1
#print(d)
#d%=1
#print(d)
#print(pow(m.e,10))
#print(pow(m.log(5+pow(m.sin(88),2)),1/6))
#print(m.ceil(4.80))
#print(m.floor(3.55))
imie='PAWEŁ'
#Nazwisko='MARZEC'
#print(imie.capitalize(),Nazwisko.capitalize() )
#piosenka='la la la la'
#print(piosenka.count('la'))
#print(imie[1],imie[-1])
#print(piosenka.split(' '))
#hex=2e23
#print('{},{},{}'.format(a,f,hex))
#lista=['sta wars','shrek','harry potter']
#lista1=[]
#lista.sort()
#print(lista)
#lista1.append(a.split(' '))
#print(lista1)
#przezwiska={'beczka':'krzysik kopczyniski','pawson':'paweł marzec','tuket':'piort marzec'}
#print(przezwiska['beczka'],przezwiska['pawson'],przezwiska['tuket'])
#liczby={'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7}
#print(liczby['I'],liczby['II'],liczby['V'],liczby['VII'])
#lista={'złoto':'gothic','bogowie':'god of war','bloki':'minecraft'}
#liczba=0
#for z in lista.keys():
#    liczba+=1
#for x  in lista.keys():
#    liczba+=1
#print(liczba)
#z=input('napisz coś')
#print(z.count(" "))
#k=int(sys.stdin.readline())
#z=int(sys.stdin.readline())
#sys.stdout.write(str(z*k))
#if 5==5:
#    print('jest równe')
#if 4!=5:
 #   print('są rózne')
#f 6>=5:
 #   print('jest wieksze lub równe')
#if k < 0:
#    k=-k
#print(k)
#for x in range(3):
#    print(z**x)
#lista=[]
#liczba=0
#while liczba <5:
 #   liczba+=1
 #   x=int(input())
 #   lista.append(x)
#print(lista)
#s=input()
#suma=0
#for x in range(len(s)):
 #   suma+=int(s[x])
#print(suma)
#for x in range(h):
   # sys.stdout.write('\n')
    #for z in range(x):
      #  sys.stdout.write('A')
#h = int(input())
#try:
 #   print(m.sqrt(h))
#except ValueError:
#   print('bład')
#h=input()
#try:
#   print(int(h))
#except ValueError:
 #  print('bład')
A=[1/x for x in range(1,10)]
B=[2**i for i in range(1,10)]
C=[x for x in B if x%4==0]
print(A)
print(B)
print(C)
lista={'złoto':'gothic','bogowie':'god of war','bloki':'minecraft'}
liczba1=0
liczba2=0
while liczba1<len(lista.keys()):
    liczba1+=1
while liczba2<len(lista.values()):
    liczba2+=1
print("{}".format(liczba1+liczba2))
def funkcja():
    a=int(input('podaj liczbe'))
    if a<0:
        print("funkcja jest malejąca")
    elif a==0:
        print("funkcja jest stała")
    else:
        print("funkcja  jest rosnąca")
def prosta():
    a = int(input('podaj liczbe '))
    a1 = int(input('podaj liczbe '))
    if a == a1:
        print("prosta jest równolegle")
    elif a*a1==-1:
        print("prosta jest prostopadłe")
    else:
        print("prosta nie jest prostopadłe ani równolegle")
#def pitagorat(a,b):
 #   c=m.sqrt(pow(a,2)+pow(b,2))
 #   print('twoja przeciprostapadła jest równa '+str(c))
def ciągu_arytmetycznego(a,r,ile):
    for x in range(ile):
        a+=r
    print(a)
def zad13():
    h=int(input('podaj wysokość od 3 do 9 '))
    for i in range(1,h):
        print(" " * (h - i), "O" * (2 * i-1))
    for i in range(h-2,-1,-1):
        print(" " * (h - i), "O" * (2 * i-1))

pakiet.dodawaanie(3,4,5,6)
pakiet.odjemowanie(5,6,2,1)
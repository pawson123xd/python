import math
def zadanie1():
 A=[x for x in range(10)]
 B=[2**i for i in range(10)]
 C=[x for x in B if x%4==0]
 print(A) 
 print(B) 
 print(C)
def zadanie2():
 a=int(input("podaj a do funkcji "))
 if a>0:
     print("funkcji jest rosnaca")
 elif a<0:
     print("funkcji jest malejąca")
 else :
     print("funkcji jest stała")
zadanie2()

import sys
h=int(input("podaj wysokość "))
for x in range(h): 
 for j in range(1+x): 
  sys.stdout.write("A") 
 sys.stdout.write("\n")

import sys
print("Proszę podać pierwszą liczbę") 
licz1 = input() 
try:
 wynik=int(licz1)
 print("Wynik= "+str(wynik)) 
except ValueError:
 print("prosiłem o liczbe")  
import math as m
import sys
print("Proszę podać pierwszą liczbę") 
licz1 = input() 
try:
 wynik=int(m.sqrt(licz1))
 print("Wynik= "+str(wynik)) 
except TypeError:
 print("nie ma piewiastka ujemnego")

import math as m
imie='paweł'
nazwisko='marzec'
tal='you are welcomes'
lista=[]
tal.split(" ")
lista.append(tal.split(" "))
print(lista) 

def pitagorac(a,b):
     c=pow((a**2+b**2),1/2)
     return c
print('podaj pierwszy bok do trojkąta')
a=int(input())
print('podaj drugi bok do trojkąta')
b=int(input())
print('twoja przeciwprostopadła jest równa '+str(pitagorac(a,b)))


def ciag(* liczby): 
 #jeżeli nie ma argumentów to 
     if len(liczby) == 0: 
         return 0.0
     else:
         suma = 1.0 
 #sumujemy elementy ciągu 
         for i in liczby: 
             suma *= i 
 #zwracamy wartość sumy 
         return suma 
#wywołanie gdy brak argumentów 
print(ciag()) 
#podajemy argumenty 
print(ciag(1,2,3,4,5,6,7,8)) 

def ciag(a,b): 
     if a==b:
         x="obie proste są równoległe"
         return x
     elif a*b==-1:
         x="obie proste są prostopadłe"
         return x
     else:
         x='obie  proste  nie są prostopadle ani równoległe'
         return x
#wywołanie gdy brak argumentów 
print('podaj liczbe a do prostej')
a=int(input())
print('podaj liczbe a do drugiej prostej')
b=int(input())
print(ciag(a,b))

x=input()
suma=0
for i in range(6):
     suma+=int(x[i])
     print(suma)

import sys 
print("Podaj jakiś tekst") 
s=int(sys.stdin.readline())
a=int(sys.stdin.readline()) #Wczytuje wiersz #Wczytuje wiersz 
sys.stdout.write(str(s*a)) 

lista=[]
liczba=1
while liczba!=0:
     print('podaj liczbe')
     x=int(input())
     lista.append(x)
     print('czy chcesz dodać coś do listy jeśli nie napiszy 0')
     if x==0:
         break
print(lista)
import sys
iloczy=1
liczba=int(input())
for i in range(1,liczba):
     sys.stdout.write('|'+str(i)+'|' )
     if i==25 or i==50 or i==75 or i==100:
          sys.stdout.write('\n')
     iloczy*=i
print('\n')
print(iloczy)

A=[x**-1 for x in range(1,11)]
print(A)
B=[2**i for i in range(1,11)]
print(B)
C=[x for x in B if x%4==0]
print(C)

def zadanie2(a1,r,ile):
     suma=0
     for a1 in range(ile):
         suma+=a1
         a1+=r 
     return suma
print(zadanie2(1,1,10))

import math
def liczby_zespolone(a):
     print('{}'.format(a))
def liczby_zespolone1(a):
     print('{}'.format(complex(0,a)))
def dodawanie_i_odjemowanie(a,b,c,d):
     x=complex(a,b)
     z=complex(c,d)
     print('{}+{} równa sie'.format(x,z))
     print('{}'.format(x+z))
dodawanie_i_odjemowanie(3,4,2,6)

import random
def zadanie1():
     ile=int(input('podaj liczby w losowanych które zostałną dodane do listy '))
     lista=[]
     random.seed()
     for x in range(ile):
        x=random.randint(0,1000)
        lista.append(x)
     print(lista)
     zadanie1()
zadanie1()

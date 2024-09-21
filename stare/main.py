import sys
from klasa import *
import math as w
import random
import statistics
def zadanie1():
    A=[1/x for x in range(1,11)]
    B=[2**i for i in range(11)]
    C=[x for x in B if x%4==0]
    print(A)
    print(B)
    print(C)
def zadanie2():
    lista={'ogrurki':'sztuki','banany':'kg','jagłaka':'sztuki'}
    lista1=[]
    proste={value: key for key, value in lista.items() if value=='sztuki'}
    lista1.append(proste)
    print(lista1)
def zadanie4():
    a=int(input('podaj a do funkcji '))
    if a < 0:
        print('funkcji jest malejoca')
    elif a==0:
        print('funkcji jest stała')
    else:
        print('funkcji jest rosnąca')
def zadanie5():
    a = int(input('podaj a do prostej '))
    a1 = int(input('podaj a do  drugiej prostej '))
    if a==a1:
        print('proste są równoległe')
    elif a*a1==-1:
        print('proste są prostopałem')
    else:
        print('proste nie są równoległe ani prostopałem')
def zadanie6(a,b):
    c=w.sqrt(a**2+b**2)
    print('twoja przeciprostopała {}'.format(c))
def zadanie7(a=1,r=1,ile=10):
    for x in range(ile):
        a+=r
        print(a)
def ciag(* liczby):
 #jeżeli nie ma argumentów to
    if len(liczby) == 0:
        return 0.0
    else:
        suma = 1.0
        for i in liczby:
          suma *= i
 #zwracamy wartość sumy
    return suma
def zadanieb1():
    a='piger'
    print(a)
    b='eddfg'
    print(b)
    x=int(23)
    print(x)
    z=int(64)
    print(z)
    o=float(23.4)
    print(o)
    c=float(2.4)
    print(c)
    d=complex(2,3)
    print('{}'.format(d))
    s=complex(6,8)
    print('{}'.format(s))
def zadanieb2(a,b):
    dodawanie=a+b
    odejmowanie=a-b
    mnożenie=a*b
    dzielenie=a/b
    reszta=a%b
    potega=a**b
    dzielenie_całkowite=a//b
    print(dodawanie)
    print(odejmowanie)
    print(mnożenie)
    print(dzielenie)
    print(dzielenie_całkowite)
    print(potega)
    print(reszta)
def zadanieb4():
    x=pow(w.e,10)
    z=pow(w.log(5+pow(w.sin(8),2)),1/6)
    a=w.ceil(4.80)
    d=w.floor(3.55)
    print(x)
    print(z)
    print(a)
    print(d)
def zadanieb5():
    i='PAWEŁ MARZEC'
    print(i.capitalize())
def zadanieb6():
    i='la la la la'
    print(i.count('la'))
def zadanieb7():
    i = 'PAWEŁ'
    print(i[0]+str(i[1])+str(i[-1]))
def zadanieb8():
    i='la la la la'
    print(i.split(' '))
def zadanieb9():
    i='ale'
    x=int(3)
    z=float(2.4)
    hex=0e16
    print('{},{},{},{}'.format(i,x,z,hex))
def zadanieb10():
    tableka=["a |0|30|45||60|90|"]
    tableka=["sina|0|1/2|sqrt(2)|"]
def zadanieb11():
    x='ala ma kota i psa i mysz'
    lista=[]
    lista.append( x.split(" "))
    print(lista)
def zadanieb12():
    lista={'orzeł':'szymon kocior','ryba':'Mateusz ryniski','tutek':'piort marzec'}
    print(lista['orzeł'])

def zadanieb13():
    lista1={}
    lista = {'orzeł': 'szymon kocior', 'ryba': 'Mateusz ryniski', 'tutek': 'piort marzec'}
    lista1=lista
    print(lista1)
def zadanieb14():
    lista = {'I': 1, 'II': 2, 'III': 3}
    print('{},{},{}'.format(lista['I'],lista['II'],lista['III']))
def zadaniea1():
    x=input('podaj')
    print(x.count(" "))
def zadaniea2():
    s=int(sys.stdin.readline())
    z=int(sys.stdin.readline())
    sys.stdout.write(str(s*z))
def zadaniea3():
    if 4==4:
        print('jest równe')
    if 4!=3:
        print(' nie jest równe')
    if 4>=4:
        print(' jest równe lub wieksze')
def zadaniea4():
    x=int(input('podaj liczbe '))
    if x<0:
        x=-x
    print(x)
def zadaniea5():
    a = int(input('podaj liczbe '))
    b = int(input('podaj liczbe '))
    c = int(input('podaj liczbe '))
    if a>c and a>b:
        if a<=10 and a>0:
            print('a jest najwieksze i należy do od 0 do 10')
        else:
            print('a jest najwieksze ale nie należy do od 0 do 10')
    elif b>a and b>c:
        if b<=10 and b>0:
            print('b jest najwieksze i należy do od 0 do 10')
        else:
            print('b jest najwieksze ale nie należy do od 0 do 10')
    elif c>a and c>b:
        if c<=10 and c>0:
            print('c jest najwieksze i należy do od 0 do 10')
        else:
            print('c jest najwieksze ale nie należy do od 0 do 10')
    else:
        print('dwie lub trzy  liczby są równe')
def zadaniea6():
    for x in range(0,100,5):
        print(x)
def zadaniea7():
    x=int(input('podaj liczbe petli '))
    for z in range(x):
        z=z**x
        print(z)
def zadanie10():
    random.seed()
    ile = int(input('podaj liczby w losowanych które zostałną dodane do listy '))
    lista = []
    for x in range(ile):
        x = random.randint(0, 1000)
        lista.append(x)
    print(lista)
    zadanie10()
def zadaniea8():
    liczba =0
    lista=[]
    while liczba < 5:
        x = int(input('podaj liczbe petli '))
        lista.append(x)
        liczba+=1
    print(lista)
def zadaniea10():
    try:
        licz1 = int(input())
        print("Wynik=  {}".format(w.sqrt(licz1)))
    except ValueError:  # nazwa błędu dzielenia przez zero
        print("bład")
def zadaniea11():
    try:
        licz1 = int(input())
        print("Wynik=  {}".format(licz1))
    except ValueError:  # nazwa błędu dzielenia przez zero
        print("bład")
def zadanie():
    x='12345432'
    z=''
    libacz=len(x)
    while libacz > 0:
        libacz -= 1
        z=z+x[libacz]

def zadanief():
    for x in range(1,101):
        for z in range(1,101):
            if x+z==100:
                print('{},{}'.format(x,z))
def zadanieB3():
    x='234'
    suma=0
    liczba=0
    while liczba < len(x):
        suma+=int(x[liczba])
        liczba+=1
    print(suma)
def zadanie2():
    x=input()
    libacz=0
    b=''
    c='k'
    d=3
    for libacz in range(len(x)):
        try:
            if d>0 and x[libacz]=='k'and x[libacz+1]=='a':
                sys.stdout.write(x[libacz].replace(c,b))
                d-=1
            else:
                sys.stdout.write(x[libacz])
        except IndexError:
            break
def zadanie3():
    n=10000
    for i in range(1,n):
        if n%i==0:
            print(i)
def zadanie4():
    random.seed(123456)
    randomlist=[random.randrange(1,101) for i in range(200)]
    suma=0
    iloczyn=1
    #for x in range(200):
     #   suma+=randomlist[x]
    #print(suma)
    #for x in range(200):
     #   randomlist[x]
    #print(min(randomlist))
   # for x in range(200):
    #    randomlist[x]
    #print(max(randomlist))
    #for x in range(200):
     #   randomlist[x]
    #print(statistics.median(randomlist))
    #for x in range(200):
     #   iloczyn*=randomlist[x]
    #słowki = {}
    #print(randomlist)
    #for j in range(0,200):
     #   z = 0
      #  for i in range(0, 200):
       #     if randomlist[j] == randomlist[i]:
        #        z += 1
        #        słowki[randomlist[j]] = z

#    print(słowki)
  #  for i in range(1,200):
   #     if randomlist[i]/10>1:
    #        print(randomlist[i])

def zadanie5():
    lista1=[]
    lista2=[]
    lista3=[]
    słownik={}
    a='ala'
    lista4=a.split(' ')
    lista2.append(a.split(" "))
    for x in range(len(a)+1):

        słownik[a]=x
    for x in range(20+1):
        if x%2==0:
            lista1.append(x)
    for x in range(1,100 + 1):
        if x % 3 == 0 and x%5==0:
            lista3.append(x)
    print(słownik)
def zadanie6():
    random.seed()
    for x in range(10):
        randomlist = [random.randrange(1, 6) for i in range(5)]
        if x%2==0:
            print(randomlist)
def zadanie7():
    random.seed()
    a=input('napisz liczby ')
    lista1=[]
    lista2 =[]
    for i in range(len(a)):
        lista1.append(a[i])
        lista2.append(a[i])
    for x in range(len(a)):
        if x<4:
            losowanie=random.sample(lista1,4)
            los = random.sample(lista2, 4)
    print(losowanie)
    print(los)
def ciąg(array):
    if len(array)%2==0:
        print("Podaj nieparzysta ilosc w ciagu")
        return 0
    elif len(array)<7:
        print("Podaj wiecej elementow ciagu")
        return 0
    min = int(array[0])
    max = int(array[len(array)//2])
    ilosclist = int(array[-1])
    iloscelementow = int(array[-3])
    result = []
    for x in range(0,ilosclist):
        data = []
        for k in range(0,iloscelementow):
            data.append(random.randrange(min,max))
        result.append(data)
    return result
def mani():
    inputuser = input("Podaj ciag: ")
    inputuser = inputuser.split(" ")
    try:
        print(ciąg(inputuser))
    except:
        print("Nieprawidłowy ciąg")
#print(ciąg_geometrycznymi(1,2,4))
#print(ciąg_arytmetycznymi(2,3,4)
def zad9(** rzeczy):
    for z in rzeczy:
        print(rzeczy[z])
        print(len(rzeczy[z]))
zad9(lista_kuputo=['mieso','słodycze','ryż','sól'], wartość=[12,34,5,12])
def mystery():
    result={
        'sanity':'hellow'}
    return result
print(mystery())

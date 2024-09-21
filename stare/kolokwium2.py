import random
from sad import *
def chenge(a,b,c,d):
    g=''
    for i in range(0,len(a)):
        if a[i]==b and d>0:
            a[i]=c
            d-=1
        g=g+a[i]+" "
    return g
def mani():
    a=input()
    b='olga'
    c='oliwa'
    d=3
    a=a.split(" ")
    print(chenge(a,b,c,d))
def losowanie(a):
    if int(len(a))<7:
        print('ciąg jest za mały')
    if int(len(a))%2==0:
        print('ciąg jest parzysty')
    result=[]
    ilośćlist=int(a[-1])
    ilośćelemetów=int(a[-3])
    min=int(a[0])
    max=int(a[len(a)//2])
    for x in range(0,ilośćlist):
        data=[]
        for z in range(0,ilośćelemetów):
            data.append(random.randrange(min,max))
        result.append(data)
    return result
def mani2():
    try:
        a=input()
        a=a.split(" ")
        print(losowanie(a))
    except:
        print('nie prawidłowy ciąg')
def mani3():
    print(zad4_1(140))
    print(zad4_2(90))
mani3()
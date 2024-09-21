import random
def changa1(a):
    g=''
    for x in range(len(a)):
        g=g+a[x]+" "
    return g
def changa(a,b,c,d):
    for i in  range(0,len(a)):
        if a[i]==b and d>0:
            a[i]=c
            d-=1
    return changa1(a)
def zad1():
    a=input()
    a=a.split(" ")
    b='ania'
    c='ola'
    d=3
    print(changa(a,b,c,d))
    return 0
def środkowanie(a):
    if len(a)%2==0:
        print('ciąg jest parzusty')
        return 0
    if len(a)<7:
        print('co najmniej 7')
        return 0
    result=[]
    min=int(a[0])
    max=int(a[len(a)//2])
    ilosć=int(a[-3])
    lista=int(a[-1])
    for i in range(lista):
        data=[]
        for z in range(ilosć):
            data.append(random.randrange(min,max))
        result.append(data)
    return result
def zad2():

    a=input()
    a=a.split(" ")
    print(środkowanie(a))
    return 0
zad2()


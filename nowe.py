def change(a):
    g=''
    slowki={}
    z=1
    for x in range(len(a)):
        if a[x-1]==a[x]:
            z+=1
            if x==len(a)-1:
                slowki[a[x]] = z
        elif a[x-1]!=a[x]:
            slowki[a[x-1]]=z
            z=1
        g=g+a[x]+" "
    print(slowki)
    return g
def mani(): #{'ala':3,'ma':1,'kota':1} ala ala ala ma kota
    a=input()
    a=a.split()
    print(change(a))
def odwrotność(a):
    liczba=len(a)
    g=""
    while liczba>0:
        liczba-=1
        g=g+a[liczba]+" "
    return g
def mani2(): #{'ala':3,'ma':1,'kota':1} ala ala ala ma kota
    a=input()
    a=a.split()
    print(odwrotność(a))
def licznie(a):
    słownnik={}
    pamieć=[]
    for x in range(len(a)):
        ile=0
        if a[x] in pamieć:
            continue
        else:
            for y in range(len(a)):
                if a[x]==a[y]:
                    ile+=1
        słownnik [a[x]]=ile
        pamieć.append(a[x])
    print(słownnik)
def mani3(): #{'ala':3,'ma':1,'kota':1} ala ala ala ma kota
    a="ala ala ala ma kota"
    a=a.split()
    licznie(a)
mani3()

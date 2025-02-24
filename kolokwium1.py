def zdani2(a):
    g=''
    for i in range(0,len(a)):
        g=g+a[i]+" "
    return g
def wyraz(a,b,c,d):
    a=a.split(" ")
    for i in range(0,len(a)):
        if a[i]==b and d>0:
            a[i]=c
            d-=1
    return zdani2(a)
def main():
    a=input()
    b = "kasia"
    c ="ania"
    d=3
    print(wyraz(a,b,c,d))
    return 0
def zadanie():
    x='12345'
    z=''
    libacz=len(x)
    while libacz > 0:
        libacz -= 1
        z=z+x[libacz]
    print(z)
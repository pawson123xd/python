def zamiania(a,b,c,d):
    g=""
    for i in range(len(a)):
        if a[i]==b and d>0:
            a[i]=c
            d-=1
        g=g+a[i]+""
    return g
def main():
    a=input()
    a=a.split(" ")
    b="oliwia"
    c="olga"
    d=3
    print(zamiania(a,b,c,d))
main()
def suma(a,n):
    lista=[]
    for x in range(n):
        suma = 0
        for j in range(n):
            suma+=int(a[j][x])
        lista.append(suma)
    w=lista[0]
    print(lista)
    for x in lista:
        if w<x:
            w=x
    print(w)
def macierz(n):
    a = [[0] * n for i in range(n)]
    for x in range(n):
        for j in range(n):
            print("podaj element")
            element=input()
            a[x][j]=element
    print(a)
    suma(a,n)
def main():
    while(True):
        print("podaj n")
        n=int(input())
        if n>10:
            print("bład Podaj jeszcze raz")
            continue
        break
    macierz(n)
main()
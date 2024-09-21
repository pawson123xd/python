def zamienie(a):
    lista=[]
    odwrocone=[]
    while True:
        if a==1:
            lista.append(1)
            break
        elif a % 2==1:
            lista.append(1)
        else:
            lista.append(0)
        a=a//2
    lista.reverse()
    for x in range(len(lista)):
        odwrocone.append(lista[x])
    print(odwrocone)
def obliczy(a):
    suma_bit=0
    w=len(a)
    a.reverse()
    for x in range(0,len(a)):
        if a[x]=='1':
            suma_bit+=2**x
    print(suma_bit)
def main():
    print("podaj opcje 1-oblicz bit , 2-zamienie_liczbe_na_bitnarna")
    select=int(input())
    if select==1:
        print("podaj bit")
        a=input()
        a=a.split(" ")
        obliczy(a)
    elif select==2:
        print("podaj liczbe")
        a=int(input())
        zamienie(a)
    else:
        print("bład")
main()
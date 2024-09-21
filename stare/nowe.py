def zad2(a):
    lista=[]
    if len(a)<5:
        print("za mało")
    else:
        for x in range(0,len(a)):
            if len(a[x])%2==0:
                continue
            else:
                lista.append(a[x])
        lista1 = []
        pamiec=[]
        for x in range(0,len(lista)):
            lista2=[]
            if lista[x][len(lista[x])//2] in pamiec:
                continue
            else:
                for j in range(0, len(lista)):
                    if lista[x][len(lista[x])//2]==lista[j][len(lista[j])//2]:
                        lista2.append(lista[j])
                    if j==len(lista)-1 and len(lista2)>=2:
                        lista1.append(lista2)
                pamiec.append(lista[x][len(lista[x])//2])
        print(lista1)

a="kajak kojak rower karton rotor motor tatry"
a=a.split(" ")
zad2(a)
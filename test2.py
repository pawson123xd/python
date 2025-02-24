def split(a,b):
    lista=[]
    pamiec=0
    for x in range(len(a)):
        g=""
        if a[x]==b:
            for y in range(pamiec,x):
                if a[y]==" ":
                    continue
                g+=a[y]
                pamiec+=1
            lista.append(g)
    return lista
a="ala ala ala ola adwazs asd asd asdf fdasasdf sdf  fsd ffds sd  gsdfgdf  fgsd df s dfvbcxv"
print(split(a," "))
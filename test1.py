def split(a,b):
    lista=[]
    w = 0
    raz=True
    for x in range(len(a)):
        g=""
        if a[x]==b and raz==True:
            for y in range(0,x):
                g+=a[y]
            w=x+1
            if len(g) == 0:
                raz = False
                continue
            lista.append(g)
            raz=False
        elif a[x]==b or x==len(a)-1:
            for y in range(w,x):
                g+=a[y]
            w=x+1
            if len(g)==0:
                continue
            if x == len(a) - 1 and a[x]!=" ":
                g+=a[x]
                lista.append(g)
            else:
                 lista.append(g)
    return lista
a="ala ala ala ola adwazs asd asd asdf fdasasdf sdf  fsd ffds sd  gsdfgdf  fgsd df s dfvbcxv"
print(split(a," "))

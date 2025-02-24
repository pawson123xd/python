def dijkstry(grand,start):
    wszystkie=[]
    for start in start:
        slownik={}
        for x in grand.keys():
            slownik[x]=0
        slownik[start]=0
        lista=[]
        lista.append([0,start])
        odwiedzone=[]
        while len(lista)!=0:
            przejcie=lista[0]
            for x in lista:
                if przejcie[0]>x[0]:
                    przejcie=x;
            lista.remove(przejcie)
            if przejcie[1] in odwiedzone:
                continue
            odwiedzone.append(przejcie[1])
            for x,y in grand[przejcie[1]].items():
                ruch=y+przejcie[0]
                if ruch<slownik[x] or slownik[x]==0 and x!=start:
                    slownik[x]=ruch
                lista.append([ruch,x])
        wszystkie.append(slownik)
    return wszystkie
def main():
    grand={
        "a":{"b":1,"c":4},
        "b": {"a": 1, "c": 2,"d":1},
        "c": {"a":4,"c": 6,"d":3},
        "d": {"b": 1, "c": 3},
    }
    start=[]
    for x in grand.keys():
        start.append(x)
    print(dijkstry(grand,start))
main()

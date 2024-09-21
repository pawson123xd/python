import random
def gra():
    los=random.randint(0,10)
    print(los)
    for x in range(1,9):
        print("podaj liczbe:",end='')
        odp=int(input())
        if(odp < los):
            print("za malo")
        elif (odp > los):
            print("za duzo")
        else:
            koniec="gratulacje udało ci sie zgadnocs odp: {} za proga {}".format(odp,x)
            return koniec
print(gra())
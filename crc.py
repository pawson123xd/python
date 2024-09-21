def crc3():
    caly_lista = []
    crc_3 = [1, 0, 1, 1]
    kod = [0,0,1, 0, 1, 1, 0, 1]
    zera=0
    for x in range(len(kod)):
        if kod[x]==0:
            zera+=1
        else:
            break
    kod.reverse()
    for x in range(zera):
        kod.pop()
    kod.reverse()
    for x in range(3):
        kod.append(0)
    lista=[0,0,0,0]
    for x in range(4):
        if kod[x]==crc_3[x]:
            lista[x] = 0
        else:
            lista[x] = 1
    for y in range(len(lista)):
        if lista[y] == 0:
            zera += 1
        else:
            break
    for y in range(len(lista)):
        if lista[y] == 0:
            zera += 1
        else:
            break
    for x in range(4,len(kod)):
        caly_lista.append(kod[x])
    petla=0
    while True:
        if lista[0]==0:
            lista.append(caly_lista[petla])
            petla+=1
            del lista[0]
        elif lista[0]==1:
                for x in range(4):
                    if lista[x] == crc_3[x]:
                        lista[x] = 0
                    else:
                        lista[x] = 1
                del lista[0]
                lista.append(caly_lista[petla])
                petla += 1
        if petla == len(caly_lista):
            if lista[0] == 0:
                del lista[0]
            elif lista[0] == 1:
                for x in range(4):
                    if lista[x] == crc_3[x]:
                        lista[x] = 0
                    else:
                        lista[x] = 1
                del lista[0]
            break
    print(lista)
crc3()
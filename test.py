crc_3=[1,0,1,1]
kod=[1,0,1,1,0,1,1]
"""kod=[1,1,0,1,1,0,1]"""
wynik=[]
zera=0
suma=4
for x in range(len(kod)):
    if kod[x]==0:
        zera+=1
    else:
        break
for x in range(zera):
    kod.pop(0)
for x in range(3):
    kod.append(0)
for x in range(4):
    if kod[x]==crc_3[x]:
        wynik.append(0)
    else:
        wynik.append(1)
for x in range(len(wynik),len(kod)):
    pamiec = suma
    zera1 = 0
    if suma==len(kod):
        print(wynik)
        break
    for y in range(len(wynik)):
        if wynik[y] == 0:
            zera1 += 1
        else:
            break
    for y in range(zera1):
            wynik.pop(0)
    if pamiec+zera1>len(kod):
        print("przekroczyło linit")
        break
    for y in range(pamiec,pamiec+zera1):
        wynik.append(kod[y])
        suma+=1
    for d in range(len(crc_3)):
        if wynik[d]==crc_3[d]:
            wynik[d]=0
        else:
            wynik[d]=1
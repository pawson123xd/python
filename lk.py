lista=[]
for x in range(1,100):
    ile=0
    for y in range(1,x):
        if x%y==0:
            ile+=1
    if ile<=1:
        lista.append(x)
print(lista)
a=['ala','ola','kacper','patryk','piort','andrzej']
result=[]
for i in range(len(a)):
    if a[i][-1]=='a':
        result.append(a[i])
n=int(input())
m=int(input())
if n>m:
    print("piersza liczba jest wieksza od drugie")
else:
    while n<m:
        print(n)
        n+=1
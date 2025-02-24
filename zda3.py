import random
def lista(a):
    result=[]
    if int(len(a))<7:
        print('za mało')
    if int(len(a))%2==0:
        print('ciąg jest niepażysty')
    ilośćelementó=int(a[-3])
    ilośćlist=int(a[-1])
    min=int(a[0])
    max=int(a[len(a)//2])
    for x in range(ilośćlist):
        data=[]
        for z in range(ilośćelementó):
            data.append(random.randrange(min,max))
        result.append(data)
    return result
def main():
    a=input()
    a=a.split(" ")
    print(lista(a))
main()
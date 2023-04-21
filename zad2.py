import random
def checkarray(a,str): #jezeli w tablicy jest podany string to zwroc 1 jezeli nie zwroc 0 np array=["test","dupa"] string="dupa" to zwroc 1
    for x in a:
        if x==str:
            return  1
    return 0
def sprawdzianie(i,a):
    result = []
    for x in a:
        if x[len(x)//2]==i and len(x)%2==1:
            result.append(x)
    return result
def zdanie2(a):
    sprawdzone = []
    result = []
    for i in a:
        if len(i)%2==0:
            continue
        else:
            if checkarray(sprawdzone,i[len(i)//2])==0:
                pom = sprawdzianie(i[len(i)//2],a)
                if len(pom)>1:
                    result.append(pom)
                sprawdzone.append(i[len(i)//2])
    return result
def main():
    a=input()
    a=a.split(" ")
    print(zdanie2(a))
def zadanie4():
    random.seed(123456)
    randomlist = [random.randrange(1, 101) for i in range(200)]
    słowki = {}
    print(randomlist)
    for j in range(0,200):
        z = 0
        for i in range(0, 200):
            if randomlist[j] == randomlist[i]:
                z += 1
                słowki[randomlist[j]] = z

    print(słowki)
zadanie4()

def zadanie3(a,b):
    g=""
    for x in a:
        if x==b:
            liczba=len(b)
            while liczba >0:
                liczba-=1
                g=g+b[liczba]
        else:
           g=g+x+" "
    print(g)
def main():
    a=input()
    b='pro'
    a=a.split()
    zadanie3(a,b)
main()
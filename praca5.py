def zad11():
    h=int(input('podaj wysokość od 3 do 9 '))
    for i in range(1,h):
        print(" " * (h - i), "O" * (2 * i-1))
    for i in range(h-2,-1,-1):
        print(" " * (h - i), "O" * (2 * i-1))
zad11()
def zad15():
 h=input()
 try:
  print(int(h))
 except ValueError:
  print('bład')
zad15()

 def ciag(* liczby): 
 #jeżeli nie ma argumentów to 
 if len(liczby) == 0: 
 return 0.0 
 else: 
 suma = 1.0 
 #sumujemy elementy ciągu 
 for i in liczby: 
 suma *= i 
 #zwracamy wartość sumy 
 return suma 
#wywołanie gdy brak argumentów 
print(ciag()) 
#podajemy argumenty 
print(ciag(1,2,3,4,5,6,7,8)) 
zad8()
def zad9(** rzeczy):
    for z in rzeczy:
        print(len(rzeczy[z]))
        print(rzeczy[z])
zad9(lista_kuputo=['mieso','słodycze','ryż','sól'], wartość=[12,34,5,12])
zad9()

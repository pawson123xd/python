def ciąg_arytmetycznymi(a,r,ile):
    print(a)
    for i in range(ile):
        a+=r
        print(a)
    print('koniec')
def ciąg_geometrycznymi(a,g,ile):
    print(a)
    for i in range(ile):
        a*=g
        print(a)
    print('koniec')
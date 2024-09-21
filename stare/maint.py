import numpy as np
def zdanie1():
    a=np.arange(0,22,2)
    print(a)
def zdanie2():
    lista=[2.5,3.6,1.2,8.9,3.4]
    a=np.array(lista,dtype='int64')
    print(a)
def zdanie3(n):
    a=np.arange(1,n*n)
    return a
def create_array(n):
    res=[]
    i=1
    while i<=n:
        res+=[i]
        i+=1
    return res
def zdanie4(a,b):
    a=np.logspace(1,b,num=b,base=a)
    print(a)
def zdanie5(a):
    j=np.arange(a,0,-1)
    print(j)
    matdiag=np.diag([x for x in j])
    print(matdiag)
def zdaniea1():
    a=np.arange(3)
    b=np.arange(3)
    z=a*b
    print(z)
def zdaniea2():
    a=np.array([[1,2,3],[5,12,2],[8,9,4]])
    b=np.array([[1,2,3,2],[4,5,12,2],[6,8,9,4],[5,3,2,1]])
    print(a)
    print(a.min(axis=0),a.min(axis=1))
    print(b.min(axis=0),b.min(axis=1))
def zdaniea3():
    a = np.arange(3)
    b = np.arange(3)
    print(a.dot(b))
def zdaniea4():
    a = np.arange(1,6)
    b = np.array([-3, -2, -1, 1 / 2, 7 / 5])
    print(a*b)
def zdaniea5():
    b=np.array([[1,2,3],[4,5,12]])
    a=np.sin(b)
    print(a)
def zdaniea6():
    a=np.array([[1,2,3],[4,5,12]])
    b=np.cos(a)
    print(b)
def dodawanie(b,a):
    print(b+a)
def zdaniea7():
    x=np.array([[1,2,3],[4,5,12]])
    a=np.sin(x)
    z=np.array([[1,2,3],[4,5,12]])
    b=np.cos(z)
    dodawanie(b,a)
def zdaniea8():
    b=np.arange(9).reshape(3,3)
    print(len(b))
    print(b)
    for x in range(len(b)):
        print(b[:,x])
        print()
def zdaniea9():
    b = np.arange(9).reshape(3, 3)
    for x in b:
        print(x)
    print(b.ravel())
def zdaniea10():
    c = np.array ([np.arange (9), np.arange (9), np.arange (9), np.arange (9), np.arange (9), np.arange (9), np.arange (9), np.arange (9), np.arange (9)])
    print(c)
    print(c.T)#Trasyt
    print(c.ravel())
def zdaniea11():
    b = np.arange(12).reshape(3, 4)
    print(b.ravel())
    print()
    w = np.arange(12).reshape(4, 3)
    print(w.ravel())
    print()
    q = np.arange(12).reshape(2, 6)
    print(q.ravel())


import random
def zadanie4():
    random.seed(170231)
    randomlist=[random.randrange(1,101) for i in range(200)]
    randomlist[0:1]=sorted( randomlist[0:10])
    print(randomlist)
def mystery():
    results = {
    'sanity': 'Hello'}
    return results
def create_array(n):
    res=[]
    i=1
    return res
print(create_array(3))
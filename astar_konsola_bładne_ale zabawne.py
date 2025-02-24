import heapq
import math
import subprocess
class node :
    def __init__(self,x,y,g=0.0,h=0.0,rodzic=None):
        self.x=x
        self.y=y
        self.g=float(g)
        self.h=float(h)
        self.rodzic=rodzic
    def __lt__(self, other):
        return (self.g+self.h)<(other.g+other.h)


def rysowanie_drogi(droga,grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            grid[x][y]=str(grid[x][y])
    grid[droga[0][1]][droga[0][0]]='S'
    grid[droga[-1][1]][droga[-1][0]]='M'
    for x in range(1,len(droga)-1):
        if droga[x-1][1]>droga[x][1] or droga[x-1][1]<droga[x][1]:
            grid[droga[x][1]][droga[x][0]]='|'
        else:
            grid[droga[x][1]][droga[x][0]]='-'
    for x in grid:
        print(x)
def losowanie_mapy():
    losowanie='map_generator.exe'
    subprocess.Popen(losowanie)
    print()
def wczytywanie_mapa():
    map=[]
    plik=open('grid.txt','rt')
    str = plik.read()
    plik.close()
    array = str.split("\n")
    for x in array:
        map.append(x.split(" "))
    for x in map:
        print(x)
    print()
    for x in range(len(map)):
        for k in range(len(map[x])):
            map[x][k] = int(map[x][k])
    return map
def szacowanie(obecna,meta):
    #return abs(obecna.x-meta.x)+abs(obecna.y-meta.y)
    return math.sqrt(pow((obecna.x-meta.x),2)+pow((obecna.y-meta.y),2))
def droga(obecna):
    sciezka=[]
    while obecna.rodzic!=None:
        sciezka.append([obecna.x,obecna.y])
        obecna = obecna.rodzic
    sciezka.append([obecna.x, obecna.y])
    sciezka.reverse()
    return sciezka


def astar(grid, start, meta):
    grid[start.y][start.x] = 0
    grid[meta.y][meta.x] = 0
    otwarta = []
    zamkniete = []
    start.h=szacowanie(start, meta)
    otwarta.append([[start.g + start.h],start])
    zamkniete.append([start.x,start.y])
    while len(otwarta) != 0:
        obecna=otwarta[0]
        for v in otwarta:
            if obecna[0]<=v[0]:
                obecna=v
        # z listy otwartej wybrać ostatnie minimalne oszacowanie, najlepiej listę (typ list)
        if obecna[1].y == meta.y and obecna[1].x == meta.x:
            return droga(obecna[1])
        lista = [[0,-1],[-1,0],[0,1],[1,0]]
        #lista = [[-1, 0], [0, -1], [1, 0], [0, 1]]
        for x in lista:
            koszt_Obecnej = obecna[1].g + 1.0
            ruch = node(obecna[1].x + x[0], obecna[1].y + x[1], koszt_Obecnej,szacowanie(node(obecna[1].x + x[0], obecna[1].y + x[1]), meta), obecna[1])
            if ruch.x < len(grid[0]) and 0 <= ruch.x  and ruch.y < len(grid) and  0 <= ruch.y and grid[ruch.x][ruch.y] == 0:
                sprawdzi=True
                for x in zamkniete:
                    if ruch.x==x[0] and ruch.y==x[1]:
                        sprawdzi=False
                if sprawdzi:
                    zamkniete.append([ruch.x, ruch.y])
                    otwarta.append([[ruch.g + ruch.h], ruch])
    return []
def main():
    start=node(0,0)
    meta=node(19,19)
    if start.x==meta.x and start.y==meta.y:
        print("start jest rowny mety")
        return None
    print("jesli chcesz zmienic mape napisz 1 jesli nie naciśnij enter")
    wybor=input()
    if wybor=='1':
        losowanie_mapy()
        print()
    grid=wczytywanie_mapa()
    road = astar(grid,start,meta)
    print(road)
    print(len(road))
    print()
    if len(road)!=0:
        rysowanie_drogi(road,grid)
    else:
        print("error not find way")
main()
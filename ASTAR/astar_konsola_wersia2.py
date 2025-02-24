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
    return round(math.sqrt(pow((obecna.x-meta.x),2)+pow((obecna.y-meta.y),2)),2)
    #return abs(obecna.x - meta.x+ obecna.y - meta.y)
def droga(obecna):
    sciezka=[]
    while obecna.rodzic!=None:
        sciezka.append((obecna.x,obecna.y))
        obecna = obecna.rodzic
    sciezka.append((obecna.x, obecna.y))
    sciezka.reverse()
    return sciezka


def astar(grid, start, meta):
    grid[start.x][start.y] = 0
    grid[meta.x][meta.y] = 0
    otwarta = []
    zamkniete = []
    start.h=szacowanie(start, meta)
    heapq.heappush(otwarta, (start.g + start.h, start))
    zamkniete.append((start.x,start.y))
    while len(otwarta) != 0:
        obecna = heapq.heappop(otwarta)
        if obecna[1].y == meta.y and obecna[1].x == meta.x:
            return droga(obecna[1])
        lista = [(0, 1), (0, -1),(1, 0), (-1, 0)]
        for x in lista:
            koszt_Obecnej = obecna[1].g + 1.0
            ruch = node(obecna[1].x + x[0], obecna[1].y + x[1], koszt_Obecnej,szacowanie(node(obecna[1].x + x[0], obecna[1].y + x[1]), meta), obecna[1])
            if 0 <= ruch.x < len(grid[0]) and 0 <= ruch.y < len(grid) and grid[ruch.y][ruch.x] == 0:
                sprawdzi=True
                for x in zamkniete:
                    if ruch.x==x[0] and ruch.y==x[1]:
                        sprawdzi=False
                if sprawdzi:
                    zamkniete.append((ruch.x, ruch.y))
                    heapq.heappush(otwarta, (ruch.g + ruch.h, ruch))
    return []
def main():
    start=node(0,0)
    meta=node(7,12)
    if start.x==meta.x and start.y==meta.y:
        print("start jest rowny mety")
        return None
    #print("jesli chcesz zmienic mape napisz 1 jesli nie naciśnij enter")
    #wybor=input()
    #if wybor=='1':
     #   losowanie_mapy()
      #  print()
    grid=wczytywanie_mapa()
    start.x=len(grid)-1-start.x
    x=start.x
    start.x=start.y
    start.y=x
    meta.x=len(grid[0])-1-meta.x
    x=meta.x
    meta.x=meta.y
    meta.y=x
    road = astar(grid,start,meta)
    print(road)
    print(len(road))
    print()
    if len(road)!=0:
        rysowanie_drogi(astar(grid,start,meta),grid)
    else:
        print("error not find way")
main()
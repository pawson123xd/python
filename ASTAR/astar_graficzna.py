import pygame
import sys
import math
import random
class node :
    def __init__(self,x=0,y=0,g=0.0,h=0.0,rodzic=None):
        self.x=x
        self.y=y
        self.g=float(g)
        self.h=float(h)
        self.rodzic=rodzic


# Inicjalizacja Pygame
pygame.init()

# Parametry planszy
GRID_SIZE = 20  # Rozmiar planszy (20x20 komórek)
CELL_SIZE = 30  # Rozmiar pojedynczej komórki w pikselach
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
SCREEN_COLOR = (255, 255, 255)  # Kolor tła (biały)
GRID_COLOR = (200, 200, 200)  # Kolor siatki (szary)
OBSTACLE_COLOR = (0, 0, 0)  # Kolor przeszkód (czarny)
START_COLOR = (0, 255, 0)  # Kolor punktu startowego (zielony)
END_COLOR = (255, 0, 0)  # Kolor punktu końcowego (czerwony)
TEXT_COLOR = (150, 100, 0)  # Kolor tekstu
droga_COLOR = (0, 0, 255)  # Kolor drogi (niebieski)
ruch_COLOR = (255, 255, 0)  # Kolor drogi (żółty)
wynik_COLOR=(124,0,120) # Kolor drogi (fioletowy)
odwiedzone_COLOR = (255, 153, 51) # Kolor drogi (pomaraniczowy)
trafinie_COLOR=(153,51,255)# jeśli narysowana droga jest rowne wynikowi

# Tworzenie okna
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Plansza do wizualizacji A*")

# Plansza
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
def szacowanie(obecna,meta):
    #return abs(obecna.x-meta.x)+abs(obecna.y-meta.y)
    return round(math.sqrt(pow((obecna.x-meta.x),2)+pow((obecna.y-meta.y),2)),2)
def droga(obecna,grid,start,meta):
    sciezka=[]
    while obecna.rodzic!=None:
        sciezka.append([obecna.y,obecna.x])
        obecna = obecna.rodzic
        if grid[obecna.x][obecna.y]==4:
            grid[obecna.x][obecna.y]=8
        else:
            grid[obecna.x][obecna.y]=6
        draw_grid()
        draw_text()  # Dodanie napisów w lewym górnym rogu
        pygame.display.flip()
    sciezka.append([obecna.y, obecna.x])
    sciezka.reverse()
    grid[start.x][start.y]=2
    grid[meta.x][meta.y]=3
    draw_grid()
    draw_text()  # Dodanie napisów w lewym górnym rogu
    pygame.display.flip()
    return sciezka


# Funkcja rysowania planszy
def draw_grid():
    screen.fill(SCREEN_COLOR)
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            cell_value = grid[row][col]
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if cell_value == 1:  # Przeszkoda
                pygame.draw.rect(screen, OBSTACLE_COLOR, rect)
            elif cell_value == 2:  # Start
                pygame.draw.rect(screen, START_COLOR, rect)
            elif cell_value == 3:  # Koniec
                pygame.draw.rect(screen, END_COLOR, rect)
            elif cell_value == 4:  # droga
                pygame.draw.rect(screen, droga_COLOR, rect)
            elif cell_value == 5:  # odwiedzone
                pygame.draw.rect(screen, ruch_COLOR, rect)
            elif cell_value == 6:  # wynik
                pygame.draw.rect(screen, wynik_COLOR, rect)
            elif cell_value == 7:  # ruch
                pygame.draw.rect(screen, odwiedzone_COLOR, rect)
            elif cell_value == 8:  # trafinie
                pygame.draw.rect(screen, trafinie_COLOR, rect)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)  # Siatka



# Funkcja rysowania napisów w lewym górnym rogu
def draw_text():
    font = pygame.font.Font(None, 20)
    obstacle_text = font.render('Klawisz 3'': dodawanie przeszkód', True, TEXT_COLOR)
    screen.blit(obstacle_text, (10, 10))  # Wyświetlanie opisu
    obstacle_text = font.render('Klawisz 4'': zaznaczanie swojej drogi', True, TEXT_COLOR)
    screen.blit(obstacle_text, (10, 40))  # Wyświetlanie opisu
    obstacle_text = font.render('Klawisz 5'': czyszczenie planszy', True, TEXT_COLOR)
    screen.blit(obstacle_text, (10, 70))  # Wyświetlanie opisu
    obstacle_text = font.render('Klawisz spacji'': zaczyna wyszukiwanie najkrótrzej drogi', True, TEXT_COLOR)
    screen.blit(obstacle_text, (10, 100))  # Wyświetlanie opisu
    obstacle_text = font.render('lewy przycisk myszy zaznacza punkty', True, TEXT_COLOR)
    screen.blit(obstacle_text, (10, 130))  # Wyświetlanie opisu
    obstacle_text = font.render('Prawy przycisk myszy usuwa zaznaczone punkty', True, TEXT_COLOR)
    screen.blit(obstacle_text, (10, 160))  # Wyświetlanie opisu
    obstacle_text = font.render('Jeśli nie zaznaczysz mety lub startu program zaznaczy losowe punkty', True, TEXT_COLOR)
    screen.blit(obstacle_text, (10, 190))  # Wyświetlanie opisu


# Funkcja do czyszczenia planszy
def clear_grid():
    global grid, start_set, end_set
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    start_set = False
    end_set = False
def tworzenie_mapy():
    start_set = False
    end_set = False
    # Flagi myszy
    mouse_down = False
    right_mouse_down = False
    # Główna pętla gry
    running = True
    blok = False
    wynik=[]
    clear_grid()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col, row = x // CELL_SIZE, y // CELL_SIZE
                if event.button == 1:  # Lewy przycisk myszy
                    mouse_down = True
                    if not start_set:
                        if grid[row][col] == 3:
                            end_set = False
                        grid[row][col] = 2  # Ustaw start
                        start = node(row, col)
                        start_set = True
                    elif not end_set:
                        if grid[row][col] == 2:
                            start_set = False
                        grid[row][col] = 3  # Ustaw koniec
                        meta = node(row, col)
                        end_set = True
                    else:
                        if grid[row][col] == 2:
                            start_set = False
                        if grid[row][col] == 3:
                            end_set = False
                        if blok == False:
                            grid[row][col] = 1  # Dodaj przeszkodę
                        if blok == True:
                            grid[row][col] = 4  # Dodaj drogi
                elif event.button == 3:  # Prawy przycisk myszy
                    right_mouse_down = True
                    if grid[row][col] == 2:
                        start_set = False
                    if grid[row][col] == 3:
                        end_set = False
                    grid[row][col] = 0  # Usuń przeszkodę
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_down = False
                elif event.button == 3:
                    right_mouse_down = False
            # Obsługa klawiatury
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_3:  # Klawisz '3' - dodawanie przeszkód
                    if blok == True:
                        blok = False
                    x, y = pygame.mouse.get_pos()
                    col, row = x // CELL_SIZE, y // CELL_SIZE
                elif event.key == pygame.K_5:  # Klawisz '5' - czyszczenie planszy
                    clear_grid()  # Czyści planszę
                    start_set = False
                    end_set = False

                elif event.key == pygame.K_4:  # Klawisz '4' - dodawanie drogi
                    if blok == False:
                        blok = True
                elif event.key == pygame.K_SPACE:
                    if not start_set:
                         losowanie=random.randint(0,GRID_SIZE-1)
                         losowanie1=random.randint(0,GRID_SIZE-1)
                         start = node(losowanie, losowanie1)
                         grid[losowanie][losowanie1] = 2
                    if not end_set:
                        losowanie = random.randint(0, GRID_SIZE - 1)
                        losowanie1 = random.randint(0, GRID_SIZE - 1)
                        while True:
                            if start.x==losowanie and start.y==losowanie1:
                                losowanie = random.randint(0, GRID_SIZE - 1)
                                losowanie1 = random.randint(0, GRID_SIZE - 1)
                                continue
                            break
                        meta = node(losowanie, losowanie1)
                        grid[losowanie][losowanie1] = 3
                    wynik.append(start)
                    wynik.append(meta)
                    return wynik
            # Rysowanie podczas przytrzymywania myszy
            if mouse_down:
                x, y = pygame.mouse.get_pos()
                col, row = x // CELL_SIZE, y // CELL_SIZE
                if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE and grid[row][col] == 0:
                    if blok == False:
                        grid[row][col] = 1  # Dodaj przeszkodę
                    elif blok == True:
                        grid[row][col] = 4  # Dodaj droge
            if right_mouse_down:
                x, y = pygame.mouse.get_pos()
                col, row = x // CELL_SIZE, y // CELL_SIZE
                if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE and grid[row][col] != 2 and grid[row][col] != 3:
                    grid[row][col] = 0  # Usuń przeszkodę
            # Rysowanie planszy i tekstów
            draw_grid()
            draw_text()  # Dodanie napisów w lewym górnym rogu
            pygame.display.flip()
def astar(grid, start, meta):
    otwarta = []
    zamkniete = []
    start.h=szacowanie(start, meta)
    otwarta.append([[start.g + start.h],start])
    zamkniete.append([start.x,start.y])
    while len(otwarta) != 0:
        obecna=otwarta[0]
        for v in otwarta:
            if obecna[0]>=v[0]:
                obecna=v
        otwarta.remove(obecna)
        if obecna[1].y == meta.y and obecna[1].x == meta.x:
            return droga(obecna[1],grid,start,meta)
        if obecna[1].y == start.y and obecna[1].x == start.x or grid[obecna[1].x][obecna[1].y]==4:
            None
        else:
            grid[obecna[1].x][obecna[1].y]=7
        lista = [[-1,0],[0,-1],[1,0],[0,1]]
        for x in lista:
            koszt_Obecnej = obecna[1].g + 1.0
            ruch = node(obecna[1].x + x[0], obecna[1].y + x[1], koszt_Obecnej,szacowanie(node(obecna[1].x + x[0], obecna[1].y + x[1]), meta), obecna[1])
            if ruch.x < len(grid[0]) and 0 <= ruch.x  and ruch.y < len(grid) and  0 <= ruch.y and grid[ruch.x][ruch.y] != 1 and grid[ruch.x][ruch.y] != 2:
                if grid[ruch.x][ruch.y]==4 or grid[ruch.x][ruch.y]==3 or grid[ruch.x][ruch.y]==7:
                    None
                else:
                    grid[ruch.x][ruch.y]=5
                sprawdzi=True
                for x in zamkniete:
                    if ruch.x==x[0] and ruch.y==x[1]:
                        sprawdzi=False
                if sprawdzi:
                    zamkniete.append([ruch.x, ruch.y])
                    otwarta.append([[ruch.g + ruch.h], ruch])
                    draw_grid()
                    draw_text()  # Dodanie napisów w lewym górnym rogu
                    pygame.display.flip()
    return []
def main(grid,mapa):
    road = astar(grid,mapa[0],mapa[1])
    for x in range(0,len(road)):
        road[x][1]=len(grid[0])-road[x][1]
    print(len(road))
    if len(road)!=0:
        print(road)
    else:
        print("error not find way")
    while True :
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_5:  # Klawisz '5' - czyszczenie planszy
                    return None
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
while True:
    mapa = tworzenie_mapy()
    main(grid,mapa)
pygame.quit()
sys.exit()
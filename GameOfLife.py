import pygame
import numpy as np

RESOLUTION = 10
WIDTH = 500
HEIGHT = 900
COLS = int(WIDTH/RESOLUTION)
ROWS = int(HEIGHT/RESOLUTION)
black = (0, 0, 0)
white = (255, 255, 255)
    
def setup():
    #setup Pygame screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill([255, 255, 255])
    pygame.display.set_caption('Conrads Game of Life')
    pygame.display.flip()
    gameLoop(screen)

def makeRandom2DArray():
    a = np.random.randint(2, size=(COLS, ROWS), dtype=np.int32)
    return a

def gameLoop(screen):
    cells = makeRandom2DArray()
    running = True
    while running:
        clockobject = pygame.time.Clock()
        clockobject.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        cells = updateCells(cells)
        drawScreen(screen, cells)
        pygame.display.update()
        


def updateCells(cells):
    nextArray = cells
    for i in range(COLS):
        for j in range(ROWS):
            numNeighbors = countNeighbors(cells, i, j)
            state = cells[i, j]

            if state == 0 and numNeighbors == 3:
                nextArray[i, j] = 1
            elif state == 1 and numNeighbors < 2 or numNeighbors > 3:
                nextArray[i, j] = 0
            else:
                nextArray[i, j] = state

    return nextArray


def countNeighbors(cells, i, j):
    sum = 0
    for x in range(-1,2):
        for y in range(-1,2):
            col = (i + x + COLS) % COLS
            row = (j + y + ROWS) % ROWS
            
            sum += cells[col, row]

    sum -= cells[x, y]
    return sum

def drawScreen(screen, cells):
    for col in range(COLS):
        for row in range(ROWS):
            state = cells[col, row]
            if state == 1:
                pygame.draw.rect(screen, black, (col*RESOLUTION, row*RESOLUTION, RESOLUTION-1, RESOLUTION-1))
            elif state == 0:
                pygame.draw.rect(screen, white, (col*RESOLUTION, row*RESOLUTION, RESOLUTION-1, RESOLUTION-1))

setup()
import pygame
import numpy as np
import constant as con


def initializePygame():
    global screen
    screen = pygame.display.set_mode((con.WIDTH, con.HEIGHT))
    screen.fill(con.WHITE)
    pygame.display.set_caption('Conrads Game of Life')
    pygame.display.flip()


def makeRandom2DArray():
    return np.random.randint(2, size=(con.COLS, con.ROWS))


def makeEmpty2DArray():
    return np.empty((con.COLS, con.ROWS), int)


def gameLoop():
    grid = makeRandom2DArray()
    renderGrid(grid)
    running = True
    pygame.display.update()
    while running:
        #clockobject = pygame.time.Clock()
        #clockobject.tick(30)
        grid = updateGrid(grid)
        renderGrid(grid)
        pygame.display.update()

        #Check to see if user closes game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        

def renderGrid(currentGrid):
    for i in range(con.COLS):
        for j in range(con.ROWS):
            if currentGrid[i, j] == 1:
                pygame.draw.rect(screen, con.BLACK, (i*con.RES, j*con.RES, con.RES-1, con.RES-1))
            elif currentGrid[i, j] == 0:
                pygame.draw.rect(screen, con.WHITE, (i*con.RES, j*con.RES, con.RES-1, con.RES-1))


def updateGrid(currentGrid):
    tempGrid = makeEmpty2DArray()
    for i in range(con.COLS):
        for j in range(con.ROWS):
            state = currentGrid[i, j]
            sum = countNeighbors(currentGrid, i, j)
            tempGrid[i][j] = currentGrid[i, j]
            if state == 0 and sum == 3:
                tempGrid[i, j] = 1
            elif state == 1 and sum < 2 or sum > 3:
                tempGrid[i, j] = 0
    return tempGrid        


def countNeighbors(grid, x, y):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            col = (x + i + con.COLS) % con.COLS
            row = (y + j + con.ROWS) % con.ROWS
            sum = sum + grid[col, row]
    sum = sum - grid[x, y]
    return sum

def run():
    initializePygame()
    gameLoop()

run()

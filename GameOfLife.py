import pygame
import numpy as np

RESOLUTION = 10
WIDTH = 2000
HEIGHT = 1000

def make2DArray(cols, rows):
    a = np.random.randint(2, size=(cols, rows), dtype=np.int32)
    return a

def initializeScreen(screen):
    cols = WIDTH//RESOLUTION
    rows = HEIGHT//RESOLUTION
    black = (0, 0, 0)
    white = (255, 255, 255)
    
    cells = make2DArray(cols, rows)
    for col in range(cols):
        for row in range(rows):
            value = cells[col, row]
            if value == 1:
                pygame.draw.rect(screen, black, (col*RESOLUTION, row*RESOLUTION, RESOLUTION, RESOLUTION))
            else:
                pygame.draw.rect(screen, white, (col*RESOLUTION, row*RESOLUTION, RESOLUTION, RESOLUTION))

def gameLoop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
   
        pygame.display.update()

def setupScreen():
    #setup Pygame screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill([255, 255, 255])
    pygame.display.set_caption('Conrads Game of Life')
    pygame.display.flip()
    
    #Draw Initial State
    initializeScreen(screen)
    return screen

def main():
    screen = setupScreen()
    gameLoop()

main()
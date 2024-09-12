"""
Author: Braz Amorim Campos
Septemper 11, 2024

Project:
Make a falling sand simulator, where when the user clicks on the game window,
a sand particle is created and falls to the bottom of the screen 

1 - Start with a black screen
2 - If the player clicks on a pixel, create a sandgrain in that pixel position
    2.1 - Gets the posisition on the game screen where the mouse was clicked
    2.2 - Create a sand grain and position him in the 2.1 position
    2.3 - Update the grainMtx that holds all sand grains positions
3 - Make the sandGrain fall until hit the end of screen or another grain
    3.1 - While there is no sand under or if still have screen pixels under:
        move the sand grain center 1px down (let the grain without cuts on the screen)
4 - Make the previous grains stay on the screen when new ones appear (ISSUE n1)
    4.1 - Make use of the grainMtx memory feature
        Search in the grainMtx for grains, retrieve their positions and draw then (do that in all repetitions)
"""
import pygame

def gridMaker(screen, rows, columns, resolution):
    #Creating the grid
    lineDistance = resolution // rows
    x, y = [0,0]
    for i in range(columns):
        x += lineDistance
        y += lineDistance
        pygame.draw.line(screen, "gray", (x, 0), (x, resolution))
        pygame.draw.line(screen, "gray", (0, y), (resolution, y))
        
def makeMtx(rows):
    return [[0]*rows for _ in range(rows)]

def gridDrawer(mtx, sandSize, surface):
    pygame.time.delay(25)
    surface.fill("black")   
    for l in range(len(mtx)):
        for c in range(len(mtx)):
            if mtx[l][c] == 1:
                sand = pygame.Rect(0, 0, sandSize, sandSize)
                sand.centerx = (c * sandSize) - (sandSize//2)
                sand.centery = (l * sandSize) - (sandSize//2)
                pygame.draw.rect(surface, "white", sand)
    pygame.display.flip()

def gridUpdater(mtx):
    #Update por cópia
    copyMtx = mtx
    #Iterando coluna da esquerda pra direita
    for c in range(len(mtx)):
        #Iterando linha de baixo para cima, pra não re-arrastar o 1
        for l in range(len(mtx) - 1, -1, -1):
            if mtx[l][c] == 1:
                if (l + 1) < len(mtx) and mtx[l+1][c] == 0:
                    copyMtx[l+1][c] = 1
                    copyMtx[l][c] = 0
                else:
                    copyMtx[l][c] = 1   
    return copyMtx

def addSandToMtx(mtx, mousex, mousey, sandSize):
    secaox = mousex // sandSize
    secaoy = mousey // sandSize
    mtx[secaoy][secaox] = 1
    return mtx

def main():
    windowResolution = 400
    rows, columns = [200, 200]
    sandSize = windowResolution // rows

    pygame.init()
    screen = pygame.display.set_mode((windowResolution, windowResolution))
    pygame.display.set_caption('Sand game!')

    gridMaker(screen, rows, columns, windowResolution)
    mtx = makeMtx(rows)
    mtx[23][12] = 1
    mtx[37][20] = 1

    #Game loop ----------------------------------------------------------
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False   

        #Cadastrar grão de areia na mtx
        #Get the mouse button that was pressed
        mouse_state = pygame.mouse.get_pressed(num_buttons=3)
        
        #If the left-mouse was clicked, add sand to mtx:
        if mouse_state[0]:
            #Get the position where the mouse was pressed
            mouseCoord = pygame.mouse.get_pos()
            mtx = addSandToMtx(mtx, mouseCoord[0], mouseCoord[1], sandSize)

        #Atualizar grid
        mtx = gridUpdater(mtx)
        #Desenhar grid
        gridDrawer(mtx, sandSize, screen)
        
        
        
    pygame.quit()
    

if __name__ == "__main__":
    main()
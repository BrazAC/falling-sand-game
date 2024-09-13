"""
Author: Braz Amorim Campos
Septemper 12, 2024

Project:
Make a falling sand simulator, where when the user clicks on the game window,
a sand particle is created and falls to the bottom of the screen 

- v2 version
Code more organized, implementing "menu" and pause
"""
import pygame
import random

def gridMaker(screen, rows, columns, resolution): #Desenha o grid na tela
    #Creating the grid
    lineDistance = resolution // rows
    x, y = [0,0]
    for i in range(columns):
        x += lineDistance
        y += lineDistance
        pygame.draw.line(screen, "gray", (x, 0), (x, resolution))
        pygame.draw.line(screen, "gray", (0, y), (resolution, y))
        
def makeMtx(rows):  #Cria uma matriz de mesma dimensão que o grid
    return [[0]*rows for _ in range(rows)]

def addSandToMtx(mtx, mousex, mousey, sandSize): #Cadastra 1 na mtx de acordo com a posição clicada pelo usuario na tela
    secaox = mousex // sandSize
    secaoy = mousey // sandSize
    mtx[secaoy][secaox] = 1
    return mtx

def gridUpdater(mtx):               #Move os 1's da mtx até a última linha (faz a areia cair)
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

def gridDrawer(mtx, sandSize, surface): #Desenha areia de acordo com 1's de mtx (desenha a areia)
    pygame.time.delay(fallingSpeed)
    surface.fill(backgroundColor)   
    for l in range(len(mtx)):
        for c in range(len(mtx)):
            if mtx[l][c] == 1:
                sand = pygame.Rect(0, 0, sandSize, sandSize)
                sand.centerx = (c * sandSize) - (sandSize//2)
                sand.centery = (l * sandSize) - (sandSize//2)
                pygame.draw.rect(surface, "white", sand)
    pygame.display.flip()

def starterMenu(sandSize, screen):
    mtxM = makeMtx(rows)
    begin = False
    while not begin:
        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 or event.button == 2 or event.button == 3:
                        begin = True
        #----------------------------------->Cadastrar grão de areia na mtx
        secaox = random.randint(0, rows - 1)
        secaoy = random.randint(0, rows - 1)
        mtxM[secaoy][secaox] = 1
        #------------------------------------------->Atualizar grid (matriz)
        mtxM = gridUpdater(mtxM)

        #----------------------------------------------------->Desenhar grid
        gridDrawer(mtxM, sandSize, screen)
    
def main():
    #IMPORTANT variables
    global fallingSpeed
    fallingSpeed = 25
    global backgroundColor
    backgroundColor = "black"
    windowResolution = 1000
    global rows
    rows, columns = [250, 250]
    sandSize = windowResolution // rows

    pygame.init()
    screen = pygame.display.set_mode((windowResolution, windowResolution))
    pygame.display.set_caption('Sand game!')

    starterMenu(sandSize, screen)
    mtx = makeMtx(rows)


    #Game loop ----------------------------------------------------------
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        starterMenu(sandSize, screen)
               

        #----------------------------------->Cadastrar grão de areia na mtx
        #Get the mouse button that was pressed
        mouse_state = pygame.mouse.get_pressed(num_buttons=3)
        #If the left-mouse was clicked, add sand to mtx:
        if mouse_state[0]:
            #Get the position where the mouse was pressed
            mouseCoord = pygame.mouse.get_pos()
            mtx = addSandToMtx(mtx, mouseCoord[0], mouseCoord[1], sandSize)
        #If middle-mouse was clicked, clear the sand
        elif mouse_state[1]:
            mtx = makeMtx(rows)
        
        #------------------------------------------->Atualizar grid (matriz)
        mtx = gridUpdater(mtx)

        #----------------------------------------------------->Desenhar grid
        gridDrawer(mtx, sandSize, screen)
    pygame.quit()
    
if __name__ == "__main__":
    main()
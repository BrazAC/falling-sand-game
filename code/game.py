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

#We are be using pygame fot this project
import pygame

#Setting some global variables
screenWidth = 400
screenHeight = 400
sandGrainWidth = 10
sandGrainHeight = 10

#Creating the matrix to store the sandGrains position
sandMtx = [[0]*screenWidth for _ in range(screenHeight)]

#Pygame setup
pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
running = True

#Start with a black screen
screen.fill("black")

#game loop
while running:
    #Close game when x button (window) is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   

    #Get the mouse button that was pressed
    mouse_state = pygame.mouse.get_pressed(num_buttons=3)
    
    #If the left-mouse was clicked, draw the sandGrain in that position
    if mouse_state[0]:
        #Get the position where the mouse was pressed
        mousePosition = pygame.mouse.get_pos()

        #Update the sandMtx (add the grain to mtx)
        sandMtx[mousePosition[1]][mousePosition[0]] = 1
        sandGrain = pygame.Rect(mousePosition[0], mousePosition[1], sandGrainWidth, sandGrainHeight)
        

        #Make the grain fall
        fall = True
        newYposition = mousePosition[1] + 1
        while fall:
            #If there is screen below
            if newYposition < screenHeight - (sandGrainHeight)//2:
                    #if there is no sand grains below
                    #y = linha, x = coluna
                    if sandMtx[newYposition][mousePosition[1]] == 0:

                        #Update the sandMtx
                        sandMtx[newYposition][mousePosition[0]] = 1
                        sandMtx[newYposition - 1][mousePosition[0]] = 0
                        
                        #"Clear" the screen, wait, update grain position, drawn grain in the new position
                        screen.fill("black")
                        pygame.time.delay(5)
                        newYposition += 1
                        sandGrain.centery = newYposition
                        pygame.draw.rect(screen, "white", sandGrain)
                        pygame.display.flip()
                    else:
                        fall = False
            else:
                fall = False
    #if the scroll-mouse was clicked, "clear" the screen sandGrains 
    elif mouse_state[1]:
        screen.fill("black")
    

    

    #Update the screen
    pygame.display.flip()

pygame.quit()

for l in range(len(sandMtx)):
    print(sandMtx[l])
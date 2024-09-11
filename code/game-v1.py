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

def gridInit(gridResolution, sandResolution):
    #Creating the grid
    grid = pygame.display.set_mode((gridResolution, gridResolution))
    

def main():
    pygame.init()

    gridResolution = 400
    sandResolution = 10
    rows, columns = [40, 40]

    gridInit(gridResolution, sandResolution)

    #Game loop
    running = True
    while running:
        #Close game when x button (window) is pressed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False   

        #Update the screen
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
import pygame
from constants import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Game Loop
    while True:
        # check for quit vent
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        # Fill Screen with Black Color
        screen.fill((0,0,0))

        # Update the display
        pygame.display.update()



if __name__ == '__main__':
    main()
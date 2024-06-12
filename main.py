# todo :
# [x] board squares stay square with window reSIZE
#    [x] FONT SIZE is adjusted based on board SIZE 
# [x] board is centered with the screen
# [ ] refactor code
#   [x] create seperate files for board generation and main()
# [ ] implement FEN function
# [ ] draw pieces to screen based on FEN string
# [ ] chess rules (piece movement)

import pygame
import cboard as c

# pygame setup
pygame.init()
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

def main():

    # local variable declarations
    running = True
    flag = 0

    while running:
        # when x clicked, close the program
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                c.board(screen)
        
        # print board to screen
        if flag != 1:
            c.board(screen)
            flag = 1

    pygame.quit()


if main() == __name__:
    main()

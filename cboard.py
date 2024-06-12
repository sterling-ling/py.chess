import pygame

def board(screen):
    # get the screen SIZE
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()

    SIZE = (SCREEN_WIDTH + SCREEN_HEIGHT) // 22 
    FONT = pygame.font.SysFont(None, (SIZE//3))
    RANK_NUMBER = 8
    FILE_LETTER = "a"

    # wipe previous screen
    screen.fill("black")

    # get grid SIZE
    GRID_WIDTH = SIZE * 8
    GRID_HEIGHT = SIZE * 8

    # calculate startx and start y
    startx = (SCREEN_WIDTH - GRID_WIDTH) // 2
    starty = (SCREEN_HEIGHT - GRID_HEIGHT) // 2

    for x in range(8):
        for y in range(8):
            # color checkerboard pattern
            if (y+x) % 2 != 0:
                color = "darkgreen"
                textc = "#faf0e6"
            else:
                color = "#faf0e6"
                textc = "darkgreen"

            rectx = (startx // 5) + x * SIZE
            recty = starty + y * SIZE

            pygame.draw.rect(screen, color, pygame.Rect(rectx,recty,SIZE,SIZE))

            if x == 0:
               # draw rank
               rank = FONT.render(str(RANK_NUMBER), True, textc, color)
               RANK_NUMBER = RANK_NUMBER - 1
               screen.blit(rank,(rectx,recty))
            if  y == 7:      
               # draw file
               FILE = FONT.render(FILE_LETTER, True, textc, color)
               FILE_LETTER = chr(ord(FILE_LETTER)+1)
               screen.blit(FILE, (rectx + (SIZE*0.875),recty + (SIZE*0.7575)))

    pygame.display.flip()

class Piece:
    def __init__(self, 

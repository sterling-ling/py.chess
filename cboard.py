# todo :
# [ ] board squares stay square with window resize
#    [x] font size is adjusted based on board size 
# [x] board is centered with the screen
# [ ] refactor code
#   [ ] create seperate files for board generation and __main__
# [ ] implement FEN function
# [ ] draw pieces to screen based on FEN string
# [ ] chess rules (piece movement)

import pygame

# pygame setup
pygame.init()
screenWidth = 1080
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))
running = True
flag = 0

def board():
    size = 80
    font = pygame.font.SysFont(None, (size//3))
    rankNo = 8
    fileLt = "a"

    # get the screen size
    screenWidth, screenHeight = screen.get_size()

    # get grid size
    gridWidth = size * 8
    gridHeight = size * 8

    # calculate startx and start y
    startx = (screenWidth - gridWidth) // 2
    starty = (screenHeight - gridHeight) // 2

    for x in range(8):
        for y in range(8):
            # color checkerboard pattern
            if (y+x) % 2 != 0:
                color = "darkgreen"
                textc = "#faf0e6"
            else:
                color = "#faf0e6"
                textc = "darkgreen"

            rectx = startx + x * size
            recty = starty + y * size

            pygame.draw.rect(screen, color, pygame.Rect(rectx,recty,size,size))

            if x == 0:
               # draw rank
               rank = font.render(str(rankNo), True, textc, color)
               rankNo = rankNo - 1
               screen.blit(rank,(rectx,recty))
            if  y == 7:      
               # draw file
               ffile = font.render(fileLt, True, textc, color)
               fileLt = chr(ord(fileLt)+1)
               screen.blit(ffile, (rectx + (size*0.875),recty + (size*0.7575)))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked x to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with x color to wipe away anything from last frame
    if flag == 0:
        board()
        pygame.display.flip()
        flag = 1


    # flip() the display to put your work on screen

pygame.quit()
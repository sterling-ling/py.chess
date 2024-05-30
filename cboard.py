# Example file showing x circle moving on screen
import pygame

# pygame setup
pygame.init()
screenWidth = 1080
screenHeight = 720
screen = pygame.display.set_mode((screenWidth, screenHeight))
running = True
flag = 0

def board():
    size = 60
    font = pygame.font.SysFont(None, 20)
    rankNo = 8
    fileLt = "a"

    for x in range(8):
        for y in range(8):
            # color checkerboard pattern
            if (y+x) % 2 != 0:
                color = "darkgreen"
                textc = "#faf0e6"
            else:
                color = "#faf0e6"
                textc = "darkgreen"

            pygame.draw.rect(screen, color, pygame.Rect(y*size,x*size,size,size))

            if y == 0:
               # draw rank
               rank = font.render(str(rankNo), True, textc, color)
               rankNo = rankNo - 1
               screen.blit(rank,(y,x*size))
            if  x == 7:      
               # draw file
               ffile = font.render(fileLt, True, textc, color)
               fileLt = chr(ord(fileLt)+1)
               screen.blit(ffile, (size*y+50,size*x+45))

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



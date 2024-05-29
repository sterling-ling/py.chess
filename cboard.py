# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((480, 480))
running = True
l = 0

def board():
    size = 60
    font = pygame.font.SysFont(None, 16)
    rankNo = 8
    fileLt = "a"

    for x in range(8):
        for y in range(8):
            # color checkerboard pattern
            if (x+y) % 2 != 0:
                color = "darkgreen"
            else:
                color = "#faf0e6"
            pygame.draw.rect(screen, color, pygame.Rect(x*size,y*size,size,size))

    for x in range (8):
        for y in range(8):
            # draw rank number
            if y == 0:
                rank = font.render(str(rankNo), True, "black", "white")
                rankNo = rankNo - 1
                screen.blit(rank,(y,x*size))

            if y == 0:
                file = font.render(fileLt, True, "black", "white")
                fileLt = chr(ord(fileLt)+1)
                screen.blit(file, (size*x,470))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    if l == 0:
        board()
        pygame.display.flip()
        l = 1


    # flip() the display to put your work on screen

pygame.quit()



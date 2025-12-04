import pygame

#Initialize the pygame

pygame.init()

screen  =  pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Game loop
running  = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False


    #RGB- Red, Green, Blue
    screen.fill((64,224,208))
    pygame.display.update()
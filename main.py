import pygame

#Initialize the pygame

pygame.init()

screen  =  pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('player.png',)
small_icon_player = pygame.transform.scale(playerImg, (64,64))

playerX = 350
playerY = 480

def player(x, y):
    screen.blit(small_icon_player, (x, y))

#Game loop
running  = True
while running:
    # RGB- Red, Green, Blue
    screen.fill((64, 224, 208))
    playerY -= 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False

    player(playerX, playerY)
    pygame.display.update()
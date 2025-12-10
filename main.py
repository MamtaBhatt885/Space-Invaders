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
playerX_change = 0

def player(x, y):
    screen.blit(small_icon_player, (x, y))

#Game loop
running  = True
while running:
    # RGB- Red, Green, Blue
    screen.fill((64, 224, 208))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False

        #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            print("A Keystoke has been pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)
    pygame.display.update()

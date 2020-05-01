import pygame

# window initialization
pygame.init() 

# window size
WIDTH,HEIGHT = 500,500
pygame.display.set_mode((WIDTH,HEIGHT))
screen = pygame.display.get_surface()

# load the background image and re-scale it to the window size
Background_Pic = pygame.image.load("Background.png")
Background_Pic = pygame.transform.scale(Background_Pic,(WIDTH,HEIGHT))

# load the mario image
Mario_Pic = pygame.image.load("Mario.png")

# create sprite
Mario = pygame.sprite.Sprite()
Mario.image = Mario_Pic 
Mario.rect = Mario.image.get_rect()
Mario.rect.x,Mario.rect.y = WIDTH/2,HEIGHT/2

# add mario to player group
Player_Group = pygame.sprite.Group()
Player_Group.add(Mario)

# start game
while True: 
    # Update
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit() 
            quit()
        if event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed() 
            if key[pygame.K_DOWN]:
                Mario.rect.y += 10
            if key[pygame.K_UP]:
                Mario.rect.y -= 10 
            if key[pygame.K_LEFT]:
                Mario.rect.x -= 10
            if key[pygame.K_RIGHT]:
                Mario.rect.x += 10
    # draw
    screen.blit(Background_Pic,(0,0))
    Player_Group.draw(screen)

    pygame.display.update()

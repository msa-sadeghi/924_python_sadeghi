import pygame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

bird_image = pygame.image.load("bird.png")
bird_rect = bird_image.get_rect()
bird_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bird_image, bird_rect)
    pygame.display.update()

import pygame
backside = pygame.image.load("png/back-side.png")
def cardDeck(screen_width, screen_height, screen):
    x = 0
    y = screen_height * 0.3
    cardImg = pygame.transform.scale(backside, (screen_width * 0.1, screen_height * 0.375))
    screen.blit(cardImg, (x, y))
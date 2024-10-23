import pyautogui
import pygame
import random
from cards import card
pygame.init()
screen_width, screen_height = pyautogui.size()
screen_height = screen_height - 60
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
cards = ['2c', '2d', '2h', '2s', '3c', '3d', '3h', '3s', '4c', '4d', '4h', '4s', '5c', '5d', '5h', '5s', '6c', '6d', '6h', '6s', '7c', '7d', '7h', '7s', '8c', '8d', '8h', '8s', '9c', '9d', '9h', '9s', 'Tc', 'Td', 'Th', 'Ts', 'Jc', 'Jd', 'Jh', 'Js', 'Qc', 'Qd', 'Qh', 'Qs', 'Kc', 'Kd', 'Kh', 'Ks', 'Ac', 'Ad', 'Ah', 'As', 'bj', 'rj']
deck = ['2c', '2d', '2h', '2s', '3c', '3d', '3h', '3s', '4c', '4d', '4h', '4s', '5c', '5d', '5h', '5s', '6c', '6d', '6h', '6s', '7c', '7d', '7h', '7s', '8c', '8d', '8h', '8s', '9c', '9d', '9h', '9s', 'Tc', 'Td', 'Th', 'Ts', 'Jc', 'Jd', 'Jh', 'Js', 'Qc', 'Qd', 'Qh', 'Qs', 'Kc', 'Kd', 'Kh', 'Ks', 'Ac', 'Ad', 'Ah', 'As', 'bj', 'rj']
random.shuffle(deck)
player1 = []
player2 = []
count = 0
while count < 5:
    player1.append(deck[count])
    count += 1
while count < 10:
    player2.append(deck[count])
    count += 1
del deck[:10]
while running:
    if len(deck) < 10:
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    for entry in range(len(player1)):
        card(player1[entry], 1, entry, cards, screen_width, screen_height, screen)
    for entry in range(len(player2)):
        card(player2[entry], 0, entry, cards, screen_width, screen_height, screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
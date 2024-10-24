import pyautogui
import pygame
import random
from cards import card
from decks import cardDeck
from draw import cardDraw
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
while "8" in deck[0] or "b" in deck[0] or "r" in deck[0]:
    random.shuffle(deck)
currentCard = []
currentCard.append(deck[0])
del deck[:1]
turn = True
while running:
    if len(player1) == 0 or len(player2) == 0:
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
        while "8" in deck[0] or "b" in deck[0] or "r" in deck[0]:
            random.shuffle(deck)
        currentCard = []
        currentCard.append(deck[0])
        del deck[:1]
        turn = True
    (mousex, mousey) = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()[0]
    deck2 = []
    for entrys in range(len(cards)):
        deck2.append(cards[entrys])
    random.shuffle(deck2)
    for entrys in range(len(deck2)):
        deck.append(deck2[entrys])
    facedown2 = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("white")
    if turn == True and len(player1) > 0 and len(player2) > 0:
        for entry in range(len(player1)):
            length = len(player1)
            card(player1[entry], 1, entry, cards, screen_width, screen_height, screen, currentCard, player1)
            if len(player1) != length:
                turn = False
                break
        try:
            if len(player1) != 0 and mousex >= 0 and mousex <= screen_width * 0.1 and mousey >= screen_height * 0.3 and mousey <= screen_height * 0.675 and pressed == True:
                player1.append(deck[0])
                del deck[:1]
        except:
            pass
    elif turn == False and len(player1) > 0 and len(player2) > 0:
        for entry in range(len(player2)):
            length = len(player2)
            card(player2[entry], 0, entry, cards, screen_width, screen_height, screen, currentCard, player2)
            if len(player2) != length:
                turn = True
                facedown2 = 0
                break
            facedown2 += 1
        try:
            if len(player2) != 0 and facedown2 == length:
                player2.append(deck[0])
                del deck[:1]
        except:
            pass
    card(currentCard[len(currentCard) - 1], 2, -1, cards, screen_width, screen_height, screen)
    cardDeck(screen_width, screen_height, screen)
    for entry in range(len(player1)):
        cardDraw(player1[entry], 1, entry, cards, screen_width, screen_height, screen, currentCard, player1)
    for entry in range(len(player2)):
        cardDraw(player2[entry], 0, entry, cards, screen_width, screen_height, screen, currentCard, player2)
    pygame.display.flip()
    clock.tick(10)
pygame.quit()
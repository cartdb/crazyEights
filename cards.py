import pygame
def card(type, player, num, cards, screen_width, screen_height, screen):
    if cards[0] == type:
        type = "2_of_clubs.png"
    elif cards[1] == type:
        type = "2_of_diamonds.png"
    elif cards[2] == type:
        type = "2_of_hearts.png"
    elif cards[3] == type:
        type = "2_of_spades.png"
    elif cards[4] == type:
        type = "3_of_clubs.png"
    elif cards[5] == type:
        type = "3_of_diamonds.png"
    elif cards[6] == type:
        type = "3_of_hearts.png"
    elif cards[7] == type:
        type = "3_of_spades.png"
    elif cards[8] == type:
        type = "4_of_clubs.png"
    elif cards[9] == type:
        type = "4_of_diamonds.png"
    elif cards[10] == type:
        type = "4_of_hearts.png"
    elif cards[11] == type:
        type = "4_of_spades.png"
    elif cards[12] == type:
        type = "5_of_clubs.png"
    elif cards[13] == type:
        type = "5_of_diamonds.png"
    elif cards[14] == type:
        type = "5_of_hearts.png"
    elif cards[15] == type:
        type = "5_of_spades.png"
    elif cards[16] == type:
        type = "6_of_clubs.png"
    elif cards[17] == type:
        type = "6_of_diamonds.png"
    elif cards[18] == type:
        type = "6_of_hearts.png"
    elif cards[19] == type:
        type = "6_of_spades.png"
    elif cards[20] == type:
        type = "7_of_clubs.png"
    elif cards[21] == type:
        type = "7_of_diamonds.png"
    elif cards[22] == type:
        type = "7_of_hearts.png"
    elif cards[23] == type:
        type = "7_of_spades.png"
    elif cards[24] == type:
        type = "8_of_clubs.png"
    elif cards[25] == type:
        type = "8_of_diamonds.png"
    elif cards[26] == type:
        type = "8_of_hearts.png"
    elif cards[27] == type:
        type = "8_of_spades.png"
    elif cards[28] == type:
        type = "9_of_clubs.png"
    elif cards[29] == type:
        type = "9_of_diamonds.png"
    elif cards[30] == type:
        type = "9_of_hearts.png"
    elif cards[31] == type:
        type = "9_of_spades.png"
    elif cards[32] == type:
        type = "10_of_clubs.png"
    elif cards[33] == type:
        type = "10_of_diamonds.png"
    elif cards[34] == type:
        type = "10_of_hearts.png"
    elif cards[35] == type:
        type = "10_of_spades.png"
    elif cards[36] == type:
        type = "jack_of_clubs.png"
    elif cards[37] == type:
        type = "jack_of_diamonds.png"
    elif cards[38] == type:
        type = "jack_of_hearts.png"
    elif cards[39] == type:
        type = "jack_of_spades.png"
    elif cards[40] == type:
        type = "queen_of_clubs.png"
    elif cards[41] == type:
        type = "queen_of_diamonds.png"
    elif cards[42] == type:
        type = "queen_of_hearts.png"
    elif cards[43] == type:
        type = "queen_of_spades.png"
    elif cards[44] == type:
        type = "king_of_clubs.png"
    elif cards[45] == type:
        type = "king_of_diamonds.png"
    elif cards[46] == type:
        type = "king_of_hearts.png"
    elif cards[47] == type:
        type = "king_of_spades.png"
    elif cards[48] == type:
        type = "ace_of_clubs.png"
    elif cards[49] == type:
        type = "ace_of_diamonds.png"
    elif cards[50] == type:
        type = "ace_of_hearts.png"
    elif cards[51] == type:
        type = "ace_of_spades.png"
    elif cards[52] == type:
        type = "black_joker.png"
    elif cards[53] == type:
        type = "red_joker.png"
    else:
        raise Exception("Not a valid card!")
    if player == 0:
        y = 0
    elif player == 1:
        y = screen_height * 0.675
    else:
        raise Exception("Not a valid player number!")
    if num == 0:
        x = screen_width * 0.1
    elif num == 1:
        x = screen_width * 0.275
    elif num == 2:
        x = screen_width * 0.45
    elif num == 3:
        x = screen_width * 0.625
    elif num == 4:
        x = screen_width * 0.8
    else:
        raise Exception("Hand limit is 5!")
    if player == 0:
        cardImg = pygame.image.load("png/back-side.png")
    elif player == 1:
        cardImg = pygame.image.load("png/" + type)
    cardImg = pygame.transform.scale(cardImg, (screen_width * 0.1, screen_height * 0.3))
    screen.blit(cardImg, (x, y))
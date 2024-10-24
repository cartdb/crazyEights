def func(arr):
    spades = 0
    hearts = 0
    diamonds = 0
    clubs = 0
    for entries in range(len(arr)):
        if "s" in arr[entries]:
            spades += 1
        elif "h" in arr[entries]:
            hearts += 1
        elif "d" in arr[entries]:
            diamonds += 1
        elif "c" in arr[entries]:
            clubs += 1
    array = [spades, hearts, diamonds, clubs]
    num = max(array)
    if num == spades:
        suit = "s"
    elif num == hearts:
        suit = "h"
    elif num == diamonds:
        suit = "d"
    elif num == clubs:
        suit = "c"
    return suit
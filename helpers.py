from time import sleep


def int_input(msg: str) -> int:
    while True:
        try:
            return int(input(msg))
        except ValueError:
            printm("Input must be a valid integer.\n> ", 0.05, 1)


def generate_deck():
    cards = []
    suits = ["Clover", "Hearts", "Spades", "Diamonds"]
    for card in range(1, 14):
        for suit in suits:
            cards.append((card, suit))
    return cards


def hand_value(hand):
    total = 0
    aces = 0
    for card, _ in hand:
        if card == 1:
            aces += 1
            total += 11
        elif card >= 10:
            total += 10
        else:
            total += card
    while total > 21 and aces != 0:
        total -= 10
        aces -= 1
    return total


def printm(m: str, t: float, mode: int = 0):
    for c in m:
        print(c, end="", flush=True)
        sleep(t)
    if mode == 0:
        print()


def card_str(card):
    value, suit = card
    names = {1: "A", 11: "J", 12: "Q", 13: "K"}
    value = names.get(value, str(value))
    return f"{value} of {suit}"


def hand_str(hand):
    return ", ".join(card_str(card) for card in hand)

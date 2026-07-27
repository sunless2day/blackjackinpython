import random

from helpers import card_str, generate_deck, hand_str, hand_value, int_input, printm


class Player:
    def __init__(self, balance=100):
        self.balance = balance

    def wager(
        self,
        timer: float,
        msg="",
    ) -> int:
        msg = f"How much do you want to bet?\tAvailable amount {self.balance}\n> "
        while True:
            printm(msg, timer, 1)
            bet = int_input("")
            if bet == 0:
                printm("You can't play for free, buddy.", 0.02)
            elif bet not in range(1, self.balance + 1):
                printm("Invalid amount.", 0.02)
            else:
                self.balance -= bet
                return bet


class Deck:
    def __init__(self):
        self.cards = generate_deck()

    def __str__(self):
        return f"Deck of {len(self.cards)} cards: {self.cards}"

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            self.cards = generate_deck()
            self.shuffle()
        return self.cards.pop()


class Game:
    def __init__(self):
        self.player = Player()
        self.deck = Deck()
        self.deck.shuffle()

    def player_round(self):
        bet = self.player.wager(0.02)
        player_hand = [self.deck.draw(), self.deck.draw()]
        dealer_hand = [self.deck.draw(), self.deck.draw()]
        while True:
            printm(
                f"Your hand: {hand_str(player_hand)} ({hand_value(player_hand)})", 0.02
            )
            printm(f"Dealer shows: {card_str(dealer_hand[0])}", 0.02)
            printm("Hit or stand? [h/s]\n> ", 0.02, 1)
            action = input().lower()
            if action in ("hit", "h"):
                player_hand.append(self.deck.draw())
                printm(
                    f"You pulled a {card_str(player_hand[len(player_hand) - 1])}", 0.02
                )
                player_total = hand_value(player_hand)
                if player_total > 21:
                    printm(
                        f"You got busted! Your total is: {player_total}.\nBetter luck next time.\n",
                        0.02,
                    )
                    return
            elif action in ("s", "stand"):
                break
            else:
                printm("That's not a choice", 0.02)

        printm(
            f"Dealer's hand: {hand_str(dealer_hand)} ({hand_value(dealer_hand)})", 0.02
        )
        while hand_value(dealer_hand) < 17:
            printm("Dealer hits...", 0.02)
            dealer_hand.append(self.deck.draw())
            printm(
                f"Dealer's hand: {hand_str(dealer_hand)} ({hand_value(dealer_hand)})",
                0.02,
            )
            if hand_value(dealer_hand) > 21:
                self.player.balance += bet * 2
                printm(
                    f"Dealer got busted! You win! New balance: {self.player.balance}.",
                    0.02,
                )
                return
        player_total = hand_value(player_hand)
        dealer_total = hand_value(dealer_hand)

        if player_total > dealer_total:
            self.player.balance += bet * 2
            printm(
                f"You win! Your total: {player_total}, Dealer: {dealer_total},\tBalance: {self.player.balance}.",
                0.02,
            )
        elif player_total < dealer_total:
            printm(
                f"You lose. Your total: {player_total}, Dealer: {dealer_total}, Balance: {self.player.balance}",
                0.02,
            )
        else:
            self.player.balance += bet
            printm(f"Push! You tie at {player_total}.", 0.02)

    def run(self):
        first_round = True
        while True:
            if first_round:
                printm("Do you want to start the game? [Y/n]\n> ", 0.02, 1)
                response = input().lower()
                if response in ("n", "no"):
                    printm("Exiting game...", 0.02)
                    exit(0)
                elif response not in ("y", "yes", ""):
                    printm("That's not a choice", 0.02)
                    continue
                else:
                    printm("Starting game...", 0.02)
                first_round = False
            self.player_round()
            if self.player.balance == 0:
                printm("You're out of money... Game over.", 0.02)
                exit(0)
            printm("Wanna play again? [Y/n]\n> ", 0.02, 1)
            response = input().lower()
            if response in ("n", "no"):
                printm("Thanks for playing!", 0.02)
                exit(0)

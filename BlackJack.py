import random
import time

class Wallet:
    def __init__(self):
        self.money = 500

    def buy_in(self):
        control = True
        print("Money: ", self.money)
        while control:
            control = False
            wager = int(input("How much would you like to wager?: "))
            if wager > self.money:
                print("Insufficient funds...\n")
                control = True
            else:
                return wager


class Deck:
    def __init__(self):
        self.reset_deck()

    def reset_deck(self):
        self.deck = [4,4,4,4,4,4,4,4,4,4,4,4,4]

    def is_empty(self):
        return not self

class Hand:
    def compute_value(self):
        for i in range(self.ace_count):
            if self.value > 21:
                self.value -= 10
                self.ace_count -= 1

    def __init__(self):
        self.hand = []
        self.ace_count = 0
        self.value = 0

    def deal(self, deck):
        if sum(deck.deck) == 0:
            print("No more cards in the deck")
            print("Shuffling...")
            time.sleep(3.5)
            deck.reset_deck()

        is_empty = True
        while is_empty == True:
            is_empty = False
            card = random.randint(2,14)
            if card == 2 and deck.deck[0] > 0:
                self.hand.append("two")
                self.value += 2
                deck.deck[0] -= 1
            elif card == 3 and deck.deck[1] > 0:
                self.hand.append("three")
                self.value += 3
                deck.deck[1] -= 1
            elif card == 4 and deck.deck[2] > 0:
                self.hand.append("four")
                self.value += 4
                deck.deck[2] -= 1
            elif card == 5 and deck.deck[3] > 0:
                self.hand.append("five")
                self.value += 5
                deck.deck[3] -= 1
            elif card == 6 and deck.deck[4] > 0:
                self.hand.append("six")
                self.value += 6
                deck.deck[4] -= 1
            elif card == 7 and deck.deck[5] > 0:
                self.hand.append("seven")
                self.value += 7
                deck.deck[5] -= 1
            elif card == 8 and deck.deck[6] > 0:
                self.hand.append("eight")
                self.value += 8
                deck.deck[6] -= 1
            elif card == 9 and deck.deck[7] > 0:
                self.hand.append("nine")
                self.value += 9
                deck.deck[7] -= 1
            elif card == 10 and deck.deck[8] > 0:
                self.hand.append("ten")
                self.value += 10
                deck.deck[8] -= 1
            elif card == 11 and deck.deck[9] > 0:
                self.hand.append("jack")
                self.value += 10
                deck.deck[9] -= 1
            elif card == 12 and deck.deck[10] > 0:
                self.hand.append("queen")
                self.value += 10
                deck.deck[10] -= 1
            elif card == 13 and deck.deck[11] > 0:
                self.hand.append("king")
                self.value += 10
                deck.deck[11] -= 1
            elif card == 14 and deck.deck[12] > 0:
                self.hand.append("ace")
                self.value += 11
                self.ace_count+=1
                deck.deck[12] -= 1
            else:
                is_empty = True

def dealer():
    print("Dealer's hand:", dealerHand.hand)
    while dealerHand.value <= yourHand.value and dealerHand.value < 21:
        time.sleep(1)
        dealerHand.deal(deck)
        print("Dealer's hand:", dealerHand.hand)
        dealerHand.compute_value()

    print("Score: ", dealerHand.value, "\n")
    time.sleep(1)
    print("\nYour hand:", yourHand.hand)
    print("Score: ", yourHand.value, "\n")
    time.sleep(1)

    if dealerHand.value < yourHand.value <= 21:
        print("You win!\nPayout: ", wager * 2)
        wallet.money += wager * 2
    elif yourHand.value < dealerHand.value <= 21:
        print("You lose!")
    elif yourHand.value == dealerHand.value:
        print("Draw!")
    elif dealerHand.value > 21:
        print("You win! Dealer busts!\nPayout: ", wager * 2)
        wallet.money += wager * 2
    print("\n\n")


# Game starts running here
deck = Deck()
wallet = Wallet()
while wallet.money > 0:

    wager = wallet.buy_in()
    wallet.money -= wager
    dealerHand = Hand()
    yourHand = Hand()

    print("\nDealing...")
    time.sleep(1.5)
    dealerHand.deal(deck)
    print("Dealer's hand:", dealerHand.hand)
    time.sleep(1.5)
    yourHand.deal(deck)
    print("Your hand:", yourHand.hand)
    time.sleep(1.5)
    print("Dealer's hand:", dealerHand.hand, ", [?]")
    dealerHand.deal(deck)
    yourHand.deal(deck)
    time.sleep(1.5)
    print("Your hand:", yourHand.hand, "\n")
    yourHand.compute_value()
    ender = False

    while True:

        # Checks hand value before prompting user
        if yourHand.value == 21:
            ender = True
            print("Blackjack! You win!\nPayout: ", wager*2, "\n\n")
            wallet.money += wager * 2
            break

        if yourHand.value > 21:
            ender = True
            print("You Bust! Loser!\n\n")
            break

        # Prompts user to either hit or stay
        user_input = input("hit or stay? ")

        if user_input == "hit":
            yourHand.deal(deck)
            print("Your hand:", yourHand.hand)
            yourHand.compute_value()

        elif user_input == "stay":
            print("\nPlayer stays...\n")
            time.sleep(1.5)
            break

        else:
            print("try again!")

    if not ender:
        dealer()

print("You are out of money! You suck!")

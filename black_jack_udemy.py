import random

'''Create a simple blackjack game between a player (human) and the computer
(dealer) using OOP.

In this milestone project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

You need to create a simple text-based BlackJack game
The game needs to have one player versus an automated dealer.
The player can stand or hit.
The player must be able to pick their betting amount.
You need to keep track of the player's total money.
You need to alert the player of wins, losses, or busts, etc...
And most importantly:

You must use OOP and classes in some portion of your game.
You can not just use functions in your game.
Use classes to help you define the Deck and the Player's hand.
There are many right ways to do this, so explore it well!
Feel free to expand this game. Try including multiple players.
Try adding in Double-Down and card splits!
Remember to you are free to use any resources you want and as always:
'''

'''As a starting point in your program, you may want to assign
variables to store a list of suits, ranks, and then use a dictionary
to map ranks to values.
'''
# suits is a tuple with the four suits
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
# ranks is a list of card ranks
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
# finally a value dictionary where you can pass in a cards rank
# and returns it's numerical value
values_dict = {'Two': 2,
               'Three': 3,
               'Four': 4,
               'Five': 5,
               'Six': 6,
               'Seven': 7,
               'Eight': 8,
               'Nine': 9,
               'Ten': 10,
               'Jack': 10,
               'Queen': 10,
               'King': 10,
               'Ace': 11,
               }

# declare a boolean value to used to control the while loop
playing = True


class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return ("{} of {}.").format(self.rank, self.suit)


class Deck():

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += "\n"+card.__str__()
        return ("The deck has: {}").format(deck_comp)

    # shuffles list in place
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        # returns a single card from the list
        single_card = self.deck.pop()
        return single_card


# this will represent which cards are ins someones hand
class Hand():

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, single_card):
        # single card passed in from Deck.deal()
        self.cards.append(single_card)
        # add value from dict to values
        self.value += values_dict[single_card.rank]

        # track aces
        if single_card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        # will assume that first ace is 11
        # if total value > 21 and I still have an ace
        # then change my ace to be a 1 instead of an 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?"))
        except:
            print("Sorry, please provide an integer.")
        else:
            if chips.bet > chips.total:
                print("Sorry, you do not have enough chips! You have: {}".format(chips.total))
            else:
                break


def hit(deck, hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing # bringing in the global variable created earlier to control while loop

    while True:
        x = input("Hit or Stand? Enter h or s.")
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player stands dealer's turn")
            playing = False
        else:
            print("Sorry, I did not understand that, please enter h or s only.")
            continue
        break


def player_busts(player, dealer, chips):
    print("Bust player.")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins.")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Player wins. Dealer busted.")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins.")
    chips.lose_bet()


# both player and dealer got 21
def push(player):
    print("Dealer and player tie! Push.")


new_deck = Deck()
new_deck.shuffle()
print(new_deck)
print(f'single card is {new_deck.deal()}')

# print(new_deck)

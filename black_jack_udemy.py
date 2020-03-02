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
               'sEight': 8,
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


class Hand():

    def __init(self,):
        pass


new_deck = Deck()
new_deck.shuffle()
print(new_deck)

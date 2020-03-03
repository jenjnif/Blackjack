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


# functions to display cards
def show_some(player, dealer):
    print("\nDealers hand:")
    print("one card hidden")
    print(dealer.cards[1])
    print("\n")
    print("Players hand:")
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    print("\nDealers hand:")
    for card in dealer.cards:
        print(card)
    print("\n")
    print("Players hand:")
    for card in player.cards:
        print(card)


# functions to display end of game scenarios
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


# run the logic of the game

while True:

    print("Welcome to Black Jack.")

    # create and shuffle deck
    deck = Deck()
    deck.shuffle()

    # deal two cards to each player
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # set up the players chips
    player_chips = Chips()

    # prompt player for bet
    take_bet(player_chips)

    # show cards but keep one dealer card hidden
    show_some(player_hand, dealer_hand)

    while playing:
        # ask player if want to hit or stand
        hit_or_stand(deck, player_hand)

        # show cards but keep one dealer card hidden
        show_some(player_hand, dealer_hand)

        # if players hand exceeds 21, run player_busts() and break from loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

    # if player hasn't busted, play dealers hand until dealer reaches beats player or busts
    # not playing soft 17
    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)

        # show all cards
        show_all(player_hand, dealer_hand)

        # run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    # inform player of their chips total
    print("\nPlayer total chips are at: {}".format(player_chips.total))

    # ask if they want to play again
    new_game = input("Would you like to play another hand? y/n")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing.")
    break

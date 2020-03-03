'''tests for blackjack game'''
from black_jack_udemy import Card, Deck, Hand


def test_card_returns_correct_suit_rank():
    suit = "hearts"
    rank = "two"
    card = Card(suit, rank)
    assert str(card) == ("{} of {}.").format(card.rank, card.suit)


def test_complete_deck():
    test_deck = Deck()
    assert len(test_deck.deck) == 52


def test_returns_single_card_suit_rank():
    test_deck = Deck()
    single_card = test_deck.deal()
    suit = single_card.suit
    rank = single_card.rank
    assert suit == "Clubs"
    assert rank == "Ace"


def test_hand_value_one_card():
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
    # creates a complete card deck
    test_deck = Deck()
    # shuffles the complete deck
    test_deck.shuffle()
    # creates a players hand
    test_player = Hand()
    # Deal one card from the deck --> Card(suit, rank)
    new_card = test_deck.deal()
    # adds card to test_player hand
    test_player.add_card(new_card)
    assert test_player.value == values_dict[new_card.rank]


def test_hand_value_two_cards():
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
    # creates a complete card deck
    test_deck = Deck()
    # shuffles the complete deck
    test_deck.shuffle()
    # creates a players hand
    test_player = Hand()

    # First card
    new_card = test_deck.deal()
    test_player.add_card(new_card)
    first_value = values_dict[new_card.rank]

    # Second card
    new_card = test_deck.deal()
    test_player.add_card(new_card)
    second_value = values_dict[new_card.rank]
    assert test_player.value == first_value + second_value

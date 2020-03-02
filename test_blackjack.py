'''tests for blackjack game'''
from black_jack_udemy import Card, Deck


def test_card_returns_correct_suit_rank():
    card = Card()
    card.suit = "hearts"
    card.rank = "two"
    assert str(card) == ("{} of {}.").format(card.rank, card.suit)


def test_complete_deck():
    test_deck = Deck()
    test_deck.deck = [1, 2, 3, "queen", "king", "ace"]
    assert test_deck.deck == [1, 2, 3, "queen", "king", "ace"]


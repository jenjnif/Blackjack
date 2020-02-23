'''tests for blackjack game'''
from black_jack_udemy import Card


def test_card_returns_correct_suit_rank():
    card = Card()
    card.suit = "hearts"
    card.rank = "two"
    assert str(card) == ("{} of {}.").format(card.rank, card.suit)

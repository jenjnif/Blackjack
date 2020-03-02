'''tests for blackjack game'''
from black_jack_udemy import Card, Deck


def test_card_returns_correct_suit_rank():
    suit = "hearts"
    rank = "two"
    card = Card(suit, rank)
    assert str(card) == ("{} of {}.").format(card.rank, card.suit)


def test_complete_deck():
    test_deck = Deck()
    assert len(test_deck.deck) == 52

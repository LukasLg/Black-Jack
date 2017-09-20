import pytest
from blackjack import Card, Deck

def test_card_has_suit():
    card = Card('diamond')
    assert hasattr(card, 'suit')

def test_deck():
    pass

def test_has_valid_suit():
    with pytest.raises(ValueError):
        Card('fakesuit')
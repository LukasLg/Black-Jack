import pytest
from blackjack import Card, Deck

def test_card_has_suit():
    card = Card('diamond',2)
    assert hasattr(card, 'suit')

def test_deck():
    pass

def test_has_valid_suit():
    with pytest.raises(ValueError):
        Card('fakesuit',2)

    c = Card('spade', 2)
    assert c.suit == 'spade'

def test_card_has_a_value():

    king_of_spades = Card('spade', 'K')
    queen_of_spades = Card('spade', 'Q')

    assert king_of_spades.value == 'K'
    assert queen_of_spades.value == 'Q'

def test_add_card():
    assert 5 == Card('spade', 2) + Card('spade', 3)

def test_add_with_face():
    assert 13 == Card('spade', 'J') + Card('spade', 3)

def test_compare():
    assert True == (Card('spade','Q') == Card('spade','J'))

def test_greater_then():
    assert True == (Card('spade','Q') > Card('spade',3))


from blackjack import Card, Deck

def test_card_has_suit():
    card = Card('diamonds')
    assert hasattr(card, 'suit')

def test_deck():
    pass

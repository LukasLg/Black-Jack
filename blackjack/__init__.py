class Card:
    def __init__(self, suit):
        if suit not in ('spade', 'diamond', 'heart', 'clubs'):
            raise ValueError('Suit must be according to 52-standard card game')

        self.suit = suit


class Deck:
    pass


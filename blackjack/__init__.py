class Card:
    def __init__(self, suit, value):
        if suit not in ('spade', 'diamond', 'heart', 'clubs'):
            raise ValueError('Suit must be according to 52-standard card game')

        self.suit = suit

        if value not in ['A','K', 'Q','J'] and value not in list(range(2,11)):
            raise ValueError

        self.value = value

        if value in ['K', 'Q', 'J']:
            self.num_value = 10
        elif value == 'A':
            self.num_value = 11
        else:
            self.num_value = value

    def __add__(self, other):
        return self.num_value + other.num_value

    def __eq__(self, other):
        return self.num_value == other.num_value

    def __gt__(self, other):
        return self.num_value > other.num_value

class Deck:
    pass


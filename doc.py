# Import Needed Package
from random import shuffle


class Card:
    """
        Defines A Card, For Use In Deck Class, With Both Suit And Value
    """
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck():
    """
        Defines A Deck Of 52 Cards, Introducing Capabilities To Shuffle
        Deck, Deal A Card, Or Deal A Hand Of Cards
    """
    def __init__(self):
        suits =  ["Clubs", "Diamonds", "Hearts", "Spades"]
        values = ["2", "3", "4", "5", "6", "7", "8", 
                  "9", "10", "J", "Q", "K", "A"]
        self.cards = [Card(value,suit) for suit in suits for value in values]

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count,num])
        if count == 0:
            raise ValueError("[ERROR] All Cards Have Been Dealt!")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size ):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count()<52:
            raise ValueError("[ERROR] Only Full Decks Can Be Shuffled!")
        shuffle(self.cards)
        return self


# Instantiate And Shuffle Deck Object
d = Deck()
d.shuffle()

# Deal And Print Card
card = d.deal_card()
print(card)

# Deal And Print Hand Of Specific Size
hand = d.deal_hand(5)
print(hand)

# Print Deck Remaining Count
print(d.count())

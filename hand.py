# hand.py

from deck import Deck

class Hand(Deck):
    def __init__(self, name):
        Deck.__init__(self, empty=True)
        self.name = name

    def addCard(self, a_card):
        self.cards.append(a_card)

    def isEmpty(self):
        return len(self.cards)==0

    def __str__(self):
        s = self.name + ' hand:\n'
        s += Deck.__str__(self)
        return s

if __name__=='__main__':
    from card import Card

    # seven of hearts
    card1 = Card(0, 7)
    # jack of clubs
    card2 = Card(2, 11)

    pl1_hand = Hand('player1')
    pl1_hand.addCard(card1)
    pl1_hand.addCard(card2)

    print(pl1_hand)

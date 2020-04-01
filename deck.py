# deck.py

from card import Card
import random

class Deck:
    def __init__(self, empty=False):
        self.cards = []
        if not empty:
            for suit, suitName in enumerate(Card.suits):
                for face, faceName in enumerate(Card.faces[1:]):
                    self.cards.append(Card(suit, face+1))

    def __str__(self):
        s = ''
        for i, card in enumerate(self.cards):
            s += "%25s" % (str(card),)
            if (i+1)%5==0:
                s += '\n'
        return s

    def shuffle(self):
        random.shuffle(self.cards)

    def removeCard(self, a_card):
        if a_card in self.cards:
            self.cards.remove(a_card)
            return True
        else:
            return False

    def dealACard(self):
        return self.cards.pop()

    def isEmpty(self):
        return len(self.cards)==0

    def dealCards(self, hands, cards_to_deal=999):
        remaining_cards = len(self.cards)
        n_hands = len(hands)
        current_hand = 0
        while remaining_cards>0 and cards_to_deal>0:
            card = self.dealACard()
            remaining_cards -= 1
            cards_to_deal -= 1
            hands[current_hand].addCard(card)
            current_hand = (current_hand+1) % n_hands


if __name__=='__main__':
    a_deck = Deck()

    print("original deck:")
    print(a_deck)

    print("\nremoving Ace of Hearts by codes (0, 1)")
    if a_deck.removeCard(Card(0, 1)):
        print("Ace of Hearts removed")
    else:
        print("ERROR, unable to remove card")
    print(a_deck)

    print("\nremoving Two of Hearts by names")
    if a_deck.removeCard(Card(Card.suits.index("Hearts"), Card.faces.index("Two"))):
        print("Two of Hearts removed")
    else:
        print("ERROR, unable to remove card")
    print(a_deck)

    print("\nDeal a card")
    print(a_deck.dealACard())

    print("\nshuffled deck:");
    a_deck.shuffle()
    print(a_deck)

    from hand import Hand
    hand1 = Hand('player1')
    hand2 = Hand('player2')
    hand3 = Hand('player3')
    # deal one card per hand
    a_deck.dealCards([hand1, hand2, hand3], 3)
    print(hand1)
    print(hand2)
    print(hand3)
    print("\n")
    print(a_deck)

    print("\n")
    a_deck.dealCards([hand1, hand2, hand3])
    print(hand1)
    print(hand2)
    print(hand3)
    print(a_deck)

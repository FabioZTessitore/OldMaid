# deck.py

# un mazzo di carte da gioco

from card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(len(Card.suits)):
            for face in range(1, len(Card.faces)):
                self.cards.append(Card(suit, face))

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
            current_hand = (current_hand+1)%n_hands


if __name__=='__main__':
    a_deck = Deck()

    print("original deck:")
    print(a_deck)

    print("removing Ace of Hearts")
    if a_deck.removeCard(Card(0, 1)):
        print "Ace of Hearts removed"
    else:
        print "ERROR, unable to remove card"
    print(a_deck)

    print "Deal a card"
    print a_deck.dealACard()

    print("shuffled deck:");
    a_deck.shuffle()
    print(a_deck)

    from hand import Hand
    hand1 = Hand('player1')
    hand2 = Hand('player2')
    hand3 = Hand('player3')
    # deal one card per hand
    a_deck.dealCards([hand1, hand2, hand3], 3)
    print hand1
    print hand2
    print hand3
    print a_deck

    a_deck.dealCards([hand1, hand2, hand3])
    print hand1
    print hand2
    print hand3
    print a_deck

# oldmaidhand.py

# una mano del gioco Old Maid

from card import Card
from hand import Hand

class OldMaidHand(Hand):
    match_rules = {    # Hearts := Diamonds,  Clubs := Spades
            0: 1,
            1: 0,
            2: 3,
            3: 2
    }

    def removeMatches(self):
        count = 0
        cards = self.cards[:]
        for card in cards:
            match = Card(OldMaidHand.match_rules.get(card.suit), card.face)
            if match in self.cards:
                self.cards.remove(match)
                self.cards.remove(card)
                print "Hand %s: %s matches %s" % (self.name, card, match)
                count += 1
        return count


if __name__=='__main__':
    # seven of hearts
    card1 = Card(0, 7)
    # jack of clubs
    card2 = Card(2, 11)
    # jack of spades
    card3 = Card(3, 11)

    pl1_hand = OldMaidHand('player1')
    pl1_hand.addCard(card1)
    pl1_hand.addCard(card2)
    pl1_hand.addCard(card3)
    print pl1_hand

    pl1_hand.removeMatches()
    print pl1_hand

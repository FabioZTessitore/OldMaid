# oldmaidgame.py

# il gioco di carte OldMaid

from card import Card
from oldmaidhand import OldMaidHand
from cardgame import CardGame

class OldMaidGame(CardGame):
    def __init__(self, names):
        print "---------------------Creazione del deck"
        CardGame.__init__(self)

        print "---------------------Rimozione della regina di picche"
        self.getDeck().removeCard(Card(Card.suits.index('Clubs'), 12))

        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))

    def removeAllMatches(self):
        matches = 0
        for hand in self.hands:
            matches += hand.removeMatches()
        return matches

    def findNeighbor(self, turn):
        numHands = len(self.hands)
        for next in range(1, numHands):
            neighbor = (turn+next) % numHands
            if not self.hands[neighbor].isEmpty():
                return neighbor

    def playOneTurn(self, turn):
        if self.hands[turn].isEmpty():
            return 0
        neighbor = self.findNeighbor(turn)
        pickedCard = self.hands[neighbor].dealACard()
        self.hands[turn].addCard(pickedCard)
        print "Hand", self.hands[turn].name, "picked", pickedCard
        count = self.hands[turn].removeMatches()
        self.hands[turn].shuffle()
        return count

    def run(self):
        print "---------------------Distribuzione delle carte"
        self.getDeck().dealCards(self.hands)
        self.printHands()

        print "---------------------Rimozione delle coppie"
        matches = self.removeAllMatches()
        self.printHands()

        turn = 0
        numHands = len(self.hands)
        while matches<25:
            matches += self.playOneTurn(turn)
            turn = (turn+1) % numHands

        print "---------------------Gioco Finito"
        self.printHands()


if __name__=='__main__':
    names = ['player1', 'player2', 'player3']
    game = OldMaidGame(names)
    game.run()

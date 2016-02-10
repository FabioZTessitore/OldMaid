# cardgame.py

# un generico gioco di carte

from deck import Deck

class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    def getDeck(self):
        return self.deck

    def printHands(self):
        for hand in self.hands:
            print hand

if __name__=='__main__':
    a_card_game = CardGame();
    print a_card_game.deck

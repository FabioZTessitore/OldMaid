# card.py

# una carta da gioco

class Card:
    faces = [ "unused", "Ace", "Two", "Three", "Four", "Five",
            "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King" ]
    suits = [ "Hearts", "Diamonds", "Clubs", "Spades" ]

    def __init__(self, suit, face):
        self.suit = suit
        self.face = face

    def getSuit(self):
        return self.suit

    def getFace(self):
        return self.face

    def getSuitName(self):
        return Card.suits[self.suit]

    def getFaceName(self):
        return Card.faces[self.face]

    def __cmp__(self, other):
        if self.face==other.face and self.suit==other.suit:
            return 0
        elif self.suit==other.suit:
            return self.face-other.face
        else:
            return self.suit-other.suit

    def __str__(self):
        return ("%s of %s" % (self.getFaceName(), self.getSuitName()))


if __name__=='__main__':
    print("Faces are:")
    for i, face in enumerate(Card.faces):
        print("%d) %s" % (i, face))

    print("Suits are:")
    for i, suit in enumerate(Card.suits):
        print("%d) %s" % (i, suit))

    suit = 0
    face = 1
    a_card = Card(suit, face)

    print "Card suit code: %d" % (a_card.getSuit(),)
    print "Card face code: %d" % (a_card.getFace(),)
    print "Card suit name: %s" % (a_card.getSuitName(),)
    print "Card face name: %s" % (a_card.getFaceName(),)
    print a_card

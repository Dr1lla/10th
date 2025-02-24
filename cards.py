class Card:
    """Одна гральна карта"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", 
             "8", "9", "10", "J", "Q", "K", ]
    SUITS = [u'\u2660', u'\u2663', u'\u2665', u'\u2666']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Unprintable_Card(Card):
    def __str__(self):
        return "<Не можна друкувати>"

class Positionable_Card(Card):
    """Карта, яку можна покласти
    обличчям або сорочкою вниз"""
    def __init__(self, rank, suit, face_up = True):
        super().__init__(rank, suit)
        self.is_face_up = face_up
    def __str__(self):
        if self.is_face_up:
            rep = super().__str__()
        else:
            rep = "XX"
        return rep
    def flip(self):
        self.is_face_up = not self.is_face_up


class Hand:
    """ Рука: набір карт, який має гравець """

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


class Deck(Hand):
    """ Deck of playing cards """

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def add_new_desk(self):
        self.populate()
        self.shuffle()

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if not self.cards:
                    self.add_new_desk()
                top_card = self.cards[0]
                self.give(top_card, hand)

if __name__ == "__main__":
    print("Ви запустили модуль cards, "
          "а не імпортували його (import cards).")
    print("Тестування модуля.\n")

    card1 = Card("T", Card.SUITS[0])
    card2 = Unprintable_Card("T", Card.SUITS[1])
    card3 = Positionable_Card("T", Card.SUITS[2])
    
    print("Об'єкт Card:", card1)
    print("Об'єкт Unprintable_Card:", card2)
    print("Об'єкт Positionable_Card:", card3)

    card3.flip()
    print("Перевертаю об'єкт Positionable_Card:", card3)

    deck1 = Deck()
    print("\nСтворено нову колоду:", deck1)
    deck1.populate()
    print("У колоді з'явились карти:", deck1, sep="\n")
    deck1.shuffle()
    print("Колода перемішена:", deck1, sep="\n")

    hand1 = Hand()
    hand2 = Hand()

    deck1.deal(hands=(hand1, hand2), per_hand=5)
    print("\nРоздано по 5 карт.")
    print("Рука1:", hand1)
    print("Рука2:", hand2)

    print("Залишилось у колоді:", deck1, sep="\n")

    deck1.clear()
    print("Колода очищена:", deck1)
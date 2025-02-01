import cards, games

class BJ_Card(cards.Positionable_Card):
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v
    
class BJ_Deck(cards.Deck):
    """Колода для гри в Блекджек."""
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))

class BJ_Hand(cards.Hand):
    """Рука гравця в Блекджек."""
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super().__str__()
        if self.total:
            rep += " (" + str(self.total) + ")"
        return rep

    @property
    def total(self)
        for card in self.cards:
            if not card.value:
                return None
        t = 0
        contains_ace = False
        for card in self.cards:
            t += card.value
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        if contains_ace and t <= 11:
            t += 10
        return t

    def is_busted(self):
        return self.total > 21

class BJ_Player(BJ_Hand)
    """Гравець у Блек-джек."""
    def is_hitting(self):
       response = games.ask_yes_no("\n" + self.name + ", братимете ще карти")
       return response == "y"

    def bust(self):
       print(self.name, "перебрав(ла).")
       self.lose()

    def win(self):
        print(self.name, "виграв(ла).")

    def push(self):
        print(self.name, "зіграв(ла) з дилером внічию")

class BJ_Dealer(BJ_Hand):
    """Дилер у Блек-джек"""
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "перебрав.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class BJ_Game:
    """Гра Блєк-джек."""
    def __init__(self, names):
        self.playing = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Дилек")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additinal_cards(self, player)
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        self.deck.deal(self.players + [self.dealer],
            per_hand = 2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)

        for player in self.players:
            self.__additinal_cards(player)
        self.dealer.flip_first_card()

        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additinal_cards(self.dealer)

        if self.dealer.is_busted():
            for player in self.still_playing:
                player.win()
        else:
            for player in self.still_playing:
                if player.total > self.dealer.total:
                    player.win()
                elif player.total < self.dealer.total:
                    player.lose()
                else:
                    player.push()

        for player in self.players:
            player.clear()
        self.dealer.clear()

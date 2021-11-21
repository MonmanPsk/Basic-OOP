import random

class Deck:
    def __init__(self):
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

        for i in range(2):
            for j in cards.copy():
                cards.append(j)

        self.deck_cards = cards
        
    def shuffle(self):
        random.shuffle(self.deck_cards)

    def deal_out(self):
        self.deal = self.deck_cards[0]
        self.deck_cards.pop(0)
        return self.deal

class Player:
    def __init__(self, deal):
        self.cards_value = 0
        self.player_cards = deal
        self.recent_cards = deal.copy()

    def choose(self):
        if self.checkStatus() == ("Bust" or "Win"):
            return

        self.answer = input("Choose between 'hit' or 'stand' : ")
        if self.answer == "hit":
            self.hit()

    def hit(self):
        card = deck.deal_out()
        self.player_cards.append(card)
        self.recent_cards.append(card)
        print("Player hand :", self.player_cards)
        self.checkValue()
        self.choose()

    def checkValue(self):
        for i in self.recent_cards:
            if i == "Jack":
                self.cards_value += 10
            elif i == "Queen":
                self.cards_value += 10
            elif i == "King":
                self.cards_value += 10
            elif i == "Ace":
                self.cards_value += int(input("Choose between 11 or 1 : "))
            else:
                self.cards_value += int(i)
        self.recent_cards = []
        self.checkStatus()

    def checkStatus(self):
        if self.cards_value > 21:
            return "Bust"
        if self.cards_value == 21:
            return "Win"

    def dealerCheck(self):
        if self.cards_value <= 16:
            card = deck.deal_out()
            self.player_cards.append(card)
            self.recent_cards.append(card)
            self.checkValue()
            print("Dealer hand :", self.player_cards)

deck = Deck()
deck.shuffle()

dealer = Player([deck.deal_out(), deck.deal_out()])
print("Dealer hand :", dealer.player_cards[0])
dealer.checkValue()

player = Player([deck.deal_out(), deck.deal_out()])
print("Player hand :", player.player_cards)
player.checkValue()
player.choose()

print("Dealer hand :", dealer.player_cards)
dealer.dealerCheck()

if (player.checkStatus == "Win" or dealer.checkStatus() == "Bust") or (player.cards_value > dealer.cards_value and player.checkStatus() != "Bust"):
    print("Win!")
else:
    print("Lose!")
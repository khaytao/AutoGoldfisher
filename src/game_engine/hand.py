from .card import Card

class Hand:

    def __init__(self):
        self.cards = []

    def land_in_hand(self):
        for card in self.cards:
            if card.is_land:
                return True
        return False

    def is_card_in_hand(self, card_name:str):
        for card in self.cards:
            if card.name == card_name:
                return True
        return False

    def add_card(self, card: Card):
        self.cards.append(card)

    def remove_card(self, card: Card):
        for card_in_hand in self.cards:
            if card_in_hand.name == card.name:
                self.cards.remove(card_in_hand)
                return

    def find_land_in_hand(self):
        for card_in_hand in self.cards:
            if card_in_hand.is_land:
                return card_in_hand
        return None

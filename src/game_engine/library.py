from copy import deepcopy
import random


def get_library_from_path(path):
    # todo implement
    pass


class Library:

    def __init__(self, decklist: dict):
        """
        :param decklist: decklist is a Card object:int dictionary where keys are cards and int are copies in the deck
        """
        self.cards = []
        self.init_library(decklist)
        random.shuffle(self.cards)

    def init_library(self, decklist: dict):
        for card in decklist.keys():
            for i in range(decklist[card]):
                self.cards.append(deepcopy(card))

    def draw_card(self):
        try:
            return self.cards.pop()
        except IndexError:
            raise IndexError("draw from empty library")
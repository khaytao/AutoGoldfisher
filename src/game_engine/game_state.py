from src.game_engine.library import Library, get_library_from_path
from src.game_engine.hand import Hand


class GameState:

    def __init__(self, decklist_dir_path):

        self.library = get_library_from_path(decklist_dir_path)
        self.hand = Hand()

        self.battlefield = []
        self.lands = []

        self.damage_dealt = 0

    def update_turns_in_play(self):
        for card in self.battlefield:
            card.turns_in_play += 1
        for card in self.lands:
            card.turns_in_play += 1

    def draw_card(self):
        # todo handle drawing from empty deck
        self.hand.add_card(self.library.draw_card())

    def play_card(self, card):
        if card in self.hand:
            self.hand.remove_card(card)

    def get_available_mana(self):
        return len(self.lands)
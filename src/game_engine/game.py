from src.game_engine.library import Library, get_library_from_path
from src.game_engine.game_state import GameState
from .card import Card


class Game:
    """
    starts the game, simulate game actions, and awaits input
    """

    def __init__(self, player_agent, decklist_dir_path, damage_goal=20, cards_in_openening_hand=7):
        # self.player = player_agent
        # self.library = get_library_from_path(decklist_dir_path)
        # self.hand = []
        # self.cards_in_opening_hand = cards_in_openening_hand
        # self.battlefield = []
        # self.lands = []
        #
        # self.damage_dealt = 0
        self.player = player_agent
        self.game_state = GameState(decklist_dir_path)
        self.damage_goal = damage_goal
        self.cards_in_opening_hand = cards_in_openening_hand
    # def draw_card(self):
    #     # todo handle drawing from empty deck
    #     self.hand.append(self.library.draw_card())

    def play_card(self, card: Card):
        self.game_state.hand.remove_card(card)
        if card.is_land:
            self.game_state.lands.append(card)
        else:
            self.game_state.battlefield.append(card)

    def play_turn(self):
        # auto play land
        land_in_hand =  self.game_state.hand.find_land_in_hand()
        if land_in_hand:
            self.play_card(land_in_hand)

        # choose player actions
        moves = self.player.get_moves_for_turn(self.game_state)
        for card in moves:
            self.play_card(card)

        # deal damage
        for card in self.game_state.battlefield:
            self.game_state.damage_dealt += card.get_damage()
            if not card.is_permanent:
                self.game_state.battlefield.remove(card)

        # update board
        self.game_state.update_turns_in_play()

    def start_game(self):
        # draw opening hand
        for i in range(self.cards_in_opening_hand):
            self.game_state.draw_card()

        while self.game_state.damage_dealt < self.damage_goal:
            self.play_turn()
        
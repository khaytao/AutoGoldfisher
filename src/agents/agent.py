from abc import ABC, abstractmethod
from src.game_engine.game_state import GameState
from src.game_engine.card import Card


class Agent(ABC):

    @abstractmethod
    def get_moves_for_turn(self, game_state) -> list:
        """
        get player actions
        :param game_state: the current game state
        :return: chosen moves, ensuring cost is less then available mana
        """


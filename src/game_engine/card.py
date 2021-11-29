class Card:
    def __init__(self,  card_name: str, cost:int, is_land: bool, is_permanent: bool, damage_per_turn: list):
        self.is_land = is_land
        self.is_permanent = is_permanent
        self.damage_per_turn = damage_per_turn
        if not self.damage_per_turn:
            self.damage_per_turn = [0]  # handles edge cases
        self.name = card_name
        self.cost = cost
        self.turns_in_play = 0

    def __copy__(self):
        return Card(self.name, self.cost, self.is_land, self.is_permanent, self.damage_per_turn)

    def get_damage(self):
        index = min(len(self.damage_per_turn) - 1, self.turns_in_play)
        return self.damage_per_turn[index]

from Player import Player
from Field import Field


class Quoridor:
    first_player = Player("Greg")
    second_player = Player("Smit")

    current_player = Player
    winner = Player

    play_field = Field

    def set_players(self, player_one, player_two):
        self.first_player = player_one
        self.second_player = player_two

    def start_game(self):
        self.current_player = self.first_player
        self.play_field = Field

    def move_player(self, letter, number):
        self.current_player.change_coordinates(letter, number)

    def create_wall(self):
        pass

    def check_end_game(self):
        pass

    def end_game(self):
        pass

    def switch_player(self):
        if self.current_player == self.first_player:
            self.current_player = self.second_player
        else:
            self.current_player = self.first_player

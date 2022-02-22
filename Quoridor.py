from Player import Player
from Field import Field


class Quoridor:
    first_player = Player("John")
    second_player = Player("Smit", "E", "9")

    current_player = Player()
    winner = Player()

    play_field = Field()

    def set_players(self, player_one, player_two):
        self.first_player = player_one
        self.second_player = player_two

    def start_game(self):
        self.current_player = self.first_player
        self.play_field = Field()
        self.play_field.write_player_location(self.first_player.get_letter(), self.first_player.get_number())
        self.play_field.write_player_location(self.second_player.get_letter(), self.second_player.get_number())

    def move_player(self, letter, number):
        if self.play_field.check_access_move(self.current_player, letter, number):
            self.play_field.clean_player_location(self.current_player.get_letter(), self.current_player.get_number())
            self.current_player.change_coordinates(letter, number)
            self.play_field.write_player_location(self.current_player.get_letter(), self.current_player.get_number())
        else:
            print("Move is incorrect!")

    def jump_player(self, letter, number):
        self.play_field.clean_player_location(self.current_player.get_letter(), self.current_player.get_number())
        self.current_player.change_coordinates(letter, number)
        self.play_field.write_player_location(self.current_player.get_letter(), self.current_player.get_number())

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
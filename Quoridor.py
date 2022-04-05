from Player import Player
from Field import Field


class Quoridor:
    first_player = Player("White")
    second_player = Player("Black", "E", "9")

    current_player = Player()
    winner = Player()

    play_field = Field()

    is_ended = False

    def set_players(self, player_one: Player, player_two: Player):
        self.first_player = player_one
        self.second_player = player_two

    def start_game(self):
        self.is_ended = False
        #self.first_player = Player("White")
        #self.second_player = Player("Black", "E", "9")
        self.play_field = Field()
        self.current_player = self.first_player
        self.play_field.write_player_location(self.first_player.get_letter(), self.first_player.get_number())
        self.play_field.write_player_location(self.second_player.get_letter(), self.second_player.get_number())

    def move_player(self, letter: str, number: str):
        if self.is_ended is False:
            if self.play_field.check_access_move(self.current_player, letter, number):
                self.play_field.clean_player_location(self.current_player.get_letter(), self.current_player.get_number())
                self.current_player.change_coordinates(letter, number)
                self.play_field.write_player_location(self.current_player.get_letter(), self.current_player.get_number())
                Quoridor.switch_player(self)
                Quoridor.check_end_game(self)
            else:
                print("Move is incorrect!")
        else:
            print("Game is already ended!")

    def jump_player(self, letter: str, number: str):
        if self.is_ended is False:
            if self.play_field.check_access_jump(self.current_player, letter, number):
                self.play_field.clean_player_location(self.current_player.get_letter(), self.current_player.get_number())
                self.current_player.change_coordinates(letter, number)
                self.play_field.write_player_location(self.current_player.get_letter(), self.current_player.get_number())
                Quoridor.switch_player(self)
                Quoridor.check_end_game(self)
            else:
                print("Jump is incorrect!")
        else:
            print("Game is already ended!")

    def create_wall(self, letter: str, number: str, h_or_v: str):
        if self.is_ended is False:
            if self.play_field.check_access_create_wall(letter, number, self.current_player.wall_counter):
                self.play_field.write_wall_creation(letter, number, h_or_v)
                self.current_player.wall_counter += 1
                Quoridor.switch_player(self)
            else:
                print("Wall creation is incorrect!")
        else:
            print("Game is already ended!")

    def check_end_game(self):
        if self.first_player.get_number() == "9":
            Quoridor.end_game(self, self.first_player)
        elif self.second_player.get_number() == "1":
            Quoridor.end_game(self, self.second_player)

    def end_game(self, winner: Player):
        self.winner = winner
        self.is_ended = True

    def switch_player(self):
        if self.current_player == self.first_player:
            self.current_player = self.second_player
        else:
            self.current_player = self.first_player
from Parser import Parser
from Player import Player


class Field:
    def __init__(self):
        self.player_coordinates = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.wall_coordinates = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def write_player_location(self, vertical_coordinate, horizontal_coordinate):
        self.player_coordinates[Parser.parse_number(horizontal_coordinate)][
            Parser.parse_player_letter(vertical_coordinate)] = 1

    def clean_player_location(self, vertical_coordinate, horizontal_coordinate):
        self.player_coordinates[Parser.parse_number(horizontal_coordinate)][
            Parser.parse_player_letter(vertical_coordinate)] = 0

    def check_access_move(self, player: Player, letter, number) -> bool:
        player_position = [Parser.parse_number(player.get_number()), Parser.parse_player_letter(player.get_letter())]
        moving_position = [Parser.parse_number(number), Parser.parse_player_letter(letter)]
        if abs(player_position[0] - moving_position[0]) == 1 and player_position[1] == moving_position[1] or \
                abs(player_position[1] - moving_position[1]) == 1 and player_position[0] == moving_position[0]:
            if player_position[0] - moving_position[0] == 1:
                if self.wall_coordinates[player_position[0]][player_position[1]] == 1 and \
                        self.wall_coordinates[player_position[0]][player_position[1]+1] == 1:
                    print("You can not move through a wall!")
                    return False
                elif self.player_coordinates[moving_position[0]][moving_position[1]] == 1:
                    print("You can not move on a another player place!")
                    return False
                else:
                    return True
            elif player_position[0] - moving_position[0] == -1:
                if self.wall_coordinates[player_position[0] + 1][player_position[1]] == 1 and \
                        self.wall_coordinates[player_position[0] + 1][player_position[1] + 1] == 1:
                    print("You can not move through a wall!")
                    return False
                elif self.player_coordinates[moving_position[0]][moving_position[1]] == 1:
                    print("You can not move on a another player place!")
                    return False
                else:
                    return True
            elif player_position[1] - moving_position[1] == 1:
                if self.wall_coordinates[player_position[0]][player_position[1]] == 1 and \
                        self.wall_coordinates[player_position[0] + 1][player_position[1]] == 1:
                    print("You can not move through a wall!")
                    return False
                elif self.player_coordinates[moving_position[0]][moving_position[1]] == 1:
                    print("You can not move on a another player place!")
                    return False
                else:
                    return True
            elif player_position[1] - moving_position[1] == -1:
                if self.wall_coordinates[player_position[0]][player_position[1] + 1] == 1 and \
                        self.wall_coordinates[player_position[0] + 1][player_position[1] + 1] == 1:
                    print("You can not move through a wall!")
                    return False
                elif self.player_coordinates[moving_position[0]][moving_position[1]] == 1:
                    print("You can not move on a another player place!")
                    return False
                else:
                    return True
        else:
            print("Position is too far!")
            return False

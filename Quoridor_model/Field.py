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

    def write_player_location(self, vertical_coordinate: str, horizontal_coordinate: str):
        self.player_coordinates[Parser.parse_number(horizontal_coordinate)][
            Parser.parse_player_letter(vertical_coordinate)] = 1

    def clean_player_location(self, vertical_coordinate: str, horizontal_coordinate: str):
        self.player_coordinates[Parser.parse_number(horizontal_coordinate)][
            Parser.parse_player_letter(vertical_coordinate)] = 0

    def write_wall_creation(self, letter: str, number: str, h_or_v: str):
        center_position = [Parser.parse_number(number) + 1, Parser.parse_wall_letter(letter) + 1]
        self.wall_coordinates[center_position[0]][center_position[1]] = 1
        if h_or_v == "h":
            self.wall_coordinates[center_position[0]][center_position[1] + 1] = 1
            self.wall_coordinates[center_position[0]][center_position[1] - 1] = 1
        if h_or_v == "v":
            self.wall_coordinates[center_position[0] + 1][center_position[1]] = 1
            self.wall_coordinates[center_position[0] - 1][center_position[1]] = 1

    def check_access_move(self, player: Player, letter: str, number: str) -> bool:
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

    def check_access_jump(self, player: Player, letter: str, number: str) -> bool:
        player_position = [Parser.parse_number(player.get_number()), Parser.parse_player_letter(player.get_letter())]
        moving_position = [Parser.parse_number(number), Parser.parse_player_letter(letter)]
        if self.player_coordinates[player_position[0] + 1][player_position[1]] == 1:
            if self.wall_coordinates[player_position[0] + 2][player_position[1]] == 0 or \
                    self.wall_coordinates[player_position[0] + 2][player_position[1] + 1] == 0:
                if player_position[0] + 2 != moving_position[0] and player_position[1] != moving_position[1]:
                    print("You must jump through a player if position is free!")
                    return False
                else:
                    return True
            else:
                if player_position[0] + 1 == moving_position[0] and player_position[1] + 1 == moving_position[1]:
                    if self.wall_coordinates[moving_position[0]][moving_position[1]] == 1 and \
                            self.wall_coordinates[moving_position[0] + 1][moving_position[1]] == 1:
                        print("You can not jump through a wall!")
                        return False
                    else:
                        return True
                elif player_position[0] + 1 == moving_position[0] and player_position[1] - 1 == moving_position[1]:
                    if self.wall_coordinates[moving_position[0]][moving_position[1] + 1] and \
                            self.wall_coordinates[moving_position[0] + 1][moving_position[1] + 1]:
                        print("You can not jump through a wall!")
                        return False
                    else:
                        return True
                else:
                    print("Position is not near another player!")
                    return False
        elif self.player_coordinates[player_position[0] - 1][player_position[1]] == 1:
            if self.wall_coordinates[player_position[0] - 1][player_position[1]] == 0 or \
                    self.wall_coordinates[player_position[0] - 1][player_position[1] + 1] == 0:
                if player_position[0] - 2 != moving_position[0] and player_position[1] != moving_position[1]:
                    print("You must jump through a player if position is free!")
                    return False
                else:
                    return True
            else:
                if player_position[0] - 1 == moving_position[0] and player_position[1] + 1 == moving_position[1]:
                    if self.wall_coordinates[moving_position[0]][moving_position[1]] == 1 and \
                            self.wall_coordinates[moving_position[0] + 1][moving_position[1]] == 1:
                        print("You can not jump through a wall!")
                        return False
                    else:
                        return True
                elif player_position[0] - 1 == moving_position[0] and player_position[1] - 1 == moving_position[1]:
                    if self.wall_coordinates[moving_position[0]][moving_position[1] + 1] and \
                            self.wall_coordinates[moving_position[0] + 1][moving_position[1] + 1]:
                        print("You can not jump through a wall!")
                        return False
                    else:
                        return True
                else:
                    print("Position is not near another player!")
                    return False
        elif self.player_coordinates[player_position[0]][player_position[1] + 1] == 1:
            if self.wall_coordinates[player_position[0]][player_position[1] + 2] == 0 or \
                    self.wall_coordinates[player_position[0] + 1][player_position[1] + 2] == 0:
                if player_position[0] != moving_position[0] and player_position[1] + 2 != moving_position[1]:
                    print("You must jump through a player if position is free!")
                    return False
                else:
                    return True
            else:
                if player_position[0] + 1 == moving_position[0] and player_position[1] + 1 == moving_position[1]:
                    if self.wall_coordinates[moving_position[0]][moving_position[1]] == 1 and \
                            self.wall_coordinates[moving_position[0]][moving_position[1] + 1] == 1:
                        print("You can not jump through a wall!")
                        return False
                    else:
                        return True
                elif player_position[0] - 1 == moving_position[0] and player_position[1] + 1 == moving_position[1]:
                    if self.wall_coordinates[moving_position[0] + 1][moving_position[1]] and \
                            self.wall_coordinates[moving_position[0] + 1][moving_position[1] + 1]:
                        print("You can not jump through a wall!")
                        return False
                    else:
                        return True
                else:
                    print("Position is not near another player!")
                    return False
        elif self.player_coordinates[player_position[0]][player_position[1] - 1] == 1:
            if self.wall_coordinates[player_position[0]][player_position[1] - 1] == 0 or \
                    self.wall_coordinates[player_position[0] + 1][player_position[1] - 1] == 0:
                if player_position[0] != moving_position[0] and player_position[1] - 2 != moving_position[1]:
                    print("You must jump through a player if position is free!")
                    return False
                else:
                    return True
            else:
                if player_position[0] + 1 == moving_position[0] and player_position[1] - 1 == moving_position[1]:
                    if self.wall_coordinates[moving_position[0]][moving_position[1]] == 1 and \
                            self.wall_coordinates[moving_position[0]][moving_position[1] + 1] == 1:
                        print("You can not jump through a wall!")
                        return False
                    else:
                        return True
                elif player_position[0] - 1 == moving_position[0] and player_position[1] - 1 == moving_position[1]:
                    if self.wall_coordinates[moving_position[0] + 1][moving_position[1]] and \
                            self.wall_coordinates[moving_position[0] + 1][moving_position[1] + 1]:
                        print("You can not jump through a wall!")
                        return False
                    else:
                        return True
                else:
                    print("Position is not near another player!")
                    return False
        else:
            print("You don't have any other player near you!")
            return False

    def check_access_create_wall(self, letter: str, number: str, wall_counter: int) -> bool:
        center_position = [Parser.parse_number(number) + 1, Parser.parse_wall_letter(letter) + 1]
        if wall_counter != 10:
            if self.wall_coordinates[center_position[0]][center_position[1]] == 0:
                return True
            else:
                print("You can not create a wall on another wall!")
                return False
        else:
            print("You have already placed all of your walls!")

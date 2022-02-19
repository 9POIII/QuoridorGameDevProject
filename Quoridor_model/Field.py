from Parser import Parser


class Field:
    def __init__(self):
        self.player_coordinates = [[0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0],
                                  [0,0,0,0,0,0,0,0,0]]

        self.wall_coordinates = [[1,1,1,1,1,1,1,1,1,1],
                                [1,0,0,0,0,0,0,0,0,1],
                                [1,0,0,0,0,0,0,0,0,1],
                                [1,0,0,0,0,0,0,0,0,1],
                                [1,0,0,0,0,0,0,0,0,1],
                                [1,0,0,0,0,0,0,0,0,1],
                                [1,0,0,0,0,0,0,0,0,1],
                                [1,0,0,0,0,0,0,0,0,1],
                                [1,0,0,0,0,0,0,0,0,1],
                                [1,1,1,1,1,1,1,1,1,1]]

    def write_player_location(self, vertical_coordinate, horizontal_coordinate):
        self.player_coordinates[Parser.parse_number(horizontal_coordinate)][Parser.parse_player_letter(vertical_coordinate)] = 1

    def clean_player_location (self, vertical_coordinate, horizontal_coordinate):
        self.player_coordinates[Parser.parse_number(horizontal_coordinate)][Parser.parse_player_letter(vertical_coordinate)] = 0

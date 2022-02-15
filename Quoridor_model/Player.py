class Player:

    name = "George"

    coordinates = ["E", "1"]

    def __init__(self, player_name):
        self.name = player_name

    def change_coordinates(self, vertical_coordinate, horizontal_coordinate):
        self.coordinates = [vertical_coordinate, horizontal_coordinate]
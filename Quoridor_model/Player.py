class Player:

    def __init__(self, player_color: str = "White", letter: str = "E", number: str = "1"):
        self.color = player_color
        self.wall_counter = 0
        self.coordinates = [letter, number]

    def get_letter(self):
        return self.coordinates[0]

    def get_number(self):
        return self.coordinates[1]

    def change_coordinates(self, vertical_coordinate: str, horizontal_coordinate: str):
        self.coordinates = [vertical_coordinate, horizontal_coordinate]

class Player:

    def __init__(self, player_name="Greg", letter="E", number="1"):
        self.name = player_name
        self.coordinates = [letter, number]

    def get_letter(self):
        return self.coordinates[0]

    def get_number(self):
        return self.coordinates[1]

    def change_coordinates(self, vertical_coordinate, horizontal_coordinate):
        self.coordinates = [vertical_coordinate, horizontal_coordinate]

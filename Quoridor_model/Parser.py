class Parser:
    player_letter_dic = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8}
    wall_letter_dic = {"S": 0, "T": 1, "U": 2, "V": 3, "W": 4, "X": 5, "Y": 6, "Z": 7}

    @classmethod
    def parse_player_letter(cls, letter) -> int:
        return cls.player_letter_dic[letter]

    @classmethod
    def parse_wall_letter(cls, letter) -> int:
        return cls.wall_letter_dic[letter]

    @staticmethod
    def parse_number(number) -> int:
        return int(number) - 1

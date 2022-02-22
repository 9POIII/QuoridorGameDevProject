from Quoridor import Quoridor
from Player import Player

class InputFunc:

    def player_controller(self, rawInput):
        letter = rawInput[0]
        number = rawInput[1]
        Q.move_player(letter, number)

    def player_choose(self, player_1, player_2):
        if player_1 == 'John':
            player_1 = Player('John')
            player_2 = Player('Smit', "E", "9")
            print('You play by John')
            Q.set_players(player_1, player_2)
            I.player_controller(rawInput = input("Your move: \n"))

        elif player_1 == 'Smit':
            player_1 = Player('John')
            player_2 = Player('John', "E", "9")
            print('You play by Smit')
            Q.set_players(player_1, player_2)
            I.player_controller(rawInput = input("Your move: \n"))

        elif player_1 != 'John' or 'Smit':
            print('error_2')


    def gamemode_choose(self, gamemode):
        self._gamemode = gamemode

        if self._gamemode == 'PvP':
            print('Its PvP')
            I.player_choose(player_1 = input("Please, select your player: John or Smit \n"), player_2= '')

        elif self._gamemode == 'PvE':
            print('Its PvE')
            I.player_choose(player_1 = input("Please, select your player: John or Smit \n"), player_2= '')

        elif self._gamemode != 'PvP' or 'PvE':
            print('error')

P = Player()
Q = Quoridor()
Q.start_game()
I = InputFunc()
I.gamemode_choose(input("Please, select game mode: PvP or PvE \n"))
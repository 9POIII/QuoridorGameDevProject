from Quoridor import Quoridor
from Player import Player
from Field import Field

class InputFunc:
    Q = Quoridor()
    player_1 = Q.first_player
    player_2 = Q.second_player
    current_player = Q.current_player


    def player_controller(self, rawInput):
        try:
            letter = rawInput[5]
            number = rawInput[6]
        except:
            print('error')
            I.player_controller(rawInput=input("Your move: \n"))
        else:
            if rawInput[0] == 'm':
                Q.move_player(letter, number)
                #print('You made a move on ' + letter + number)
                I.player_controller(input("Your move: \n"))

            elif rawInput[0] == 'j':
                Q.jump_player(letter, number)
                #print('You made a jump on ' + letter + number)
                I.player_controller(input("Your move: \n"))

            elif rawInput[0] == 'w':
                wallLetter = rawInput[5]
                wallNumber = rawInput[6]
                h_or_v = rawInput[7]
                Q.create_wall(wallLetter, wallNumber, h_or_v)
                I.player_controller(input("Your move: \n"))
                #print('you put up a wall on ' + letter + number)

            elif rawInput[0] != 'm' or 'j' or 'w':
                print('error')
                I.player_controller(rawInput=input("Your move: \n"))


    def player_choose(self, player_1:Player, player_2:Player):
        global viborIgroka
        if viborIgroka == player_1.color:
            print('You play by ' + viborIgroka)
            Q.set_players(player_1, player_2)
            I.player_controller(rawInput = input("Your move: \n"))

        elif viborIgroka == player_2.color:
            print('You play by ' + viborIgroka)
            Q.set_players(player_2, player_1)
            I.player_controller(rawInput = input("Your move: \n"))

        elif viborIgroka != player_1.color or player_2.color:
            print('error')
            viborIgroka = player_1.color
            I.player_choose(self.player_1, self.player_2)


    def gamemode_choose(self, gamemode):
        global viborIgroka
        self._gamemode = gamemode

        if self._gamemode == 'PvP':
            print('Its PvP')
            viborIgroka = input('Please, select player: White, Black \n')
            I.player_choose(self.player_1, self.player_2)

        elif self._gamemode == 'PvE':
            print('Its PvE')
            viborIgroka = input('Please, select player: White, Black \n')
            I.player_choose(self.player_1, self.player_2)

        elif self._gamemode != 'PvP' or 'PvE':
            print('error')
            I.gamemode_choose(input("Please, select game mode: PvP or PvE \n"))

F = Field()
P = Player()
Q = Quoridor()
Q.start_game()
I = InputFunc()
I.gamemode_choose(input("Please, select game mode: PvP or PvE \n"))
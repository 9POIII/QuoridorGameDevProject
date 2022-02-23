from Quoridor import Quoridor
from Player import Player
from Field import Field

class InputFunc:
    Q = Quoridor()
    player_1 = Q.first_player
    player_2 = Q.second_player
    current_player = Q.current_player


    def player_controller(self, rawInput):

        if rawInput.lower() == 'restart':
            Q.start_game()
            I.gamemode_choose(input("Please, select game mode: PvP or PvE \n"))
        else:
            try:
                letter = rawInput[5]
                number = rawInput[6]
            except:
                print('error')
                I.player_controller(input("Your move: \n"))
            else:
                if rawInput[0].lower() == 'm':
                    Q.move_player(letter, number)
                    print('player placement: ' + str(Q.first_player.coordinates))
                    print('player placement: ' + str(Q.second_player.coordinates))
                    I.player_controller(input("Your move: \n"))

                elif rawInput[0].lower() == 'j':
                    Q.jump_player(letter, number)
                    print('player placement: ' + str(Q.first_player.coordinates))
                    print('player placement: ' + str(Q.second_player.coordinates))
                    I.player_controller(input("Your move: \n"))

                elif rawInput[0].lower() == 'w':
                    wallLetter = rawInput[5]
                    wallNumber = rawInput[6]
                    h_or_v = rawInput[7]
                    Q.create_wall(wallLetter, wallNumber, h_or_v)
                    I.player_controller(input("Your move: \n"))

                elif rawInput[0].lower() != 'm' or rawInput[0].lower() != 'j' or rawInput[0].lower() != 'w':
                    print('error')
                    I.player_controller(rawInput = input("Your move: \n"))



    def player_choose(self, player_1:Player, player_2:Player):
        global viborIgroka
        if viborIgroka.lower() == 'white':
            print('You play by ' + viborIgroka)
            Q.set_players(player_1, player_2)
            I.player_controller(input("Your move: \n"))

        elif viborIgroka.lower() == 'black':
            print('You play by ' + viborIgroka)
            Q.set_players(player_2, player_1)
            I.player_controller(input("Your move: \n"))

        elif viborIgroka.lower() != 'white' or viborIgroka.lower() != 'black':
            print('error')
            viborIgroka = player_1.color
            I.player_choose(self.player_1, self.player_2)


    def gamemode_choose(self, gamemode):
        global viborIgroka
        player_1 = Q.first_player
        player_2 = Q.second_player
        #self._gamemode = gamemode

        if gamemode.lower() == 'pvp':
            print('Its PvP')
            viborIgroka = input('Please, select player: White, Black \n')
            I.player_choose(player_1, player_2)

        elif gamemode.lower() == 'pve':
            print('Its PvE')
            viborIgroka = input('Please, select player: White, Black \n')
            I.player_choose(player_1, player_2)

        elif gamemode.lower() != 'pvp' or gamemode.lower() != 'pve':
            print('error')
            I.gamemode_choose(input("Please, select game mode: PvP or PvE \n"))

F = Field()
P = Player()
Q = Quoridor()
Q.start_game()
I = InputFunc()
I.gamemode_choose(input("Please, select game mode: PvP or PvE \n"))
from Quoridor import Quoridor
from Player import Player
from random import randint, choice

class InputFunc:
    Q = Quoridor()
    player_1 = Q.first_player
    player_2 = Q.second_player
    gamemode = "PvP"
    color_choice = "white"

    def gamemode_choose(self, gamemode):
        self.gamemode = gamemode

        if self.gamemode == 'PvP' or 'pvp':
            print('Its PvP. Now it is white player turn.')
            self.Q.set_players(self.player_1, self.player_2)
            InputFunc.pvp_func(self, rawInput=input("Your move: \n"))

        elif self.gamemode == 'PvE' or 'pve':
            print('Its PvE')
            self.color_choice = input('Please, select player: White, Black \n')
            InputFunc.player_choose(self, self.player_1, self.player_2)

        elif self.gamemode != 'PvP' or 'PvE' or 'pvp' or 'pve':
            print('error')
            InputFunc.gamemode_choose(self, input("Please, select game mode: PvP or PvE \n"))

    def player_choose(self, player_1: Player, player_2: Player):
        if self.color_choice == player_1.color or 'white':
            print('You play by ' + self.color_choice)
            self.Q.set_players(player_1, player_2)
            InputFunc.pve_white_func(self, rawInput=input("Your move: \n"))

        elif self.color_choice == player_2.color or 'black':
            print('You play by ' + self.color_choice)
            self.Q.set_players(player_1, player_2)
            InputFunc.pve_black_func(self, "move E0")

        elif self.color_choice != player_1.color or player_2.color:
            print('error')
            self.color_choice = player_1.color
            InputFunc.player_choose(self, self.player_1, self.player_2)

    def pvp_func(self, rawInput):
        try:
            letter = rawInput[5]
            number = rawInput[6]
        except:
            print('error')
            InputFunc.pvp_func(self, rawInput=input("Your move: \n"))
        else:
            if rawInput[0] == 'm':
                self.Q.move_player(letter, number)
                print(self.Q.current_player.color + ' player made a move on ' + letter + number)
                InputFunc.pvp_func(self, input("Your move: \n"))

            elif rawInput[0] == 'j':
                self.Q.jump_player(letter, number)
                print(self.Q.current_player.color + ' player made a jump on ' + letter + number)
                InputFunc.pvp_func(self, input("Your move: \n"))

            elif rawInput[0] == 'w':
                wallLetter = rawInput[5]
                wallNumber = rawInput[6]
                h_or_v = rawInput[7]
                self.Q.create_wall(wallLetter, wallNumber, h_or_v)
                print(self.Q.current_player.color + ' player put up a wall on ' + letter + number)
                InputFunc.pvp_func(self, input("Your move: \n"))


            elif rawInput[0] != 'm' or 'j' or 'w':
                print('error')
                InputFunc.pvp_func(self, rawInput=input("Your move: \n"))

    def pve_white_func(self, rawInput):
        if self.Q.current_player.color == "Black":
            pass
        else:
            try:
                letter = rawInput[5]
                number = rawInput[6]
            except:
                print('error')
                InputFunc.pve_white_func(self, rawInput=input("Your move: \n"))
            else:
                if rawInput[0] == 'm':
                    self.Q.move_player(letter, number)
                    InputFunc.pve_white_func(self, input("Your move: \n"))

                elif rawInput[0] == 'j':
                    self.Q.jump_player(letter, number)
                    InputFunc.pve_white_func(self, input("Your move: \n"))

                elif rawInput[0] == 'w':
                    wallLetter = rawInput[5]
                    wallNumber = rawInput[6]
                    h_or_v = rawInput[7]
                    self.Q.create_wall(wallLetter, wallNumber, h_or_v)
                    InputFunc.pve_white_func(self, input("Your move: \n"))

                elif rawInput[0] != 'm' or 'j' or 'w':
                    print('error')
                    InputFunc.pve_white_func(self, rawInput=input("Your move: \n"))

    def pve_black_func(self, rawInput):
        if self.Q.current_player.color == "White":
            pass
        else:
            try:
                letter = rawInput[5]
                number = rawInput[6]
            except:
                print('error')
                InputFunc.pve_black_func(self, rawInput=input("Your move: \n"))
            else:
                if rawInput[0] == 'm':
                    self.Q.move_player(letter, number)
                    InputFunc.pve_black_func(self, input("Your move: \n"))

                elif rawInput[0] == 'j':
                    self.Q.jump_player(letter, number)
                    InputFunc.pve_black_func(self, input("Your move: \n"))

                elif rawInput[0] == 'w':
                    wallLetter = rawInput[5]
                    wallNumber = rawInput[6]
                    h_or_v = rawInput[7]
                    self.Q.create_wall(wallLetter, wallNumber, h_or_v)
                    InputFunc.pve_black_func(self, input("Your move: \n"))

                elif rawInput[0] != 'm' or 'j' or 'w':
                    print('error')
                    InputFunc.pve_black_func(self, rawInput=input("Your move: \n"))

    def random_move(self, player: Player):
        type_of_move = randint(0, 2)
        if type_of_move == 0:
            move_randnum = str(randint(1, 9))
            move_randlet = choice(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
            if self.Q.play_field.check_access_move(player, move_randlet, move_randnum):
                self.Q.move_player(move_randlet, move_randnum)
            else:
                self.random_move(player)
        elif type_of_move == 1:
            jump_randnum = str(randint(1, 9))
            jump_randlet = choice(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
            if self.Q.play_field.check_access_jump(player, jump_randlet, jump_randnum):
                self.Q.jump_player(jump_randlet, jump_randnum)
            else:
                self.random_move(player)
        else:
            wall_randnum = str(randint(1, 8))
            wall_randlet = choice(["S", "T", "U", "V", "W", "X", "Y", "Z"])
            wall_rand_h_v = choice(["h", 'v'])
            if self.Q.play_field.check_access_create_wall(player, wall_randlet, wall_randnum):
                self.Q.create_wall(wall_randlet, wall_randnum,wall_rand_h_v)
            else:
                self.random_move(player)


I = InputFunc()
I.gamemode_choose(input("Please, select game mode: PvP or PvE \n"))

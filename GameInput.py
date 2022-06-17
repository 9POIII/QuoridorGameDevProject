from Quoridor import Quoridor
from Player import Player
from random import randint, choice

class InputFunc:
    Q = Quoridor()
    player_1 = Q.first_player
    player_2 = Q.second_player

    def gamemode_choose(self, gamemode):

        if gamemode == 'PvP' or gamemode == 'pvp':
            print('Its PvP. Now it is white player turn.')
            self.Q.start_game()
            self.pvp_func(input("Your move: \n"))

        elif gamemode == 'PvE' or gamemode == 'pve':
            print('Its PvE')
            self.player_choose(input('Please, select player: White, Black \n'))

        elif gamemode != 'PvP' or gamemode != 'PvE' or gamemode != 'pvp' or gamemode != 'pve':
            print('error')
            self.gamemode_choose(input("Please, select game mode: PvP or PvE \n"))

    def player_choose(self, color_choice):
        if color_choice == self.Q.first_player.color or color_choice == 'white':
            print('You play by ' + color_choice)
            self.Q.start_game()
            self.pve_white_func(input("Your move: \n"))

        elif color_choice == self.Q.second_player.color or color_choice == 'black':
            print('You play by ' + color_choice)
            self.Q.start_game()
            self.pve_black_func()

        else:
            print('error')
            self.player_choose(input('Please, select player: White, Black \n'))

    def pvp_func(self, rawInput):
        if self.Q.is_ended:
            return self.game_loop()
        try:
            letter = rawInput[5]
            number = rawInput[6]
        except:
            print('error')
            return self.pvp_func(input("Your move: \n"))
        else:
            if rawInput[0] == 'm':
                print(self.Q.current_player.color + ' player made a move on ' + letter + number)
                self.Q.move_player(letter, number)
                return self.pvp_func(input("Your move: \n"))

            elif rawInput[0] == 'j':
                print(self.Q.current_player.color + ' player made a jump on ' + letter + number)
                self.Q.jump_player(letter, number)
                return self.pvp_func(input("Your move: \n"))

            elif rawInput[0] == 'w':
                wallLetter = rawInput[5]
                wallNumber = rawInput[6]
                h_or_v = rawInput[7]
                print(self.Q.current_player.color + ' player put up a wall on ' + letter + number + h_or_v)
                self.Q.create_wall(wallLetter, wallNumber, h_or_v)
                return self.pvp_func(input("Your move: \n"))


            elif rawInput[0] != 'm' or 'j' or 'w':
                print('error')
                return self.pvp_func(input("Your move: \n"))

    def pve_white_func(self, rawInput="move E1"):
        if self.Q.is_ended:
            return self.game_loop()
        if self.Q.current_player.color == "Black":
            self.random_move(self.Q.current_player)
            return self.pve_white_func(input("Your move: \n"))
        else:
            try:
                letter = rawInput[5]
                number = rawInput[6]
            except:
                print('error')
                return self.pve_white_func(input("Your move: \n"))
            else:
                if rawInput[0] == 'm':
                    print(self.Q.current_player.color + ' player made a move on ' + letter + number)
                    self.Q.move_player(letter, number)
                    return self.pve_white_func()

                elif rawInput[0] == 'j':
                    print(self.Q.current_player.color + ' player made a jump on ' + letter + number)
                    self.Q.jump_player(letter, number)
                    return self.pve_white_func()

                elif rawInput[0] == 'w':
                    wallLetter = rawInput[5]
                    wallNumber = rawInput[6]
                    h_or_v = rawInput[7]
                    print(self.Q.current_player.color + ' player put up a wall on ' + letter + number + h_or_v)
                    self.Q.create_wall(wallLetter, wallNumber, h_or_v)
                    return self.pve_white_func()

                elif rawInput[0] != 'm' or 'j' or 'w':
                    print('error')
                    return self.pve_white_func(input("Your move: \n"))

    def pve_black_func(self, rawInput=""):
        if self.Q.is_ended:
            return self.game_loop()
        if self.Q.current_player.color == "White":
            self.random_move(self.Q.current_player)
            return self.pve_black_func(input("Your move: \n"))
        else:
            try:
                letter = rawInput[5]
                number = rawInput[6]
            except:
                print('error')
                return self.pve_black_func(input("Your move: \n"))
            else:
                if rawInput[0] == 'm':
                    print(self.Q.current_player.color + ' player made a move on ' + letter + number)
                    self.Q.move_player(letter, number)
                    return self.pve_black_func()

                elif rawInput[0] == 'j':
                    print(self.Q.current_player.color + ' player made a jump on ' + letter + number)
                    self.Q.jump_player(letter, number)
                    return self.pve_black_func()

                elif rawInput[0] == 'w':
                    wallLetter = rawInput[5]
                    wallNumber = rawInput[6]
                    h_or_v = rawInput[7]
                    print(self.Q.current_player.color + ' player put up a wall on ' + letter + number + h_or_v)
                    self.Q.create_wall(wallLetter, wallNumber, h_or_v)
                    return self.pve_black_func()

                elif rawInput[0] != 'm' or 'j' or 'w':
                    print('error')
                    return self.pve_black_func(input("Your move: \n"))

    def random_move(self, player: Player):
        type_of_move = randint(0, 2)
        if type_of_move == 0:
            move_randnum = str(randint(1, 9))
            move_randlet = choice(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
            if self.Q.play_field.check_access_move(player, move_randlet, move_randnum):
                print(self.Q.current_player.color + ' player made a move on ' + move_randlet + move_randnum)
                self.Q.move_player(move_randlet, move_randnum)
            else:
                return self.random_move(player)
        elif type_of_move == 1:
            jump_randnum = str(randint(1, 9))
            jump_randlet = choice(["A", "B", "C", "D", "E", "F", "G", "H", "I"])
            if self.Q.play_field.check_access_jump(player, jump_randlet, jump_randnum):
                print(self.Q.current_player.color + ' player made a jump on ' + jump_randlet + jump_randnum)
                self.Q.jump_player(jump_randlet, jump_randnum)
            else:
                return self.random_move(player)
        else:
            wall_randnum = str(randint(1, 8))
            wall_randlet = choice(["S", "T", "U", "V", "W", "X", "Y", "Z"])
            wall_rand_h_v = choice(["h", 'v'])
            if self.Q.play_field.check_access_create_wall(wall_randlet, wall_randnum, player.wall_counter):
                print(self.Q.current_player.color + ' player put up a wall on ' + wall_randlet + wall_randnum + wall_rand_h_v)
                self.Q.create_wall(wall_randlet, wall_randnum,wall_rand_h_v)
            else:
                return self.random_move(player)

    def game_loop(self):
        loop_answer = input("The game has ended! Do you wish to start a new game?:")
        if loop_answer == "yes" or loop_answer == "Yes":
            return InputFunc.gamemode_choose(self, input("Please, select game mode: PvP or PvE \n"))
        if loop_answer == "no" or loop_answer == "No":
            return 0
        else:
            print("Sorry. We could not understand your answer, so we take it as a 'No'.")
            return 0


I = InputFunc()
I.gamemode_choose(input("Please, select game mode: PvP or PvE \n"))

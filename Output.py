import os
from Quoridor import Quoridor

exitprogramm = 0

graphic_board = [["╔", "═", "═", "═", "═", "═", "═", "═", "═", "═", "═", "═", "═", "═", "═", "═", "═", "═", "╗"],
                 ["║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"],
                 ["║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"],
                 ["║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"],
                 ["║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"],
                 ["║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"],
                 ["║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"],
                 ["║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"],
                 ["║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"],
                 ["║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"],
                 ["║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"],
                 ["║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"],
                 ["║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"],
                 ["║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"],
                 ["║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"],
                 ["║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"],
                 ["║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"],
                 ["║", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "║"],
                 ["╚", "═", "═", "═", "═", "═", "═", "═", "═", "═", "═", "═", "═", "═", "═", "═", "═", "═", "╝"]]

white_player_icon = "☻"
black_player_icon = "☺"
horizontal_wall_icon = "═"
vertical_wall_icon = "║"
player_icon = "O"
wall_icon = "█"

def drawBoard():
    os.system('cls')
    graphic_board_temp = graphic_board
    c = 0
    g = 0
    q = 1
    o = 1
    #Получение информациии о столе
    for i in range(len(graphic_board_temp)):
        for j in range(len(graphic_board_temp[i])):
            if i % 2 != 0 and i != 0 and i != 18:
                if j % 2 != 0 and j != 19:
                    graphic_board_temp[i][j] = Quoridor.play_field.player_coordinates[c][g]
                    if g != 8:
                        g += 1
                    else:
                        c += 1
                        g -= 8
            if not i & 1 and i != 0 and i != 18:
                if not j & 1 and j != 0 and j != 18:
                    graphic_board_temp[i][j] = Quoridor.play_field.wall_coordinates[q][o]
                    if o != 8:
                        o += 1
                    else:
                        q += 1
                        o -= 7

# Отрисовка стола
    print("╔" + "═" * 19 + "╗", end=' ')
    for i in range(len(graphic_board_temp)):
        for j in range(len(graphic_board_temp[i])):
            if i % 2 != 0 and i != 0 and i != 18:
                if j % 2 != 0 and j != 19:
                    if graphic_board_temp[i][j] == 1:
                        print(player_icon, end=' ')
                    elif graphic_board_temp[i][j] == 0:
                        print("·", end=' ')
            if not i & 1 and i != 0 and i != 18:
                if not j & 1 and j != 0 and j != 18:
                    if graphic_board_temp[i][j] == 1:
                        print(wall_icon, end=' ')
                    elif graphic_board_temp[i][j] == 0:
                        print(" ", end=' ')
            if i % 2 != 0 and i != 0 and i != 18 and j == 0:
                print(" ", end=' ')
            if not i & 1 != 0 and i != 0 and i != 18 and j == 0:
                print("  ", end=' ')
        if i != 18:
            print()
    print("╚" + "═" * 19 + "╝", end='\n')

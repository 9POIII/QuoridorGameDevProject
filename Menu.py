import os
from GameInput import InputFunc
import getpass

exitprogramm = 0

def mainmenu():
    os.system('cls')
    print("Welcome you in game Quoridor!\n")
    print("WARNING! This version of the game is an alpha. Therefore, there may be some errors during the game.\n")
    print("Start the game (Enter 1)")
    print("How to play (Enter 2)")
    print("Rules of the game (Enter 3)")
    print("Credits (Enter 4)")
    print("Exit from game (Enter 5)")
    answer = input()
    if answer == "1":
        gamemode()
    elif answer == "2":
        gamecommands()
    elif answer == "3":
        gamerule()
    elif answer == "4":
        authors()
    elif answer == "5":
        os.system('cls')
        print("It was nice to deal with you, " + getpass.getuser())
        global exitprogramm
        exitprogramm = 1
    else:
        os.system('cls')
        print("You have entered an incorrect value. Please enter the correct value.")
        print("(Press Enter button to exit this menu)")
        input()

def gamecommands():
    os.system('cls')
    print("How to play\n")
    print("The game is controlled by commands \"move\", \"jump\" and \"wall\"\n")
    print("About command \"move\" (Enter 1)")
    print("About command \"jump\" (Enter 2)")
    print("About command \"wall\" (Enter 3)")
    print("Back (Enter 4)")
    answer = input()
    if answer == "1":
        os.system('cls')
        print("How to play\n")
        print("Command \"move\"")
        print("Used to move your chip around the cells")
        print("To use this command, you need to enter the command itself (\"move\") and the coordinates on which you want to put your chip\n")
        print("Example:\n\"move F6\"\nWhite player made a move on F6\n")
        print("(Press Enter button to back)")
        input()
        gamecommands()
    elif answer == "2":
        os.system('cls')
        print("How to play\n")
        print("Command \"jump\"")
        print("Used to jump over another player")
        print("To use this command, you need to enter the command itself (\"jump\") and the coordinates on which you want to put your chip\n")
        print("Example:\n\"jump C3\"\nBlack player made a jump on C3\n")
        print("(Press Enter button to back)")
        input()
        gamecommands()
    elif answer == "3":
        os.system('cls')
        print("How to play\n")
        print("Command \"wall\"")
        print("Used to set up a wall to obstruct another player")
        print("To use this command, you need to enter the command itself (\"wall\"), the coordinates and wall orientation (\"h\" or \"v\") which you want to put your wall\n")
        print("Example:\n\"wall v4h\"\nWhite player put up a wall on v4h2\n")
        print("(Press Enter button to back)")
        input()
        gamecommands()
    elif answer == "4":
        os.system('cls')
        mainmenu()
    else:
        os.system('cls')
        print("You have entered an incorrect value. Please enter the correct value.")
        print("(Press Enter button to exit this menu)")
        input()
        gamecommands()

def gamemode():
    os.system('cls')
    print("Please select a gamemode\n")
    print("Game against the player [PvP] (Enter 1)")
    print("Game against the computer [PvE] (Enter 2)")
    print("Back (Enter 3)")

    answer = input()
    if answer == "1":
        os.system('cls')
        InputFunc().gamemode_choose("pvp")
    elif answer == "2":
        os.system('cls')
        InputFunc().gamemode_choose("pve")
    elif answer == "3":
        os.system('cls')
        mainmenu()
    else:
        os.system('cls')
        print("You have entered an incorrect value. Please enter the correct value.")
        print("(Press Enter button to exit this menu)")
        input()
        gamemode()


def gamerule():
    os.system('cls')
    print("Rules of the game:\n")
    print("The player's task is to hold his chip to the opposite side. Whoever managed to do it first, wins. You can only move the chip vertically or horizontally.\nIf you have a wall on the way, you will have to go around it. Instead of moving, you can put an wall on the field from your stock.\n")
    print("(Press Enter button to exit this menu)")
    input()


def authors():
    os.system('cls')
    print("It was created by a team \"LIC\"\n")
    print("He was responsible for creating the model component:")
    print("Mikitenko Vsevolod\n")
    print("He was responsible for creating the input component:")
    print("Richtik Daniel\n")
    print("Responsible for creating the output component:")
    print("Bratishko Olexander\n")
    print("(Press Enter button to exit this menu)")
    input()

while exitprogramm == 0:
    mainmenu()

from player import *
#import main as main
import input as input_local
import ai as ai


def main_menu():
    print('Welcome to the Simple Roulette!')
    list_option = ["Start game", "Settings", "Exit game"]

    option = input_local.input_select(list_option)

    if option == 1:
        game()
    if option == 2:
        print('Settings - Not implemented')
    if option == 3:
        print('Return to main menu - Not implemented')
        #main.main_menu()


def game():
    ai_player = ComputerPlayer(1000, 1)
    ai.martingale(ai_player, 0)

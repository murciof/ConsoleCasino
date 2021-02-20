from game import *


def main_menu():
    list_games = [Game('Simple Roulette'), Game('Test')]
    print('Welcome to the Console Casino!')
    print('Main menu')
    game_select(list_games)


main_menu()

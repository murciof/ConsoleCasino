import input as input_local

import games.simple_roulette.game as simple_roulette


class Game:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


def game_select(games):

    option = input_local.input_select(games)

    if option == 1:
        simple_roulette.main_menu()
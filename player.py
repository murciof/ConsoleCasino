class Player:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def bet(self, money):
        self._balance -= money

    def win(self, money):
        self._balance += money

    def print_name(self):
        print(str(self._name))

    def print_balance(self):
        print(str(self._balance))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance


class ComputerPlayer(Player):
    def __init__(self, balance, ai):
        super().__init__('Computer', balance)
        self._ai = ai
        self._last_game = False

    @property
    def last_game(self):
        return self._last_game

    @last_game.setter
    def last_game(self, last_game):
        self._last_game = last_game

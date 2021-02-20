class TableCell:
    def __init__(self, number, color):
        self._number = number
        self._color = color

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @property
    def color(self):
        return self._color

    @color.setter
    def number(self, color):
        self._color = color


# Work in progress
def init_roulette_table(table):
    print('Initializing Roulette Table')
    number = 1
    for i in range(12):
        line = []
        for j in range(3):
            line.append(TableCell(number, 1))
            #print(line[j].number)
            #print(number)
            number += 1
        table.append(line)


def display_roulette_table(table):
    for i, line in enumerate(table):
        for j, column in enumerate(table[i]):
            print(table[i][j].number, end=' ')
        print('\n', end='')
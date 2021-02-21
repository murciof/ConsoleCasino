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
    def color(self, color):
        self._color = color


def init_roulette_table(table):
    number = 1
    color = False  # Boolean value for table colors: False for Red | True for Black
    for i in range(12):
        line = []
        for j in range(3):
            if (i < 3) or (i > 8):
                if j == 0 and (i == 0 or i == 9):
                    color = False
                if ((j > 0 and (i == 0 or i == 9)) or (i != 0 and i != 9)) and color is False:
                    color = True
                else:
                    color = False
            else:
                if j < 2 and (i == 3 or i == 6):
                    color = True
                if ((j > 1 and (i == 3 or i == 6)) or (i != 3 and i != 6)) and color is True:
                    color = False
                else:
                    color = True
            line.append(TableCell(number, color))
            number += 1
        table.append(line)


def display_roulette_table(table):
    for i, line in enumerate(table):
        for j, column in enumerate(table[i]):
            if table[i][j].number < 10:
                if table[i][j].color is False:
                    print(str(table[i][j].number).zfill(2), 'R', sep='', end=' ')
                else:
                    print(str(table[i][j].number).zfill(2), 'B', sep='', end=' ')
            else:
                if table[i][j].color is False:
                    print(table[i][j].number, 'R', sep='', end=' ')
                else:
                    print(table[i][j].number, 'B', sep='', end=' ')
        print('\n', end='')


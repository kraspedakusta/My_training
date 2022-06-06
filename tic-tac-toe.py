class Field:

    def __init__(self, value_of_column):
        self.value_of_column = value_of_column
        self.field = []

    def create_field(self):
        for i in range(self.value_of_column):
            self.field.append([0] * self.value_of_column)
        return self.field

    def show_field(self):
        self.border_line()
        for i in range(self.value_of_column):
            for j in range(self.value_of_column):
                print('|', end=' ')
                print(self.field[i][j], end=' ')
            print('|')
            self.border_line()

    def border_line(self):
        for i in range(self.value_of_column):
            print(' ---', end='')
        print('')


class Game:
    def __init__(self, value_of_column, win_count):
        self.account_1st = None
        self.account_2nd = None
        self.win_count = win_count
        self.move_counter = 0
        self.value_of_column = value_of_column
        self.winner = ''
        self.Field = Field(self.value_of_column)
        self.Field.create_field()
        self.Field.show_field()

    def game_proccess(self):
        account_1st_name = input('Input name 1st player:')
        account_1st_symbolvalue = GameSymbol(input('Input symbol 1st player:'))
        account_2nd_name = input('Input name 2nd player:')
        account_2nd_symbolvalue = GameSymbol(input('Input symbol 2nd player:'))
        self.account_1st = Account(account_1st_name, account_1st_symbolvalue.symbolvalue)
        self.account_2nd = Account(account_2nd_name, account_2nd_symbolvalue.symbolvalue)
        while True:
            x, y = map(int, input(f'{self.account_1st.name} select cordinate x,y:', ).split())
            self.make_move(x, y, self.account_1st.symbolvalue)
            self.Field.show_field()
            self.move_counter += 1
            if self.move_counter >= self.win_count:
                if self.check_win(self.account_1st.symbolvalue) == self.account_1st.symbolvalue:
                    print(f'Winner - {self.account_1st.name}')
                    break
            x, y = map(int, input(f'{self.account_2nd.name} select cordinate x,y:', ).split())
            self.make_move(x, y, self.account_2nd.symbolvalue)
            self.Field.show_field()
            if self.move_counter >= self.win_count:
                if self.check_win(self.account_2nd.symbolvalue) == self.account_2nd.symbolvalue:
                    print(f'Winner - {self.account_2nd.name}')
                    break

    def check_win_combination_in_a_row(self, symbol):
        counter = 0
        for i in self.Field.field:
            for j in i:
                if j == symbol:
                    counter += 1
                else:
                    counter = 0
                if counter == self.win_count:
                    return True

    def check_win_combination_in_a_cell(self, symbol):
        counter = 0
        for i in range(self.Field.value_of_column):
            for j in self.Field.field:
                if j[i] == symbol:
                    counter += 1
                else:
                    counter = 0
                if counter == self.win_count:
                    return True

    def check_win_combination_in_a_diagonal_from_start_to_end(self, symbol, number_of_row):
        counter = 0
        for i in range(number_of_row, self.Field.value_of_column):
            diagonal_shift = i
            for j in self.Field.field[number_of_row:len(self.Field.field) - diagonal_shift]:
                print('*start_to_end*')
                print(self.Field.field[number_of_row:len(self.Field.field) - diagonal_shift])
                print (j)
                print(diagonal_shift)
                print(j[diagonal_shift])
                if j[diagonal_shift] == symbol:
                    counter += 1
                else:
                    counter = 0
                if counter == self.win_count:
                    return True
                diagonal_shift += 1

    def check_win_combination_in_a_diagonal_from_end_to_start(self, symbol, number_of_row):
        counter = 0
        for i in range(number_of_row, self.Field.value_of_column, -1):
            diagonal_shift = i
            for j in self.Field.field[number_of_row:len(self.Field.field) - diagonal_shift, -1]:
                print('*end_to_start*')
                print(self.Field.field[number_of_row:len(self.Field.field) - diagonal_shift])
                print(j)
                print(diagonal_shift)
                print(j[diagonal_shift])
                if j[diagonal_shift] == symbol:
                    counter += 1
                else:
                    counter = 0
                if counter == self.win_count:
                    return True
                diagonal_shift += 1

    def check_win_comination_in_a_diagonals(self, symbol):
        for i in range(self.Field.value_of_column):
            if self.check_win_combination_in_a_diagonal_from_start_to_end(symbol, i) is True:
                return True
            if self.check_win_combination_in_a_diagonal_from_end_to_start(symbol, i) is True:
                return True

    def check_win(self, symbol):
        if self.check_win_combination_in_a_row(symbol) or self.check_win_combination_in_a_cell(symbol) or self.check_win_comination_in_a_diagonals(symbol):
            return symbol

    def make_move(self, coordinate_x, coordinate_y, value):
        self.Field.field[coordinate_x][coordinate_y] = value


class GameSymbol:
    def __init__(self, symbolvalue):
        self.symbolvalue = symbolvalue


class Account:
    def __init__(self, name, symbolvalue):
        self.name = name
        self.symbolvalue = symbolvalue


a = Game(5, 3)
a.game_proccess()

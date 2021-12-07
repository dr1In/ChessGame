import os
from classModule import *
from os import kill, system

def main():
    team_now = 'black'
    Running = True
    board = Board(First_realize())
    board.show()
    
    movements = {
        'pawn': Pawn_movement
    }


    #print(board.get_figures_coords())
    print('Пример хода: a2 a4')

    while Running:
        if team_now == 'black': team_now = 'white'
        else: team_now = 'black'

        cur_place, want = map(str, input('Ход команды {}: '.format(team_now)).split())
        while want not in movements[board.get_figure_type_on_place(cur_place)](cur_place, team_now, board.get_figures_coords()):
            print('Невозможный ход, повторите попытку: ')
            cur_place, want = map(str, input().split())
        else: board.swap(cur_place, want, False)

        system('CLS')
        board.show()

    print('Игра окончена')


if __name__ == '__main__':
    main()
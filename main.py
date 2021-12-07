from classModule import *
from os import system

def main():
    team_now = 'black'
    Running = True
    board = Board(First_realize())
    board.show()
    print('Пример хода: a2 a4')

    while Running:
        if team_now == 'black': team_now = 'white'
        else: team_now = 'black'

        cur_place, want = map(str, input('Ход команды {}: '.format(team_now)).split())
        print(cur_place, want)
            

    print('Игра окончена')


if __name__ == '__main__':
    main()
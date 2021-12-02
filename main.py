from classModule import *

def main():
    Running = True
    board = Board(
        Team_init(),
        First_realize(),
        {'white': [3, 7], 'black': [3, 0]})
    Board_view_decorate(board.update())
    print('Пример хода: <pa2 f5>, Сдаться <0>')
    while Running:
        step = input('Ваш ход: ')
        if step == '0':
            print('Противник сдался')
            Running = False

    print('Игра окончена')


if __name__ == '__main__':
    main()
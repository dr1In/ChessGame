from classModule import *

def main():
    all_possible_steps = {
        'pawn': Pawn_movement
    }
    (Running, team_now) = (True, 'black')
    board = Board(
        Team_init(),
        First_realize(),
        {'white': [3, 7], 'black': [3, 0]})
    Board_view_decorate(board.update())
    print('Пример хода: <a2 f5>, Сдаться <0>')
    while Running:
        if team_now == 'black': team_now = 'white'
        elif team_now  == 'white': team_now = 'black'

        step = input('Ваш ход: ')
        if step == '0':
            print('Противник сдался')
            Running = False
        step = list(step.split())
        current_place = {'x': step[0][0], 'y': int(step[0][-1]) - 1}
        ft = board.get_figure_type_on_place(current_place)
        qq = all_possible_steps[ft](current_place, team_now, board.get_figures_coords())
        print(qq)
            

    print('Игра окончена')


if __name__ == '__main__':
    main()
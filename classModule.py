from os import system


x_axis = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y_axis = ['1', '2', '3', '4', '5', '6', '7', '8']

class Board():
    def __init__(self, coords: dict()):
        self.figures_coords = coords
    
    def show(self):
        for_show = [[None for _ in range(8)] for __ in range(8)]
        for y in range(8):
            for x in range(8):
                if self.figures_coords[y_axis[y]][x_axis[x]] is None: for_show[y][x] = '   '
                else: for_show[y][x] = self.figures_coords[y_axis[y]][x_axis[x]].get_symbol()
        Board_view_decorate(for_show)
        
    def get_figures_coords(self):
        return self.figures_coords

    def get_kings_position(self):
        pass

    def get_figure_type_on_place(self, place: str()):
        return self.figures_coords[place[-1]][place[0]].get_type()

    def swap(self, cur_place: str(), new_place: str(), kill: bool()):
        if not kill:
            self.figures_coords[new_place[-1]][new_place[0]] = self.figures_coords[cur_place[-1]][cur_place[0]]
            self.figures_coords[cur_place[-1]][cur_place[0]] = None


class Figure():
    def __init__(self, figure_type: str(), team: str(), symbol: str()):
        self.type = figure_type
        self.team = team
        self.symbol = symbol

    def get_team(self):
        return self.team

    def get_type(self):
        return self.type

    def get_symbol(self):
        return self.symbol


def Team_init():
    figuresWhite = {
        'king': ' ♔ ',
        'queen': ' ♕ ',
        'rook': ' ♖ ',
        'bishop': ' ♗ ',
        'knight': ' ♘ ',
        'pawn': ' ♙ '
        }
    figuresBlack = {
        'king': ' ♚ ', 
        'queen': ' ♛ ',
        'rook': ' ♜ ',
        'bishop': ' ♝ ',
        'knight': ' ♞ ',
        'pawn': ' ♟︎ '
        }
    return {'white': figuresWhite, 'black': figuresBlack}


def First_realize():
    symboles = Team_init()
    coords = {f'{__ + 1}': {chr(97 + _): None for _ in range(8)} for __ in range(8)}
    helper = ['rook', 'knight', 'bishop','king','queen','bishop','knight', 'rook']
    for x in zip(x_axis, helper):
        coords['1'][x[0]] = Figure(x[-1], 'black', symboles['black'][x[-1]])
        coords['2'][x[0]] = Figure('pawn', 'black', symboles['black']['pawn'])
        coords['7'][x[0]] = Figure('pawn', 'white', symboles['white']['pawn'])
        coords['8'][x[0]] = Figure(x[-1], 'white', symboles['white'][x[-1]])

    return coords


def Board_view_decorate(current_view: list()):
    line_spacing = '   ' + '+---' * 8 + '+'
    for line in range(len(current_view)):
        print(line_spacing)
        print(' {} '.format(line + 1) + '|' + '|'.join(current_view[line]) + '|')
    print(line_spacing)
    print('     A   B   C   D   E   F   G   H  ')    


def Pawn_movement(place: dict(), team: str(), all_coords: list()):
    (x, y, moves) = (place[0], int(place[-1]), [])
    if team == 'white':
        if y == 7:
            if all_coords[f'{y - 1}'][x] is None and all_coords[f'{y - 2}'][x] is None:
                moves.append(x + f'{y - 1}')
                moves.append(x + f'{y - 2}')
        if y < 7 and all_coords[f'{y - 1}'][x] is None:
            moves.append(x + f'{y - 1}')
    else:
        if y == 2:
            if all_coords[f'{y + 1}'][x] is None and all_coords[f'{y + 2}'][x] is None:
                moves.append(x + f'{y + 1}')
                moves.append(x + f'{y + 2}')
        if y > 2 and all_coords[f'{y + 1}'][x] is None:
            moves.append(x + f'{y + 1}')


    return moves
class Board():
    def __init__(self, view: list(), coords: list(), kings: dict()):
        self.view = view
        self.figures_coords = coords
    
    def update(self):
        for_show = [[None for _ in range(8)] for __ in range(8)]
        for y in range(8):
            for x in range(8):
                if self.figures_coords[x][y] != None: for_show[x][y] = self.view[self.figures_coords[x][y].get_team()][self.figures_coords[x][y].get_type()]
                else: for_show[x][y] = '   '
        return for_show

    def get_figures_coords(self):
        print(self.figures_coords)

    def get_kings_position(self):
        pass


class Figure():
    def __init__(self, position: list(), figure_type: str(), team: str()):
        self.position = position
        self.type = figure_type
        self.team = team

    def get_team(self):
        return self.team

    def get_type(self):
        return self.type


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
    coords = [[None for _ in range(8)] for __ in range(8)]
    inithelper = ['rook', 'knight', 'bishop','king','queen','bishop','knight', 'rook', 'pawn']
    for x in range(8):
        coords[0][x] = Figure([x, 0], inithelper[x], 'black')
        coords[1][x] = Figure([x, 1], inithelper[-1], 'black')
        coords[8-1][x] = Figure([x, 0], inithelper[x], 'white')
        coords[8-2][x] = Figure([x, 1], inithelper[-1], 'white')
    return coords


def Board_view_decorate(current_view: list()):
    line_spacing = '   ' + '+---' * 8 + '+'
    for line in range(len(current_view)):
        print(line_spacing)
        print(' {} '.format(line + 1) + '|' + '|'.join(current_view[line]) + '|')
    print(line_spacing)
    print('     A   B   C   D   E   F   G   H  ')    


def Pawn_movement(current_place: list(), team: str()):
    max_move = 0
    if team == 'white':
        if 
def horse(cell):
    alpha = 'abcdefgh'
    moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    x = alpha.find(cell[0]) + 1
    y = int(cell[1])
    for xy in moves:
        x1, y1 = x + xy[0], y + xy[1]
        if 0 < x1 < 9 and 0 < y1 < 9:
            print(f'{alpha[x1-1]}{y1}')
 
horse('a3')
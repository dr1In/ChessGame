def Xunconvert(x: str()):
    xlable = {f'{chr(i + 97)}': i for i in range(8)}
    return xlable[x]


def Xconvert(x: str()):
    xlable = {i: f'{chr(i + 97)}' for i in range(8)}
    return xlable[x]


def Pawn_movement(current_place: dict(), team: str()):
    moves = []
    if team == 'white':
        if current_place['y'] <= 6:
            moves.append(Xconvert(current_place['x']) + str(current_place['y'] - 1))
        elif current_place['y'] > 6:
            moves.append(Xconvert(current_place['x']) + str(current_place['y'] - 1))
            moves.append(Xconvert(current_place['x']) + str(current_place['y'] - 2))
    return moves

print(Pawn_movement({'x': 4, 'y': 5}, 'white'))
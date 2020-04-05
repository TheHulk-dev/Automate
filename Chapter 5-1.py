#! python3

# Validateur de dictionnaire d'échec

test = {'1h': 'bking', '6c': 'wqueen',
        '2h': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
pieces = ('wking', 'wqueen', 'wrook', 'wbishop', 'wknight', 'wpawn',
          'bking', 'bqueen', 'brook', 'bbishop', 'bknight', 'bpawn')
row = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
column = tuple(range(1, 9))


def isValidChessBoard(board):
    nbRoiBlanc, nbRoiNoir, nbPiontBlancs, nbPionsNoirs, nbPicesBlanches, nbPiecesNoires = (0,0,0,0,0,0)
    
    # Positions sur le plateau
    for m, p in board.items():
        if (int(m[0]) not in column) or (m[1] not in row) or (p not in pieces):
            print(m[0], m[1])
            print('Pas sur le plateau')
            return False

    # 1 roi noir et 1 roi blanc
    for p in board.values():
        if p == 'wking':
            nbRoiBlanc += 1
        if p == 'bking':
            nbRoiNoir += 1
    if nbRoiBlanc != 1 or nbRoiNoir != 1:
        print('Pas le bon nombre de roi')
        return False

    # Nombre de pions 8 max
    for p in board.values():
        if p == 'wpawn':
            nbPiontBlancs += 1
        if p == 'bpawn':
            nbPionsNoirs += 1
    if nbPiontBlancs > 8 or nbPionsNoirs > 8:
        print('Trop de pions')
        return False

    # Nombre de pièces 16 max
    for p in board.values():
        if p[0] == 'w':
            nbPicesBlanches += 1
        if p[0] == 'b':
            nbPiecesNoires += 1
    if nbPicesBlanches > 8 or nbPicesBlanches > 8:
        print('Trop de pièces')
        return False

    # Si tout va bien, return True
    return True


print(isValidChessBoard(test))

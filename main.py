from copy import deepcopy

from change import show
kx=3
ky=7
board = [
    ['wr', 'wn', 'wb', 'wk', 'wq', 'wb', 'wn', 'wr'],
    ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['__', '__', '__', '__', '__', '__', '__', '__'],
    ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
    ['br', 'bn', 'bb', 'bk', 'bq', 'bb', 'bn', 'br'],
]
boardcopy=deepcopy(board)
Turn = True

def cord(y1, y2):
    return (6 - y1, 6 - y2)


def output():
    a = 7
    for i in board:
        print(a, *i)
        a -= 1
    print('  1  2  3  4  5  6  7  8')


def change(x2, y2, figure):
    board[y2][x2] = figure
    return figure


def pawngo(x1, y1, x2, y2):
    if 'b' in board[y2][x2]:
        return False

    if y2 == 0:
        figure = show()
        return figure, True
    elif y2 == 4 and y1 == 6 and x1 == x2 and board[y2][x1] == '__' and not ischeck(kx,ky):
        board[6][x1] = '__'
        board[4][x1] = 'bp'
        if ischeck(kx,ky):
            board[6][x1] = 'bp'
            board[4][x1] = '__'
            return False
        return True
        # 2 moves
    elif y1 - y2 == 1 and x2 == x1 and board[y2][x1] == '__' and not ischeck(kx,ky):
        board[y1][x1] = '__'
        board[y2][x2] = 'bp'
        if ischeck(kx,ky):
            board[y1][x1] = 'bp'
            board[y2][x2] = '__'
            return False
        return True
        # 1 move
    elif y1 - y2 == 1 and x2 - x1 == 1 and board[y2][x2] != '__' and not ischeck(kx,ky):
        board[y1][x1] = '__'
        board[y2][x2] = 'bp'
        if ischeck(kx,ky):
            board[y1][x1] = 'bp'
            board[y2][x2] = '__'
            return False
        return True
        # eat move
    else:
        return False


def rook(x1, y1, x2, y2):
    if 'b' in board[y2][x2]:
        return False

    if y1 == y2 and x1 != x2:
        move = True
        for i in range(min(x1, x2) + 1, max(x1, x2)):
            if board[y1][i] != '__' and i != x1:
                move = False
                break
        if move:
            board[y1][x1] = '__'
            board[y2][x2] = 'br'
            if ischeck(kx,ky):
                board[y1][x1] = 'br'
                board[y2][x2] = '__'
                return False
    elif x1 == x2 and y1 != y2:
        move = True
        for i in range(min(y1, y2) + 1, max(y1, y2)):
            if board[i][x1] != '__' and i != y1:
                move = False
                break

        if move:
            board[y1][x1] = '__'
            board[y2][x2] = 'br'
            if ischeck(kx,ky):
                board[y1][x1] = 'br'
                board[y2][x2] = '__'
                return False
    return move


def bishop(x1, y1, x2, y2):
    if 'b' in board[y2][x2]:
        return False
    if abs(x1 - x2) == abs(y1 - y2):
        b = True
        m = [y for y in range(min(y1, y2) + 1, max(y1, y2) - 1)]
        if len(m) == 0:
            m.append(y2)
        c = m[0]
        for i in range(min(x2, x1) + 1, max((x1, x2)) - 1):
            print(board[c][i])
            if board[c][i] != '__':
                b = False
                break
            c += 1
        if b != False:
            board[y2][x2] = 'bb'
            board[y1][x1] = "__"
            if ischeck(kx,ky):
                board[y2][x2] = '__'
                board[y1][x1] = "bb"
                return False
    return b


def knight(x1, y1, x2, y2):

    if 'w' in board[y2][x2]:
        return False

    if (abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or (abs(x1 - x2) == 2 and abs(y1 - y2) == 1):
        board[y1][x1] = '__'
        board[y2][x2] = 'bn'
        if ischeck(kx,ky):
            board[y1][x1] = 'bn'
            board[y2][x2] = '__'
            return False
        return True
    else:
        return False


def queen(x1, y1, x2, y2):

    if 'b' in board[y2][x2]:
        return False
    move = True

    if y1 == y2 and x1 != x2:

        for i in range(min(x1, x2) + 1, max(x1, x2)):
            if board[y1][i] != '__' and i != x1:
                move = False
                break
        if move:
            board[y1][x1] = '__'
            board[y2][x2] = 'bq'
    elif x1 == x2 and y1 != y2:

        for i in range(min(y1, y2) + 1, max(y1, y2)):
            if board[i][x1] != '__' and i != y1:
                move = False
                break
        if move:
            board[y1][x1] = '__'
            board[y2][x2] = 'bq'
    else:
        if abs(x1 - x2) == abs(y1 - y2):
            b = True
            m = [y for y in range(min(y1, y2) + 1, max(y1, y2) - 1)]
            if len(m) == 0:
                m.append(y2)
            c = m[0]
            print(c)
            for i in range(min(x2, x1) + 1, max((x1, x2)) - 1):
                print(board[c][i])
                if board[c][i] != '__':
                    b = False
                    break
                c += 1
            if b:
                board[y2][x2] = 'bq'
                board[y1][x1] = "__"
            else:
                move = False
        else:
            move = False
    if move:
        if ischeck(kx,ky):
            board[y2][x2] = '__'
            board[y1][x1] = "bq"
            move=False
    return move

def king(x1,y1,x2,y2):
    global kx, ky


    if 'w' not in board[y2][x2]:
        if ((abs(x1-x2)==1 and abs(y1-y2)==1) or (abs(x1-x2)==1 and abs(y1-y2)==0) or (abs(x1-x2)==0 and abs(y1-y2)==1)) and not ischeck(x2,y2):
            board[y1][x1]='__'
            board[y2][x2]='bk'
            kx=x2
            ky=y2
            return True
    return False
def ischeck(x, y):
    # returns True if check exist
    try:
        if board[y-1][x+1]=='wp' or board[y-1][x-1]=='wp':
            return True
    except:
        pass
    try:
        if board[y+1][x+1]=='wk' or board[y-1][x-1]=='wk' or board[y-1][x+1]=='wk' or board[y+1][x-1]=='wk' or board[y][x+1]=='wk' or board[y][x-1]=='wk'or board[y+1][x]=='wk' or board[y-1][x]=='wk':
            return True
    except:
        pass
    x, y = y, x
    try:
        if board[x + 1][y + 2] == 'wn':
            return True
    except:
        pass
    try:
        if board[x + 2][y + 1] == 'wn':
            return True
    except:
        pass
    try:
        if board[x + 2][y - 1] == 'wn':
            return True
    except:
        pass
    try:
        if board[x + 1][y - 2] == 'wn':
            return True
    except:
        pass
    try:
        if board[x - 1][y - 2] == 'wn':
            return True
    except:
        pass
    try:
        if board[x - 2][y - 1] == 'wn':
            return True
    except:
        pass
    try:
        if board[x - 2][y + 1] == 'wn':
            return True
    except:
        pass
    try:
        if board[x - 2][y - 1] == 'wn':
            return True
    except:
        pass
    try:
        if board[x - 2][y - 1] == 'wn':
            return True
    except:
        pass
    try:
        if board[x - 1][y + 2] == 'wn':
            return True
    except:
        pass
    x, y = y, x
    for i in range(x-1, -1, -1):
        if 'b' in board[y][i] or board[y][i] == 'wn' or board[y][i] == 'wp' or board[y][i] == 'wk' or board[y][i] == 'wb':
            break
        if board[y][i] == 'wq' or board[y][i] == 'wr':
            return True
    for i in range(x+1, 8):
        if 'b' in board[y][i] or board[y][i] == 'wn' or board[y][i] == 'wp' or board[y][i] == 'wk' or board[y][i] == 'wb':
            break
        if board[y][i] == 'wq' or board[y][i] == 'wr':
            return True
    for i in range(y-1, -1, -1):
        if 'b' in board[i][x] or board[i][x] == 'wn' or board[i][x] == 'wp' or board[i][x] == 'wk' or board[i][x] == 'wb':

            break
        if board[i][x] == 'wq' or board[i][x] == 'wr':
            return True
    for i in range(y+1, 8):
        if 'b' in board[i][x] or board[i][x] == 'wn' or board[i][x] == 'wp' or board[i][x] == 'wk' or board[i][x] == 'wb':

            break
        if board[i][x] == 'wq' or board[i][x] == 'wr':
            return True
    x1, y1 = x, y
    while x1 < 8 and y1 < 8:
        if 'b' in board[y1][x1]:
            break
        if board[y1][x1] == 'bq' or board[y1][x1] == 'bb':
            return True
        x1 += 1
        y1 += 1
    x1, y1 = x, y
    while x1 >= 0 and y1 >= 0:
        if 'b' in board[y1][x1]:
            break
        if board[y1][x1] == 'bq' or board[y1][x1] == 'bb':
            return True
        x1 -= 1
        y1 -= 1
    x1, y1 = x, y
    while x1 < 8 and y1 >= 0:
        if 'b' in board[y1][x1]:
            break
        if board[y1][x1] == 'bq' or board[y1][x1] == 'bb':
            return True
        x1 += 1
        y1 -= 1
    x1, y1 = x, y
    while x1 >= 0 and y1 < 8:
        if 'b' in board[y1][x1]:
            break
        if board[y1][x1] == 'bq' or board[y1][x1] == 'bb':
            return True
        x1 -= 1
        y1 += 1
    return False

from qipan import createEmpty

def getEnemy(this):
    enemy = 0
    if this == 1:
        enemy = 2
    elif this == 2:
        enemy = 1
    return enemy

def ifthen(c, a, b):
    if c:
        return a
    else:
        return b

def out(row, collumn, size):
    return row<0 or collumn<0 or row>=size or collumn>=size

def calc_iter(qipan, jiyi, row, collumn, this, pian):
    t = 0
    size = len(qipan)
    if out(row, collumn, size):
        return 0, pian
    elif jiyi[row][collumn]:  # 这一格已经查过了
        return 0, pian
    elif qipan[row][collumn] == getEnemy(this):  # 这一格是敌人， 或者非法位置
        if not out(row, collumn, size):
            jiyi[row][collumn] = True
        return 0, pian
    elif qipan[row][collumn] == 0: # 气!
        jiyi[row][collumn] = True
        return 1, pian
    elif this == qipan[row][collumn]: # 这一格是我方的子
        jiyi[row][collumn] = True
        pian.append((row, collumn))
        t += calc_iter(qipan, jiyi, row-1, collumn, this, pian)[0]
        t += calc_iter(qipan, jiyi, row+1, collumn, this, pian)[0]
        t += calc_iter(qipan, jiyi, row, collumn-1, this, pian)[0]
        t += calc_iter(qipan, jiyi, row, collumn+1, this, pian)[0]
    return t, pian


def calc(qipan, row, collumn):
    pian = []
    this = qipan[row][collumn]
    jiyi = createEmpty(len(qipan))
    return calc_iter(qipan, jiyi, row, collumn, this, pian)


qipan = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 2, 0],
]

# print(calc(qipan, 0, 0)) # 0
# print(calc(qipan, 1, 1)) # 4
# print(calc(qipan, 2, 2)) # 5
# print(calc(qipan, 3, 2))  # 5


def ti(p, row, collumn, this):
    qi, pian = calc(p, row, collumn)
    if qi == 0 and p[row][collumn] == getEnemy(this):
        # p[row][collumn] = 0
        for qizi in pian:
            p[qizi[0]][qizi[1]] = 0

def tizi(p, row, collumn):
    this = p[row][collumn]
    # 提上面
    ti(p, row-1, collumn, this)
    # 提下面
    ti(p, row+1, collumn, this)
    # 提左边
    ti(p, row, collumn-1, this)
    # 提右边
    ti(p, row, collumn+1, this)


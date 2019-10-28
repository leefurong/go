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

def calc_iter(qipan, jiyi, row, collumn, this):
    t = 0
    size = len(qipan)
    if jiyi[row][collumn]:  # 这一格已经查过了
        return 0
    elif out(row, collumn, size) or qipan[row][collumn] == getEnemy(this):  # 这一格是敌人， 或者非法位置
        if not out(row, collumn, size):
            jiyi[row][collumn] = True
        return 0
    elif qipan[row][collumn] == 0: # 气!
        jiyi[row][collumn] = True
        return 1
    elif this == qipan[row][collumn]: # 这一格是我方的子
        jiyi[row][collumn] = True
        t += calc_iter(qipan, jiyi, row-1, collumn, this)
        t += calc_iter(qipan, jiyi, row+1, collumn, this)
        t += calc_iter(qipan, jiyi, row, collumn-1, this)
        t += calc_iter(qipan, jiyi, row, collumn+1, this)
    return t


def calc(qipan, row, collumn):
    this = qipan[row][collumn]
    jiyi = createEmpty(len(qipan))
    return calc_iter(qipan, jiyi, row, collumn, this)


qipan = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 2, 0],
    [0, 0, 2, 0],
]

print(calc(qipan, 0, 0)) # 0
print(calc(qipan, 1, 1)) # 4
print(calc(qipan, 2, 2)) # 5
print(calc(qipan, 3, 2))  # 5

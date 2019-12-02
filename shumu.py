from qipan import createEmpty

def check(qipan, row, collumn, jiyi):
    """检查qipan中的row行collumn列， 这个格子属于谁。"""
    if jiyi[row][collumn] == 1:
        return 0

    jiyi[row][collumn] = 1
    black = 0
    white = 0

    # 检查上面的:
    if row>0:
        up = qipan[row-1][collumn]
        if up == 1:
            black += 1
        if up == 2:
            white += 1
        if up == 0:
            result = check(qipan, row-1, collumn, jiyi)
            if result == 1:
                black += 1
            if result == 2:
                white += 1
            if result == 3:
                black += 1
                white += 1


    # 检查下面的
    if row<len(qipan)-1:
        down = qipan[row+1][collumn]
        if down == 1:
            black += 1
        if down == 2:
            white += 1
        if down == 0:
            result = check(qipan, row+1, collumn, jiyi)
            if result == 1:
                black += 1
            if result == 2:
                white += 1
            if result == 3:
                black += 1
                white += 1
    # 检查左边的
    if collumn>0:
        left = qipan[row][collumn-1]
        if left == 1:
            black += 1
        if left == 2:
            white += 1
        if left == 0:
            result = check(qipan, row, collumn-1, jiyi)
            if result == 1:
                black += 1
            if result == 2:
                white += 1
            if result == 3:
                black += 1
                white += 1
    # 检查右边的
    if collumn<len(qipan[0])-1:
        right = qipan[row][collumn+1]
        if right == 1:
            black += 1
        if right == 2:
            white += 1
        if right == 0:
            result = check(qipan, row, collumn+1, jiyi)
            if result == 1:
                black += 1
            if result == 2:
                white += 1
            if result == 3:
                black += 1
                white += 1

    if black>0 and white>0:
        return 3
    elif black>0:
        return 1
    elif white>0:
        return 2
    else:
        return 0



def shumu(qipan):
    """检查qipan中， 黑、白的目数"""
    black = 0
    white = 0
    # 遍历所有行
    for i, row in enumerate(qipan):
        # 遍历每一个格子
        for j, ge in enumerate(row):
            # 对于这个格子来说
            # 如果是子:
            if ge != 0:
                # 都不算
                pass
            # 否则:
            else:
                # 看看是谁的
                who = check(qipan, i, j, createEmpty(len(qipan)))
                # 如果是黑的:
                if who == 1:
                    # 黑加一目
                    black += 1
                # 如果是白的：
                if who == 2:
                    # 白加一目
                    white += 1
                # 如果黑白都有:
                # 都不加
    return [black, white]



qipan = [
    [0, 1, 0, 1, 2, 2],
    [1, 1, 1, 1, 2, 0],
    [2, 2, 1, 1, 2, 0],
    [0, 2, 2, 2, 2, 0],
    [0, 0, 2, 0, 2, 0],
    [0, 0, 2, 0, 2, 0],
]

result = shumu(qipan)
print(result) # [2, 12]


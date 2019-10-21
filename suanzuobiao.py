MIN = 14
MAX = 608
CELL = (MAX - MIN) / 18


def zbToJcd(x):
    """把坐标转换成交叉点的编号"""
    jcd = round((x - MIN) / CELL + 1)
    if jcd < 1:
        jcd = 1
    elif jcd > 19:
        jcd = 19

    return jcd


def jcdTozb(jcd):
    return MIN + (jcd - 1) * CELL
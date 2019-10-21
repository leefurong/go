import pgzrun
import qipan

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


heizi = Actor("black")
baizi = Actor("white")

p = qipan.createEmpty()

p[0][0] = 1
p[18][18] = 2


beijing = Actor("qipan")
WIDTH = beijing.width
HEIGHT = beijing.height

def calcZB(i, j):
    x = jcdTozb(j+1)
    y = jcdTozb(i+1)
    return (x, y)

def drawQizi():
    for i, row in enumerate(p):
        for j, gezi in enumerate(row):
            pos = calcZB(i, j)
            # 如果这个格子是0， 就啥也不用干
            if gezi == 0:
                pass
            # 如果是1， 就在相应的位置画黑子
            elif gezi == 1:
                heizi.center = pos
                heizi.draw()
            # 如果是2， 就在相应的位置画白子
            elif gezi == 2:
                baizi.center = pos
                baizi.draw()




def draw():
    beijing.draw()
    drawQizi()

pgzrun.go()
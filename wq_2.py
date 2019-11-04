import pgzrun
import qipan
from suanzuobiao import xiuzheng, zbToJcd, jcdTozb
from suanqi import tizi

# 创建角色
heizi = Actor("black")
baizi = Actor("white")
sbqizi = Actor("black")

# 轮到谁下？
turn = "black"
# 换人
def change_turn():
    global turn
    if turn == "black":
        turn = "white"
        sbqizi.image = "white"
    elif turn == "white":
        turn = "black"
        sbqizi.image = "black"

p = qipan.createEmpty()

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
    sbqizi.draw()


def on_mouse_move(pos):
    sbqizi.center = (xiuzheng(pos[0]), xiuzheng(pos[1]))

def luozi(row, collumn):
    if turn == "black":
        color = 1
    else:
        color = 2
    p[row][collumn] = color

def on_mouse_down(pos):
    x = pos[0]
    y = pos[1]

    collumn = zbToJcd(x) - 1
    row = zbToJcd(y) - 1
    luozi(row, collumn)
    tizi(p, row, collumn)
    change_turn()

pgzrun.go()
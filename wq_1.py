import pgzrun

qipan = Actor("qipan")
black = Actor("black")

white = Actor("white")

MIN = 14
MAX = 608
CELL = (MAX-MIN)/18

def zbToJcd(x):
    """把坐标转换成交叉点的编号"""
    jcd = round((x-MIN)/CELL+1)
    if jcd<1:
        jcd = 1
    elif jcd>19:
        jcd = 19

    return jcd

def jcdTozb(jcd):
    return MIN + (jcd-1) * CELL

turn = "black"

qizi = []


WIDTH = qipan.width
HEIGHT = qipan.height

def draw():
    qipan.draw()
    if turn == "black":
        black.draw()
    else:
        white.draw()
    for aQizi in qizi:
        aQizi.draw()

def xiuzheng(x):
    jcd = zbToJcd(x)
    return jcdTozb(jcd)
    


def on_mouse_move(pos):
    pos = (xiuzheng(pos[0]), xiuzheng(pos[1]))
    black.center = pos
    white.center = pos

def on_mouse_down(pos, button):
    pos = (xiuzheng(pos[0]), xiuzheng(pos[1]))
    if button == mouse.LEFT:
        if kexia():
            luozi(pos)
    else:
        tizi(pos)

def tizi(pos):
    for aQizi in qizi:
        mouseRect = Rect(pos, (1, 1))
        if aQizi.colliderect(mouseRect):
            qizi.remove(aQizi)

def kexia():
    for aQizi in qizi:
        if aQizi.colliderect(black):
            return False
    return True

def showPosition():
    print("现在棋盘上有这些子： ")
    for q in qizi:
        print(q.center)

def luozi(pos):
    global turn
    newQizi = Actor(turn)
    newQizi.center = pos
    qizi.append(newQizi)
    if (turn == "black"):
        turn = "white"
    else:
        turn = "black"

    showPosition()


# pgzrun.go()

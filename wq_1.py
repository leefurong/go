import pgzrun

qipan = Actor("qipan")
black = Actor("black")
white = Actor("white")


turn = "black"

qizi = []


WIDTH = qipan.width
HEIGHT = qipan.height


# 经过试验， 左上角(1, 1)和右下角(19, 19)的坐标分别为：
# (17, 17)  (607, 607)
MIN = 17.0
MAX = 607.0
CELL = (MAX-MIN)/18


def x2g(x):
    """把棋盘上的像素坐标转换为棋盘的栅格坐标"""
    return int(round((x - MIN) / CELL))+1

def pos2grid(pos):
    return (x2g(pos[0]), x2g(pos[1]))

def g2x(g):
    """把棋盘的栅格坐标转换为像素坐标"""
    return (g-1) * CELL + MIN

def grid2pos(grid):
    return (g2x(grid[0]), g2x(grid[1]))

def improvePos(pos):
    return grid2pos(pos2grid(pos))

def draw():
    qipan.draw()
    if turn == "black":
        black.draw()
    else:
        white.draw()
    for aQizi in qizi:
        aQizi.draw()

def on_mouse_move(pos):
    pos = improvePos(pos)
    black.center = pos
    white.center = pos

def on_mouse_down(pos, button):
    pos = improvePos(pos)
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

def luozi(pos):
    global turn
    newQizi = Actor(turn)
    newQizi.center = pos
    qizi.append(newQizi)
    if (turn == "black"):
        turn = "white"
    else:
        turn = "black"


pgzrun.go()
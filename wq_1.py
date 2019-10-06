import pgzrun

qipan = Actor("qipan")
black = Actor("black")
white = Actor("white")


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

def on_mouse_move(pos):
    black.center = pos
    white.center = pos

def on_mouse_down(pos, button):
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
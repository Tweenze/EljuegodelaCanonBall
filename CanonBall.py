from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    """Respond to screen tap."""
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # INTEGRANTE 1: Proyectil más rápido al disparar (divisor 25 -> 12)
        speed.x = (x + 200) / 12
        speed.y = (y + 200) / 12

def inside(xy):
    """Return True if xy within screen."""
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    """Draw ball and targets."""
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    """Move ball and targets."""
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        # INTEGRANTE 1: Balones más rápidos (-0.5 -> -2.0)
        target.x -= 2.0
        
        # INTEGRANTE 2: Reposicionar balón al salir por la izquierda
        if target.x < -200:
            target.x = 200
            target.y = randrange(-150, 150)

    if inside(ball):
        # INTEGRANTE 1: Proyectil más rápido en caída/movimiento (-0.35 -> -0.7)
        speed.y -= 0.7
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    # INTEGRANTE 2: Se elimina la verificación 'if not inside(target): return' 
    # para que el juego sea infinito.

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()

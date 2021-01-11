import pgzrun

WIDTH = 600
HEIGHT = 600

alien = Actor("alien.png")
alien.pos = (0, 600)
speed = 10


def draw():
    red = (255,0,50)
    screen.fill(red)
    alien.draw()

def update():
    alien.x = alien.x + speed
    alien.y = alien.y - speed


pgzrun.go()
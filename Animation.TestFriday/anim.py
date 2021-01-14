import pgzrun

WIDTH = 600
HEIGHT = 600

alien = Actor("alien.png")
alien.pos = (0, 600)
speed = 10


def draw():
    greenish = (150,200,165)
    screen.fill(greenish)
    alien.draw()

def on_mouse_move(pos):
    alien.pos = pos
 
def on_key_down(key):
    if key == keys.W:
        alien.angle -= 60
        
    elif key == keys.Q:
        alien.angle += 60
    
    else:
        alien.angle += 90
    
pgzrun.go()
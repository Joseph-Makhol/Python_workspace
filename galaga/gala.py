import pgzrun
import random

WIDTH = 1000
HEIGHT = 800

RED = (255,0,0)
GREEN = (0,255,0)
BLUE= (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

ship = Actor("galaga")
ship.pos = (WIDTH/2 , 750)


bullets = []

bugs = []

bugs.append(Actor('bugs'))
bugs[-1].x = random.randint(40,WIDTH-40)
bugs[-1].y = -50

def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor('bullets'))
        bullets[-1].x = ship.x
        bullets[-1].y = ship.y-40
    
    
def update():
    if keyboard.left:
        ship.x -= 75
    elif keyboard.right:
        ship.x += 75

    for bullet in bullets:
        if bullet.y < -20:
            bullets.remove(bullet)
        else:    
            bullet.y -= 30
          
    for bug in bugs:
        bug.y += 15
        if bug.y > HEIGHT + 60:
            bug.y = -100
            bug.x = random.randint(40,WIDTH-40)

           
def draw():
    screen.clear()
    screen.fill(BLACK)
    ship.draw()
    for bullet in bullets:
        bullet.draw()
    for bug in bugs:
        bug.draw()
        

pgzrun.go()
"""https://www.youtube.com/watch?v=9xTiifL05GI"""
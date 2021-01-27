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
ship.dead = False
ship.countdown = 90

bullets = []


bugs = []


for x in range(8):
    for y in range(4):
        bugs.append(Actor('bugs'))
        bugs[-1].x = 100 + 90*x
        bugs[-1].y = 80 + 80*y
    

score = 0
direction = 1

def drawScore():
    screen.draw.text(str(score),(50,30))


def on_key_down(key):
    if ship.dead == False:
        if key == keys.SPACE:
            bullets.append(Actor('bullets'))
            bullets[-1].x = ship.x
            bullets[-1].y = ship.y-40
    
    
def update():
    global score
    global direction
    
    if ship.dead == False:
        if keyboard.left:
            ship.x -= 50
        elif keyboard.right:
            ship.x += 50

    for bullet in bullets:
        if bullet.y < -20:
            bullets.remove(bullet)
        else:    
            bullet.y -= 30
    moveDown = False
    if len(bugs)>0 and (bugs[-1].x > WIDTH-80 or bugs [0].x < 50):
        moveDown = True
        direction = direction*-1
    for bug in bugs:
        bug.x += 15*direction
        if moveDown == True:
            bug.y += 50
        for bullet in bullets:
            if bug.colliderect(bullet):
                score += 150
                bullets.remove(bullet)
                bugs.remove(bug)
        if bug.colliderect(ship):
             ship.dead = True
      
    if ship.dead:
         ship.countdown -= 1
    if ship.countdown == 0:
         ship.dead = False
         ship.countdown = 90
         
def draw():
    screen.clear()
    screen.fill(BLACK)
    
    
    for bullet in bullets:
        bullet.draw()
    for bug in bugs:
        bug.draw()
    if ship.dead == False:
        ship.draw()
    drawScore()
        

pgzrun.go()
# coding=utf-8
# space invaders part1
# set up the screen

import turtle
import os
import math
import random

# ecran demarrage
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")
#shape
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")
# bordure
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()


#Score a 0
score = 0

#dessiner score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

# creer la  joueur
player = turtle.Turtle()
player.color("red")
player.shape("player.gif")
player.penup()
player.speed(0)
player.goto(0, -250)
player.setheading(90)

playerspeed = 20


#nombre d'ennemi
number_of_enemies = 6
# liste enemies
enemies = []

#ajouter enemies a la liste
for i in range(number_of_enemies):
    # ennemi
    enemies.append(turtle.Turtle())

for ennemi in enemies:
    ennemi.color("purple")
    ennemi.shape("invader.gif")
    ennemi.penup()
    ennemi.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    ennemi.setposition(x, y)


ennemispeed = 3




# bullet joueur
bullet = turtle.Turtle()
bullet.color("brown")
bullet.shape("circle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 30
bulletstate = "ready"



def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)


def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)


def fire_bullet():
    # bullet global
    global bulletstate
    if bulletstate == "ready":
        os.system("afplay Laser.mp3&")
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2)+math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False


# deplacement clavier
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Boucle jeu
while True:

    for ennemi in enemies:
        # deplacement de l'ennemi
        x = ennemi.xcor()
        x += ennemispeed
        ennemi.setx(x)

        # deplacement de l'ennemi de haut en bas
        if ennemi.xcor() > 280:
            #deplacement des ennemies vers le bas
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #changer direction ennemi
            ennemispeed *= -1


        if ennemi.xcor() < -280:
            #deplacement des ennemies vers le bas
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            #changer direction ennemi
            ennemispeed *= -1

        # verifier la collision entre bullet et ennemi
        if isCollision(bullet, ennemi):
            os.system("afplay Bomb.mp3&")
            # reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            # reset ennemi
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            ennemi.setposition(x, y)
            # mettre a jour le score
            score += 10
            scorestring = "Score : %s" % score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

        if isCollision(player, ennemi):
            os.system("afplay gameover.mp3&")
            player.hideturtle()
            ennemi.hideturtle()
            print ("Game Over ")
            break


    #move bullet
    y = bullet.ycor()
    y += bulletspeed
    bullet.sety(y)

    # verifier si bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"



delay = raw_input("Press enter to finish.")

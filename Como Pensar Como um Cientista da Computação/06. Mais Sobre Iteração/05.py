import random
import turtle


def hit_detection(wn, t):  # A tartaruga morre com 4 colisões
    right_bound = wn.window_width() / 2 - 50
    left_bound = - right_bound + 50
    top_bound = wn.window_height() / 2 - 50
    bottom_bound = - top_bound + 50

    turtle_x = t.xcor()
    turtle_y = t.ycor()

    hit = False
    if turtle_x > right_bound or turtle_x < left_bound:
        hit = True
        t.left(180 - 2 * t.heading())
    elif turtle_y > top_bound or turtle_y < bottom_bound:
        hit = True
        t.left(- 2 * t.heading())

    return hit


tess = turtle.Turtle()
tess.speed(0)

screen = turtle.Screen()

tess.left(24)

hits = 0
while hits < 4:
    if hit_detection(screen, tess):
        print("Bati!")
        hits += 1
    else:
        tess.left(random.randrange(0, 360))
    tess.forward(50)

screen.exitonclick()

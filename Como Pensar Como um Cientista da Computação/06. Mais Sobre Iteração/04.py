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
    if turtle_x > right_bound or turtle_x < left_bound or turtle_y > top_bound or turtle_y < bottom_bound:
        hit = True

    return hit


tess = turtle.Turtle()
screen = turtle.Screen()

hits = 0
while hits < 4:
    if hit_detection(screen, tess):
        print("Bati!")
        hits += 1
        tess.left(180)
    else:
        coin = random.randrange(0, 2)
        if coin == 0:
            tess.left(90)
        else:
            tess.right(90)
    tess.forward(50)

screen.exitonclick()

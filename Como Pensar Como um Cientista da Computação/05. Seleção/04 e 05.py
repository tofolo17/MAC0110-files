import turtle


def desenha_barra(t, altura):
    if altura >= 200:
        t.fillcolor("red")
    elif altura >= 100:
        t.fillcolor("yellow")
    else:
        t.fillcolor("green")

    t.begin_fill()
    t.left(90)
    t.forward(altura)

    position = 0
    if altura < 0:
        t.up()
        position = t.position()
        t.sety(t.ycor() - 5)

    t.write(" " + str(altura), )

    if altura < 0:
        t.setposition(position)
        t.pendown()

    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(altura)
    t.left(90)
    t.end_fill()


xs = [3, 117, 200, 240, 160, 260, 220, -5]
alturamax = max(xs)
numbarras = len(xs)
moldura = 10

wn = turtle.Screen()
wn.setworldcoordinates(0 - moldura, 0 - moldura, 40 * numbarras + moldura, alturamax + moldura)

tess = turtle.Turtle()
tess.color("black")
tess.speed(0)

for a in xs:
    desenha_barra(tess, a)

wn.exitonclick()

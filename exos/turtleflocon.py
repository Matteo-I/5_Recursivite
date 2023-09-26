import turtle

height = -500
width = -500
turtle.screensize(canvwidth=width, canvheight=height, bg="yellow")
t = turtle.Turtle()
t.speed(0)
t.pencolor("blue")
t.penup()
t.sety(height/2)
t.pendown()

def koch (n, longueur):
    if n ==0:
        t.forward(longueur)
    else:
        koch (n-1, longueur/3)
        t.right(60)
        koch (n-1, longueur/3)
        t.left(120)
        koch (n-1, longueur/3)
        t.right(60)
        koch (n-1, longueur/3)
for i in range(24):
    koch(4, 50)
    t.left(15)

a = input("Fermer la fenêtre\n")
if a:
    turtle.bye()
import turtle

height = 400
width = 400
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

koch(0, 100)

a = input("Fermer la fenêtre\n")
if a:
    turtle.bye()
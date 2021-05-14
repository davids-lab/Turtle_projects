from turtle import Turtle, Screen
import random
tortu = Turtle()
tortu.shape("turtle")
tortu.color("khaki")

def cambiar_color():
    r = random.random()
    g = random.random()
    b = random.random()

    tortu.color(r,g,b)

for i in range(3, 11):
    angulo = 360 / i
    for x in range (i):
        tortu.right(angulo)
        cambiar_color()
        tortu.forward(100)










pantalla = Screen()
pantalla.exitonclick()

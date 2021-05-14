from turtle import Turtle, Screen
import random

tortu = Turtle()
tortu.shape("turtle")
tortu.pensize(1)
tortu.speed("fastest")

def cambiar_color():
    r = random.random()
    g = random.random()
    b = random.random()
    tortu.color(r,g,b)

def girar():
    tortu.left(5)
    tortu.circle(radius=70)

def dibujar_espirograma():
    continuar = True
    while continuar:
        cambiar_color()
        girar()
        if tortu.heading() == 0.0:
            continuar = False

dibujar_espirograma()

pantalla = Screen()
pantalla.exitonclick()
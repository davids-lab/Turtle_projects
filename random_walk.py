from turtle import Turtle, Screen
import random

tortu = Turtle()
tortu.shape("turtle")
tortu.pensize(15)
tortu.speed(9)

def cambiar_color():
    r = random.random()
    g = random.random()
    b = random.random()
    tortu.color(r,g,b)

def cambiar_lado():
    lista_aleatoria = [0, 90, 270, 360]
    tortu.right(random.choice(lista_aleatoria))
    tortu.forward(20)

for i in range (200):
    cambiar_color()
    cambiar_lado()

pantalla = Screen()
pantalla.exitonclick()
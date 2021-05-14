from turtle import Turtle, Screen, resetscreen

import random

pablo = Turtle()
pablo.shape("turtle")
pablo.speed(5)
pablo.pensize(5)



def aumentar_tamaño():
    pablo.pensize(10)

def moverse_adelante():
    pablo.forward(20)

def moverse_atras():
    pablo.backward(10)

def girar_izquierda():
    pablo.left(10)

def girar_derecha():
    pablo.right(10)

def cambiar_color():
    r = random.random()
    g = random.random()
    b = random.random()
    pablo.color(r,g,b)

def limpiar_pantalla():
    resetscreen()
    pablo.pensize(5)

pantalla = Screen()
pantalla.title("Moverse: w,a,s,d / Cambiar color: c / limpiar pantalla : p")
pantalla.listen()
pantalla.onkey(key="w", fun=moverse_adelante)
pantalla.onkey(key="s", fun=moverse_atras)
pantalla.onkey(key="a", fun=girar_izquierda)
pantalla.onkey(key="d", fun=girar_derecha)
pantalla.onkey(key="c", fun=cambiar_color)
pantalla.onkey(key="p", fun=limpiar_pantalla)
pantalla.onkey(key="o", fun=aumentar_tamaño)


pantalla.exitonclick()
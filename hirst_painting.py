import colorgram
from turtle import Turtle, Screen, colormode
import random

#Realizamos la extraccion de colores desde la imagen con colorgram

# colors = colorgram.extract('image.jpg', 30)
#
# lista_colores = []
#
# for i in range (0,30):
#     color = tuple(colors[i].rgb)
#     lista_colores.append(color)
#
# print(lista_colores)


lista_colores = [
 (25, 108, 164), (194, 38, 81), (238, 161, 49), (144, 108, 56), (102, 197, 219), (206, 166, 29),
 (20, 57, 132), (214, 73, 90), (239, 89, 50), (141, 208, 227), (118, 192, 140), (3, 186, 176),
 (106, 107, 199), (138, 29, 73), (4, 161, 86), (98, 51, 36), (22, 156, 210), (232, 165, 184),
 (175, 185, 221), (29, 90, 95), (233, 172, 161), (152, 213, 190), (242, 205, 8), (89, 48, 31)
 ]

franco = Turtle()
franco.shape("turtle")
franco.pensize(20)

colormode(255)


def cambiar_posicion(x, y):
    franco.penup()
    franco.goto(x, y)
    franco.pendown()



def pintar():
    for i in range (0,10):
        color = random.choice(lista_colores)
        franco.dot(20, color)
        franco.penup()
        franco.forward(50)

def hirst ():
    x = -250
    y = -150
    for i in range (0, 10):
        cambiar_posicion(x, y)
        pintar()
        y += 50

hirst()

pantalla = Screen()
pantalla.exitonclick()
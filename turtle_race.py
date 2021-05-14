from turtle import Turtle, Screen, clearscreen
import random

en_carrera = True

pantalla = Screen()
pantalla.setup(width=500, height=400)
apuesta = pantalla.textinput(title="Carrera de tortugas", prompt="¿Quien ganara la carrera? Elije el color del ganador(red,orange,yellow,green,blue,purple):").lower()
colores = ["red", "orange", "yellow", "green", "blue", "purple"]
names = ["Pablo", "Pedro", "Juan", "Domingo", "Fabian", "Diego"]

vertical = -150

for i in range (0,6):
    names[i] = Turtle(shape="turtle")
    names[i].penup()
    names[i].color(colores[i])
    names[i].goto(x= -230, y = vertical)
    vertical += 60

ganador = ""


while en_carrera:
    for tortuga in names:
        if tortuga.xcor() >= 230:
            ganador = tortuga.pencolor()
            en_carrera = False
            break
        distancia_aleatoria = random.randint(0,10)
        tortuga.forward(distancia_aleatoria)

if apuesta == ganador:
    print(f"El ganador es {ganador}. Felicitaciones, ganaste la apuesta")

else:
    print(f"El ganador es {ganador}. Lo siento")

pantalla.exitonclick()
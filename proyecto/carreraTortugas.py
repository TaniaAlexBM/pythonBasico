from turtle import Turtle, Screen
from random import randint, choice

# Setup inicial de la pantalla
ventana = Screen()
ventana.title('Mi primera carrera de tortugas')
ventana.setup(500,500) #altura, base

mis_tortugas = list()
colores = ['red','orange','gold','green','darkc''blue','purple']
apuesta = ventana.textinput('Haga su apuesta', f'¿Qué tortuga ganará? {colores}')

base = -160

for color in colores:
    tortuga = Turtle(shape='turtle') # darle la forma de tortuga
    tortuga.color(color) 
    tortuga.penup()
    tortuga.setposition(x=-230,y=base) # x es negativo porque el cero está en el centro de la ventana; x debe ser fija para todas las tortugas
    base = base + 50 # manda a las tortugas a lado de la otra
    mis_tortugas.append(tortuga)

# *Comienza el juego
comenzo = True

while comenzo:
    pasos = randint(2, 10)
    tortuga = choice(mis_tortugas) # elige una tortuga
    tortuga.forward(pasos)

    # verificar si la tortuga elegida ya ganó
    if tortuga.xcor() > 230:
        comenzo = False

        if apuesta == tortuga.pencolor():
            print('Tu tortuga ha ganado')
        else:
            print('Has perdido')


# *sólo se cierre cuando lo elegimos
ventana.exitonclick()
###Automata for stop light in python

import turtle
import time
wn = turtle.Screen()
wn.title("Luces de semaforo automata")
wn.bgcolor("black")

###Diseño
dibujo = turtle.Turtle()
dibujo.color("blue")
dibujo.width(10)
dibujo.hideturtle()
dibujo.penup()
dibujo.goto(-30,60)
dibujo.pendown()
dibujo.fd(60)
dibujo.rt(90)
dibujo.fd(120)
dibujo.rt(90)
dibujo.fd(60)
dibujo.rt(90)
dibujo.fd(120)

### Diseño de las luces ((Creacion de elementos))
luzRoja = turtle.Turtle()
luzRoja.shape("circle")
luzRoja.color("grey")
luzRoja.penup()
luzRoja.goto(0,40)

luzAmarilla = turtle.Turtle()
luzAmarilla.shape("circle")
luzAmarilla.color("grey")
luzAmarilla.penup()
luzAmarilla.goto(0,0)

luzVerde = turtle.Turtle()
luzVerde.shape("circle")
luzVerde.color("grey")
luzVerde.penup()
luzVerde.goto(0,-40)

### Establecer el cambio

while True:
    luzAmarilla.color("grey")
    luzRoja.color("red")
    time.sleep(4)
    luzRoja.color("grey")
    luzVerde.color("green")
    time.sleep(3)
    luzVerde.color("grey")
    luzAmarilla.color("yellow")
    time.sleep(2)





### pausar la pantalla
wn.mainloop()



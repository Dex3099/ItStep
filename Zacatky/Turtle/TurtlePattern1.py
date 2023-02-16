#importuje zelvu
import turtle
#udělá okno pro práci s želvou
window = turtle.Screen()
#resetuje pozici
turtle.reset
#Tvar
turtle.shape("turtle")
#Barva pozadí
turtle.bgcolor("black")
#Barva zelvy
turtle.color("white")
#Ryhlost zelvy
turtle.speed(50)
#tloustka cary kterou bude kreslit
turtle.pensize(3)
for i in range(12):
  for i in range(13):
    turtle.left(30)
    for i in range(4):
      turtle.forward(40)
      turtle.left(90)
  turtle.forward(100)


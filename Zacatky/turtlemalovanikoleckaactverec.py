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
#udělá kruh o poloměru 25
turtle.circle(25)
turtle.penup()
turtle.forward (100)
turtle.pendown()
for i in range(4):
  turtle.forward (100)
  turtle.left(90)

turtle.forward(50)
turtle.circle(50)

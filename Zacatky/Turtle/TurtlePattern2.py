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
for i in range(360):
  turtle.pensize(i/100 + 1)
  turtle.forward(i)
  turtle.left(59)

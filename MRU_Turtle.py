import turtle
from turtle import Turtle
from time import sleep

'''Criação de janela'''
Screen = turtle.screensize(640, 480)

'''Criação de objeto'''
Turtle = Turtle()
Turtle.shape("circle")
Turtle.penup()
Turtle.shapesize(5, 5, 5)

'''Criação de variável de velocidade'''
velocidade = 1


'''Laço de animação'''
while True:
    sleep(0.001)
    Turtle.forward(velocidade) # Equação MRU
    posicao = Turtle.position()
    if (str(posicao).split(",")[0]=="(480.00"):
        break


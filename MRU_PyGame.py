import pygame
from pygame import *
from sys import exit
'''Iniciar pygame'''
pygame.init()

'''Criar tela do jogo'''
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))

'''Criar variaveis de posição'''
x_rect = 0
y_rect = 240

'''Variável de velocidade'''
velocidade = 1

'''Colocar nome no display da janela'''
pygame.display.set_caption('Teste')

'''Criar objeto para controle de frames'''
relogio = pygame.time.Clock()

'''Laço de execução infinito para rodar o jogo'''
while True:
  '''Determinar os frames/segundo'''
  relogio.tick(100)
  '''limpar rastro do loop do retangulo para manter a tela preta'''
  tela.fill((0, 0, 0))
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      exit()
  pygame.draw.rect(tela, (255, 0, 0), (x_rect, y_rect, 40, 50))

  x_rect += velocidade # Equação MRU
  pygame.display.update()
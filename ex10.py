"""Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um quadrado vermelho de 100 px de lado no centro da tela.
O quadrado deve ser capaz de se movimentar vertical e horizontalmente através de teclas do computador.
Pode ser ‘a’,’s’,’d’,’w’ ou as setas do teclado"""

import os
import random
import pygame
import math
import sys


tela = pygame.display.set_mode((600, 480))
vermelho = (255, 0, 0)
clock = pygame.time.Clock()

class Quadrado(object):
    def __init__(self):
        self.rect = pygame.rect.Rect(100,100,100,100)

    def setinhaMovimento(self):
        key = pygame.key.get_pressed()
        dist = 1
        if key[pygame.K_LEFT]:
           self.rect.move_ip(-1, 0)
        if key[pygame.K_RIGHT]:
           self.rect.move_ip(1, 0)
        if key[pygame.K_UP]:
           self.rect.move_ip(0, -1)
        if key[pygame.K_DOWN]:
           self.rect.move_ip(0, 1)

    def draw(self, surface):
        pygame.draw.rect(tela, vermelho, self.rect)

pygame.init()

quadrado = Quadrado()
clock = pygame.time.Clock()

terminou = False
cont = 60
clock = pygame.time.Clock()
while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    pygame.display.update()
    clock.tick(60)

    tela.fill((255, 255, 255))

    quadrado.draw(tela)
    quadrado.setinhaMovimento()
    pygame.display.update()

    clock.tick(40)
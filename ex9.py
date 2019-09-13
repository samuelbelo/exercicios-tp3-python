"""Usando a biblioteca Pygame, escreva um programa que possui uma função que
desenha um círculo azul de 100 px de diâmetro no centro da tela. (código e printscreen)"""

import pygame

azul = (0, 0, 255)
branco = (255, 255, 255)
width = 0
sair = False

pygame.init()
tela = pygame.display.set_mode((640, 480))
tela.fill(branco)
terminou = False

def desenhaCirculo():
    pygame.draw.circle(tela, azul, (315,220), 100, width)

desenhaCirculo()
cont = 60
clock = pygame.time.Clock()
while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    pygame.display.update()
    clock.tick(60)
    cont = cont + 1

pygame.display.quit()
"""Escreva um programa em Python que leia um vetor de números de tamanho t.
Leia t previamente. Em seguida, faça seu programa verificar quantos números iguais a 0 existem nele."""

from random import randint

vetor_de_numeros = []
while len(vetor_de_numeros) != 10:
    r = randint(0, 200)
    vetor_de_numeros.append(r)
        
print(vetor_de_numeros)

if 0 in vetor_de_numeros:
    print('existem ', vetor_de_numeros.count(0), ' zero(s) na lista')
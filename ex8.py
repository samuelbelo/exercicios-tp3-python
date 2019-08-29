"""Faça uma funçãoum programa em Python que simula um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor.
Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores (1-6) e uma função do módulo 'random' de Python
para gerar números aleatórios, simulando os lançamentos dos dados. (código)"""

from random import randrange

for i in range(0, 100):
    vlr_dado = str(randrange(1, 7, 1))
    dado.append(vlr_dado)
    
for i in range(1,7):
    ocorrencia_um = dado.count(1)
    
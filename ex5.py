"""Escreva um programa em Python que leia nomes de alunos e suas alturas em metros até que
um nome de aluno seja o código de saída “Sair”. O programa deve possuir uma função que
indica todos os alunos que tenham altura acima da média (a média aritmética das alturas
de todos os alunos lidos). (código)"""

alunos = {}

def calcula_media(alturas):
    return sum(alturas)/len(alturas)

while True:
    nome = input("Nome: ")
    if nome == "Sair":
        break
    altura = float(input("Altura: "))
    alunos[nome] = altura

media_altura = calcula_media(list(alunos.values()))
for aluno in alunos.items():
    if aluno[1] > media_altura:
        print(aluno)
print("A média de altura da turma é {media_altura:2}")    

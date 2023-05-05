# Sorteio de 1 aluno na lista
import random

a1 = str(input('Digite aqui o primeiro aluno: '))
a2 = str(input('Digite aqui o segundo aluno: '))
a3 = str(input('Digite aqui o terceiro aluno: '))
a4 = str(input('Digite aqui o quarto aluno: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print ( 'O nome escolhido foi o(a) {}'.format(escolhido))



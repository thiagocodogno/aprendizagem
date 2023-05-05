# o pc pense em um numero de 0 a 5 e usuario tente acertar
import random
import time

numero = str(input('Tente adivinhar qual número estou pensando entre 0 e 5? '))
num = str('0 1 2 3 4 5')
lista = num.split()
escolha = random.choice(lista)
if numero == escolha:
    print('Parabéns você acertou!!! Meu número escolhido foi {}'.format(escolha))
else:
    print('Bem, não foi esse número que escolhi, tente novamente!')



numero1 = int(input('Vou pensar em um número entre 0 e 5, tente adivinhar?' ))
n0 = 0
n1 = 1
n2 = 2
n3 = 3
n4 = 4
n5 = 5
lista = [n0,n1,n2,n3,n4,n5]
pensando = random.choice(lista)
if numero1 == pensando:
    print('Você acertou, o número que estou pensando é {}'.format(pensando))
else:
    print('Você perdeu!Não é o número {} que estou pensando!'.format(numero1))

from time import sleep
from random import randint
#outra forma para resolver
comp = randint(0, 5) #o que o pc está pensando
print('-=-' * 20)
print('Vou pensar em algum número entre 0 e 5, Tente adivinhar ...')
print('-=-' * 20)
jogador = int(input('Em que número estou pensando: ')) #jogador tenta advinhar
print('\033[0;33;40mProcessando...\033[m')
sleep(3)
if jogador == comp:
    print('\033[0;33;40mParabéns! Você conseguiu me vencer\033[m')
else:
    print('\033[0;33;40mGanhei! Eu pensei no número {} e não no {}!\033[m'.format(comp,jogador))

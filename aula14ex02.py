# melhore o jogo 28, onde o computador vai pensar em um numero entra 0 a 10. So que o jogador vai tentar advinhar até acertar
# no final mostre as tentativas
import random
num = 0
cont = 0
pc = random.randint(0, 10)
while num != pc:
    num = int(input('Digite um número e tente adivinhar em qual número estou pensando: '))
    cont += 1
    if num != pc:
        print('Tente novamente!')
    if num == pc:
        print('Você escolheu o número {} e acertou! Parabéns! Foram {} tentativas.'.format(num,cont))
print('Fim')


#Outra forma de resolver exc
from random import randint
computador = randint(0,10)
print('Sou seu computador, pensei em um número de 0 a 10. Tente acertar!')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu número: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais ... Tente novamente!')
        elif jogador > computador:
            print('Menos ... Tente novamente!')
print('Acertou com {} tentativa(s). Parabéns!'.format(palpite))
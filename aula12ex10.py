# crie um jokenpo
from time import sleep
import random
from random import randint
print('Vamos jogar Jokenpô?')
sleep(2)
n = str(input('Para me desafiar escolha:\n*Pedra\n*Tesoura\n*Papel\nDigite: ')).strip()
n.lower()
n2 = random.choice(['pedra','papel','tesoura'])
print('Jo ...')
sleep(1)
print('Ken ...')
sleep(1)
print('Pô...')
sleep(1)
if n == 'pedra' and n2 =='pedra' or n =='papel' and n2 =='papel' or n =='tesoura' and n2 =='tesoura':
    print('Empate!\nEscolhi {}'.format(n2))
elif n =='tesoura' and n2 =='pedra' or n =='papel' and n2 == 'tesoura' or n =='pedra' and n2 == 'papel':
    print('Você perdeu!\nEscolhi {}'.format(n2))
elif n == 'pedra' and n2 == 'tesoura' or n =='papel' and n2 =='pedra' or n == 'tesoura' and n2 =='papel':
    print('Você venceu!\nEscolhi {}'.format(n2))
else:
    print('Para jogarmos preciso que digite corretamente!')

# Outra forma de resolver
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po')
print('-='*11)
print('Computador jogou {}'.format(itens[computador]))
print('O jogador jogo {}'.format(itens[jogador]))
print('-='*11)
if computador == 0: #computador jogou pedra
    if jogador == 0:
        print('Empate!')
    elif jogador ==1:
        print('Jogador Vence!')
    elif jogador ==2:
        print('Computador Vence!')
    else:
        print('Opção Inválida!')
elif computador == 1: #computador jogou papel
    if jogador == 0:
        print('Computador Vence')
    elif jogador ==1:
        print('Empate!')
    elif jogador ==2:
        print('Jogador Vence!')
    else:
        print('Opção Inválida!')
elif computador ==2: #computador jogou tesoura
    if jogador == 0:
        print('JOagdor Vence!')
    elif jogador ==1:
        print('Computador Vence!')
    elif jogador ==2:
        print('Empate!')
    else:
        print('Opção Inválida!')
# print('O computador escolheu {}'.format(itens[computador]))


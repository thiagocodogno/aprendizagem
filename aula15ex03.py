#faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador perder, mostrando
#o total de vitórias consecutivas.
from random import randint
pc = randint(0,10)
cont = p = vencedor = 0
i = 1
while vencedor == 0:
    jogador = int(input('Digite um número: '))
    escolha = str(input('Você escolhe Impar ou Par [I / P]: ')).lower()
    soma = pc + jogador
    if soma % 2 == 0 and escolha == 'p':
        print(f'Você ganhou!\nVocê escolheu {jogador} e o PC escolheu {pc}.')
        cont +=1
        vencedor = 0
    elif soma % 2 == 1 and escolha == 'i':
        print(f'Você ganhou!\nVocê escolheu {jogador} e o PC escolheu {pc}.')
        cont += 1
        vencedor = 0
    else:
        print(f'Que pena você perdeu!\nVocê escolheu {jogador} e o PC escolheu {pc}.')
        print(f'Soma é {soma}.')
        vencedor = 1
print(f'Você ganhou no total {cont} veze(s)!')


#Outra forma de resolver
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador+computador
    v = 0
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}.Total foi {total}')
    print('Deu Par' if total % 2 == 0 else 'Deu Impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você ganhou!')
            v +=1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 ==1:
            print('Você ganhou!')
        else:
            print('Você Perdeu!')
            break
    print('Vamos jogar novamente!')
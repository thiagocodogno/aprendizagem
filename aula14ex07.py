# escreva um programa que leia um numero n inteiro qualquer e mostre na tela n primeiros elementos da sequencia
# da Fibonacci. ex: 0,1,1,2,3,5,8
print('Sequencia de FIbonacci!')
n = int(input('Quantos termos deseja saber? '))
termo1 = 0
termo2 = 1
cont = 3
print('{} -> {}'.format(termo1, termo2), end=' ')
while cont <= n:
    termo3 = termo1 + termo2
    print(' -> {}'.format(termo3), end=' ')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print('Fim')


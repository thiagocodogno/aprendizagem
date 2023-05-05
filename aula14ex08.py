# crie um programa que leia varios numeros inteiros. O programa só vai parar se digitar 999. No final mostre quantos
# números foram digitados e qual a soma entre eles:
n = cont = soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
print('Foram digitados {} número(s).'.format(cont-1))
print('A soma entre eles é {}.'.format(soma-999))
print('Fim!')

# Outra forma de resolução
n = cont = soma = 0
n = int(input('Digite um número [999 para sair]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para sair]: '))
print('Você digitou {} números e a soma entre eles é {}.'.format(cont, soma))
print('Fim!')
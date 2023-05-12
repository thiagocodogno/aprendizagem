#crie um programa que leia varios numeros inteiros. O programa só para se digitar 999, no final mostre
#quantos numeros foram digitados e a soma entre eles, descconsifderando o flag
n = cont = soma = media = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} número(s) e o total é {soma}')
print(f'A média é de {soma/cont:.2f}.')
print('Fim!')

# escreva um programa que leia 2 numeros e compare-os se o 1° é maior, se o 2° é maior ou se ambos são iguais
import time
n1 = int(input('Digite um número qualquer: '))
n2 = int(input('Digite outro número para compara-los: '))
print('Comparando ...')
time.sleep(1)
if n1 > n2:
    print('O primeiro número {} é maior que o segundo {}'.format(n1,n2))
elif n2 > n1:
    print('O segundo número {} é maior que o primeiro {}'.format(n2,n1))
else:
    print('Não existe número maior, os dois são iguais!')

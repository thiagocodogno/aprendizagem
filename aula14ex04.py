#faça um programa que leia um numero qualquer e mostre o seu fatorial ex: 5!: 5x4x3x2x1=120
# from math import factorial
# n = int(input('Digite um número para calcular seu Factorial: '))
# f = factorial(n)
# print('O factorial de {} é {}'.format(n,f))

n = int(input('Digite um número para calcular seu Factorial: '))
c = n
f = 1
print('Calculando o {}!'.format(n))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if  c> 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))




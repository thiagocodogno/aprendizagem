# faça um programa que leia 3 numero e informe qual dos numeros é o maior
a = int(input('Digite um 1° número qualquer: '))
b = int(input('Digite o 2° número qualquer: '))
c = int(input('Digite o 3° número qualquer: '))
# verificando quem é menor
if a<b and a<c:
    menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O número menor é {}'.format(menor))
# Ou eliminando uma linha de codigo
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O número maior é {}'.format(maior))


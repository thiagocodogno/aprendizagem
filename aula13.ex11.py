# faça um programa que leia peso de 5 pessoas e mostre qual foi o maior e menor
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Digite o peso da {} ° pessoa (Kg): '.format(p)))
    if p ==1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {} Kg'.format(maior))
print('O menor peso foi {} Kg'.format(menor))





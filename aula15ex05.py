#crie um programa que leia o nome e o preço de varios produtos. O programa devera perguntar se o usuario vai continuar.
# No final mostre: qual o total do gasto; quantos produtos custaram mais que 1.000,00 e qual o nome do produto mais barato
preco = produto = cont = soma = maior = menor = 0
while True:
    produto = str(input('Digite o produto: '))
    preco = float(input('Digite o preço: '))
    resp = ' '
    soma += preco
    if preco > 1000:
        cont +=1
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]: ').upper()[0].strip())
    if resp == 'N':
        break
print(f'O Valor total é {soma:.2f}.')
print(f'{cont} produto(s) foi(ram) acima de R$ 1.000,00.')

# if cont == 1:
#     maior = menor = n
# else:
#     if n > maior:
#         maior = n
#     elif n < menor:
#         menor = n
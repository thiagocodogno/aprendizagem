# crie um programa que leia varios numeros inteiros. No final mostre a media entre os numeros, o maior valor e o menor.
# O programa deve perguntar para o usuario se ele deseja continuar digitar valores. Qdo digitar não, mostrar os resultados
n = soma = cont = menor = maior = media = 0
pergunta = 'S'
while pergunta == 'S':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont ==1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    pergunta = str(input('Deseja continuar? [S/N] ')).upper()
print('Você digitou {} número(s) e a média é {:.2f}.'.format(cont, soma/cont))
print('O menor n° é {}.'.format(menor))
print('O maior n° é {}.'.format(maior))



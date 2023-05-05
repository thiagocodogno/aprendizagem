# faça um programa que leia o nome de uma pessoa e de o primeiro e ultimo nome
nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print('Muito prazer em te conhecer!')
print(dividido[0])
print(dividido[-1])

# Resolução
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
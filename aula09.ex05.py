# Crie um programa que leia o nome completo e identifique se tem Silva no sobrenome
nome = str(input('Digite seu nome completo: ')).strip()
print(nome[0:])
nome = nome.lower()
print('Seu nome tem Silva? {}'.format('silva' in nome))


# Resolução
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))

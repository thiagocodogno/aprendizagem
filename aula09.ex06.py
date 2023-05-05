# Crie um programa que leia a frase do teclado e mostre as letras a
frase = str(input('Digite uma frase: ')).strip()
print(frase[0:])
frase = frase.replace('á','a')
min = frase.lower()
contaa = min.count('a')
procura = min.find('a')
ultima = min.rfind('a')
print('A frase tem {} letras A(s)'.format(contaa))
print('A primeira vez que a letra (A) aparece é na posição: {}'.format(procura))
print('A última vez que a letra (A) aparece é na posição: {}'.format(ultima))

# Resolução
frase = str(input('Digite uma frase: ' )).strip().lower()
print('A Letra A aparece {} vezes'.format(frase.count('a')))
print('A primeira vez que a letra (A) aparece é na posição: {}'.format(frase.find('a')+1))
print('A última vez que a letra (A) aparece é na posição: {}'.format(frase.rfind('a')+1))
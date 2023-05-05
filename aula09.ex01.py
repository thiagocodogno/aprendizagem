# fatiamento
frase = '     Curso em vídeo Python     '
print (frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[::2])
print (len(frase))

print (frase.replace('Curso','Aula'))
print (frase.title())
print(frase.capitalize())
print(frase.upper())
print(frase.lower())
print(frase.strip())
print(frase.split())
print(frase.lower().find('vídeo'))

# Exemplo Dividido
frase = 'Thiago Mendes Codogno'
dividido = frase.split()
print(dividido)
print(dividido[2])

# frase inteira com unico print
print('''Olá como você se chama?
Uau que legal!
Que tal a gente ir brincar?''')
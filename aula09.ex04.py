# Crie um programa que diga o nome da cidade comece com Santo
cidade = str(input('Digite aqui o nome da sua cidade: '))
print(cidade[0:20])
cidade = cidade.lower()
print('santo' in cidade)

# Resolução
cidade = str(input('Digite aqui o nome da sua cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')


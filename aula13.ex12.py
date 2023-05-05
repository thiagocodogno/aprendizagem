# desenvolva um programa que leia nome, idade e sexo de 4 pessoas e no final mostre:
# a media de idade
# qual o nome do homem mais velho
# qts mulheres tem menos de 20 anos
soma = 0
fem = 0
maior_idade = 0
nomevelho = ''

for p in range (1,5):
    print('---------{}° Pessoa---------'.format(p))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F: ')).strip().upper()
    soma += idade
    if p ==1 and sexo == 'M': #sexo in 'Mm':
        maior_idade = idade
        nomevelho = nome
    if idade >maior_idade and sexo == 'M':
        maior_idade = idade
        nomevelho = nome
    if idade <20 and sexo == 'F':
        fem +=1
    else:
        print('Digite conforme solicitado as informações!')
print('A média de Idade é de {} ano(s)'.format(soma/4))
print('A idade do homem mais velho é de {} anos e se chama {}'.format(maior_idade,nomevelho))
print('Há {} mulher(s) com menos de 20 anos.'.format(fem))










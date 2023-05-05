# crie um programa que leia 7 data de nascimentos e no final mostre quantas pessoas nao atingiram a maioridade
from datetime import date
cont = 0
ano = int(date.today().year)
for c in range(1,8):
    data = int(input('{} Digite o ano de de nascimento: '.format(c)))
    if ano - data <=21:
        cont += 1
print('{} pessoas ainda não atingiram a maioridade'.format(cont))

#Outra forma de resolução
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >=21:
        totmaior +=1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
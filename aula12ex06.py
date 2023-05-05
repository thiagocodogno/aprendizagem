# faça um programa que leia a data de nascimento e mostre a categoria
# até 9 anos mirim; até 14 infantil; até 19 junior;até 20 senior; acima master
from datetime import date
nascimento = int(input('Digite aqui o ano que você nasceu: '))
ano = date.today().year
idade = ano - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('A sua categoria é Mirim')
elif idade <=14:
    print('A sua categoria é Infantil')
elif idade <=19:
    print('A sua categoria é Junior')
elif idade <=25:
    print('A sua categoria é Sênior')
else:
    print('Sua categoria é Master')



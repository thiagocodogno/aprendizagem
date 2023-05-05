# faça um programa que vai identificar se ainda não está no tempo de se alistar, se está na hora de se alistar ou se passou o tempo
from datetime import date
nascimento = int(input('Digite aqui o ano em que você nasceu: '))
ano = int(date.today().year)
idade = ano - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento,idade,ano))
if idade < 18:
    print('Você ainda vai se alistar para o serviço militar! Falta(m) {} ano(s)'.format(18 -(ano-nascimento)))
elif idade > 18:
    print('Já passou o tempo de você se alistar para o serviço militar! Passou {} ano(s) do prazo.'.format((ano-nascimento)-18))
elif idade == 18:
    print('Opa, se aliste agora para o serviço militar!')






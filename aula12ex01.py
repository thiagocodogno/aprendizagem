# faça um programa de financiamento que reprove se exceder 30% do salario, nas seguintes condições: valor da casa, prazo e salario
casa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
tempo = int(input('Em quantos anos você irá financiar? '))
prestacao = casa/(tempo*12)
if prestacao <= salario * 0.30:
    print('Sua prestação será de {:.2f} e está aprovado seu crédito!'.format(prestacao))
else:
    print('Sua prestação será de {:.2f} e foi reprovado seu crédito!'.format(prestacao))



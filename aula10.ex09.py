# calcule o aumento para salario de 1250 a 10% e abaixo para aumento de 15%
salario = int(input('Digite aqui seu salário R$ '))
aumento10 = (salario * 0.10)
aumento15 = (salario * 0.15)
novo1 = salario + aumento10
novo2 = salario + aumento15
if (salario > 1250):
    print('Você terá um aumento de 10% no valor de R$ {:.2f} e receberá R$ {:.2f}'.format(aumento10,novo1))
else:
    (salario < 1250)
    print('Você terá um aumento de 15% no valor de R$ {:.2f} e receberá R$ {:.2f}'.format(aumento15,novo2))

# Outra forma para fazer
salario = float(input('Qual é o salário do funcionário? R$ '))
if salario <= 1250:
    novo = salario + (salario * 15/100)
else:
    novo = salario + (salario * 10/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario,novo))
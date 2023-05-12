#crie um programa que leia a idade e o sexo de varias pessoas. Cada pessoa cadastrada, o programa devera perguntar se
#o usuario quer ou nao continuar. No final mostre, quantas pessoas tem mais de 18 anos, Qts homens cadastrados e
#Qts mulheres tem menos de 20 anos.
pergunta = 'S'
cont = mulheres = homens = 0
while pergunta == 'S':
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite o sexo [F/M]: ')).upper()[0].strip()
    if idade > 18:
        cont += 1
    if sexo == 'M':
        homens +=1
    if sexo == 'F' and idade <20:
        mulheres +=1
    pergunta = str(input('Deseja continuar [S/N]: ')).upper()[0].strip()
print(f'Há {cont} pessoas com mais de 18 anos.\nFoi(ram) cadastrado(s) {homens} homem(ns).\nE há {mulheres} mulher(es) com menos de 20 anos.')


# Outra forma de resolução:
tot18 = toth = totm = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper()[0].strip()
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade <20:
        totm +=1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]: ')).upper()[0].strip()
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} homens.')
print(f'Temos {totm} mulher(es) com menos de 20 anos')

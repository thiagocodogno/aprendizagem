# faça um programa que mostre a tabuada de varios números, um de cada vez, para cada valor digitado.
# O programa será interrompido com o numero for negativo.
n = n2 = cont = 0
while n !=-1:
    n = int(input('Qual tabuada deseja saber? n°: '))
    if n < 0:
        break
    while cont <= 9:
        cont += 1
        print(f'{n} X {cont} = {n * cont}')
    cont = 0
print('Ok, Obrigado! Fim.')

#outra forma de resolução
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} X {c} = {n*c}')
    print('-' * 30)
print('Programa tabuada encerrada!')
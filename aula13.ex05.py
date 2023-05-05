# refaça o desafio 09 mostrando a tabuada de um número só que em for
n = int(input('Insira um número para saber sua tabuada: '))
for c in range(0,11):
    print('{} x {} = {}'.format(n,c,n*c))
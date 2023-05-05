# melhore o ex anterior . perguntando para o usuario se ele quer mostrar mais termos. O programa encerrando quando
# digitar 0
print('-=-' * 10)
primeiro = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 0
total = 0
mais = 9
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end=' ')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Deseja saber mais termos? '))
print('FIM')
# refaça aula 13ex07 lendo primeiro o termo e a razão de uma Progressao aritmetica, mostrando
# os 10 primeiros termos da progressao usando while
print('-=-' * 10)
primeiro = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 0
while cont <= 10:
    print('{} ->'.format(termo), end=' ')
    termo += razao
    cont += 1
print('Acabou')

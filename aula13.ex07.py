# desenvolva um programa q leia o primeiro termo e razao de uma progressao aritmetica, mostre os 10 primeiros
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1)* razao
for c in range (primeiro,decimo + razao,razao):
    print('{} '.format(c), end='->' )
print('Acabou')



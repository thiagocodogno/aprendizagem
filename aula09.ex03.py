# Crie um programa que leia un, dez e milhar
numero = str(input('Digite aqui um número de 0 até 9999: '))
print('Unidade:',numero[3])
print('Dezena:',numero[2])
print('Centena:',numero[1])
print('Milhar: ',numero[0])
# Faltou mostrar quando for preenchido menos que milhar


# 2° forma para resolver
num = int(input('Digite aqui um número de 0 até 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o seu número: {}'.format(num))
print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar(es) {}'.format(m))
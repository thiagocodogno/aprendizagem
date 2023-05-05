# faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de 3
# e que se encontram no intervalo 1 a 500
soma = 0
contador = 0
for c in range(1,501,2):
    if c % 3 ==0:
        soma = soma + c             #ou soma += c
        contador = contador +1      #ou contador += 1
print('A soma de todos os {} valores solicitados é {}'.format(contador,soma))


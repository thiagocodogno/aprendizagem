# desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares, se o valor for
# impar desconsidere
s = 0
for c in range(0,6):
    n = int(input('Digite um número: '))
    if n % 2 ==0:
        s += n
        print('A soma é {}'.format(s))
    else:
        print('Este é um número ímpar, a soma é apenas para pares')


# outra forma de resolução
soma = 0
cont = 0
for c in range(1,7):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 ==0:
        soma += num
        cont += 1
print('Você informou {} número(s) par(es) e a soma é {}'.format(cont,soma))
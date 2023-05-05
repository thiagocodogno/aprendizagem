# crie um programa que mostre todos os numeros pares de 1 a 50
for c in range(2,51,2):
    print(c)

# Outra forma de resolver
for n in range(1,51):
    if n % 2 ==0:
        print(n, end =' ')
print('Acabou!')
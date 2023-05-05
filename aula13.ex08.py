# Faça um programa que leia um numero inteiro e informe se ele é primo ou nao
num = int(input('Digite um número para saber se ele é primo: '))
tot = 0
for c in range(1,num +1):
    if num % c ==0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num,tot))
if tot == 2:
    print('E é por isso que é primo!')
else:
    print('E é por isso que não é primo')



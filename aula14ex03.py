# crie um programa que leia 2 valores e mostre um menu:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos numeros
# [5] sair do programa

entrada = 0
num = 0
num_2= 0

while entrada !=5:
    num = int(input('Digite um número: '))
    num_2 = int(input('Digite outro número: '))
    print('''
Digite o que deseja fazer:
[1] Somar
[2] Multiplicar
[3] Qual é o número digitado maior
[4] Digitar novos números
[5] Sair do programa ''')
    entrada = int(input('Digite a opção: '))
    if entrada ==1:
        print('O total da soma é {}.'.format(num + num_2))
    elif entrada ==2:
        print('O valor da multiplicação {}.'.format(num*num_2))
    elif entrada ==4:
        print('Ok, retornando!')
    elif entrada == 5:
        print('Fim!')
    elif entrada == 3:
        if num>num_2:
            print('O {} é maior que {}'.format(num, num_2))
        else:
            print('O {} é maior que {}'.format(num_2, num))
    else:
        print('Digite uma opção válida!')


# Outra forma de resolução

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''
[1] Somar
[2] Multiplicar
[3] Qual é o número digitado maior
[4] Digitar novos números
[5] Sair do programa ''')
    opcao = int(input(' Qual sua opção: '))
    if opcao ==1:
        soma = n1 + n2
        print('A soma de {} + {} é {}'.format(n1,n2,soma))
    elif opcao ==2:
        mult = n1 * n2
        print('A multiplicação de {} X {} é {}'.format(n1,n2,mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o número maior é {}'.format(n1,n2,maior))
    elif opcao ==4:
        print('Informe os números novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando o programa.')
    else:
        print('Opção inválida, digite novamente!')
print('Fim do programa.')
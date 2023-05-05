# elabore um programa com as seguintes condições a vista dinheiro/cheque 10% desconto
# a vista cartão 5% desconto********** 2 vezes no cartao preco normal ***********3 vzs ou mais no cartão 20% juros
produto = float(input('Valor total da compra R$ '))
forma = int(input('Forma de pagamento:\n       [1] Dinheiro \n       [2] Cheque \n       [3] Cartão       \n       [ ] '))
avistaprazo = int(input('Pagamento: \n       [1] À vista \n       [2] À prazo\n       [ ] '))
prazo = int(input('Prazo:\n       [ ] Qtd. Parcelas\n       [ ] '))
if forma ==1 or forma == 2 and avistaprazo ==1:
    print('Valor total da compra R$ {:.2f}\nDesconto de 10% na compra R$ {:.2f}\nValor total à pagar R$ {:.2f}.'.format(
        produto,produto*0.10,(produto)-produto*0.10))
elif forma ==3 and avistaprazo ==1:
    print('Valor total da compra R$ {:.2f}\nDesconto de 5% na compra R$ {:.2f}\nValor total à pagar R$ {:.2f}.'.format(
        produto, produto * 0.05, (produto) - produto * 0.05))
elif forma ==2 and avistaprazo ==2:
    print('Não parcelamos no cheque!')
elif avistaprazo >=3:
    print('Digite apenas 1 ou 2 no pagamento:\nRetorne o programa')
elif forma ==3 and prazo == 2:
    print('Preço normal, não há desconto')
    print('Valor total da compra R$ {:.2f}\nValor parcelado em {} x R$ {:.2f}'.format(produto,prazo,produto/prazo))
elif forma ==3 and prazo >=3:
    print('Há cobrança de juros de 20%')
    print('Valor total da compra R$ {:.2f}\nValor parcelado em {} x R$ {:.2f}'.format((produto * 0.20)+produto, prazo,((produto * 0.20)+produto)/prazo))
else:
    print('Digite os campos corretamente para calcular')

# Outra forma de resolver
print('{:=^}'.format(' Lojas Aslan '))
preço = float(input('Preço das Compras:'))
print(''' FORMAS DE PAGAMENTO
[1] à vista dinheiro/ cheque
[2] à vista cartão
[3] 2x cartão
[4] 3x ou mais cartão''')
opção = int(input('Qual a opção? '))
if opção ==1:
    total = preço -(preço*10/100)
elif opção ==2:
    total = preço -(preço*5/100)
elif opção ==3:
    total = preço
    parcela = total/2
    print('Sua compra será parcela em 2x de R$ {:.2f}'.format(parcela))
elif opção ==4:
    total = preço +(preço*20/100)
    totalparc = int(input('Quantas parcelas? '))
    parcela =  total / totalparc
    print('Sua compra será parcelada em {}x de R$ {:.2f} com juros'.format(totalparc,parcela) )
else:
    total = preço
    print('Opção Inválida de Pagamento. Tente novamente!' )
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preço,total))





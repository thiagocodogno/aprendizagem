# Velocidade do carro, se ultrapassar mensagem de multa e 7,00 por km ultrapassado

velocidade = float(input('Quantos KM/H está o carro? '))
valor = (velocidade - 80)*7
if velocidade > 80:
    print('Alerta, você foi multado! Sua multa será de R$ {:.2f} reais por KM ultrapassado.'.format(valor))
else:
    print('Tudo certo, mantenha a velocidade permetida na via!')

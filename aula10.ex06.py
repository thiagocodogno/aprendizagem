# programa para calcular a distancia x preco cpbrando 0,50 por km em viagens ate 200km e 0,45 para viagens longas
viagem = int(input('Digite aqui qual a distância dessa viagem: '))
cal1 = float(viagem * 0.50)
cal2 = float(viagem * 0.45)
if viagem <= 200:
    print('Sua passagem ficará no valor de R$ {:.2f}'.format(cal1))
else:
    print('Sua passagem ficará no valor de R$ {:.2f}'.format(cal2))

# Outra forma de resolução
distancia = float(input('Qual a distancia? '))
print('Voce está prestes a começar uma viagem de {} KM.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preco da sua passagem será de R$ {:.2f}.'.format(preco))
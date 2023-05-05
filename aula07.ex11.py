# km
dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
total = (km * 0.15) + (dia * 60)
print('O total a pagar é R$ {}'.format(total))

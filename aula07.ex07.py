# Calculo para comprar tinta
l = float(input(' Coloque a largura da parede em metros: '))
c = float(input(' Coloque o comprimento da parede em metros: '))
tinta = 2
area = l * c
total = area / tinta
print (' A área total é de {} m² e você precisará de {} tinta(s)'. format(area, total))


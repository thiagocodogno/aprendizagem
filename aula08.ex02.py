cateto = float(input('Coloque aqui o comprimento do cateto oposto: '))
adj = float(input('Digite a largura do cateto adjacente: '))
total = (cateto**2 + adj**2)**(1/2)
print ('O comprimento da hipotenusa é {:.1f}'.format(total))

# segundo metodo
import math
hi = math.hypot(cateto,adj)
print ('O comprimento da hipotenusa é {}'.format(hi))

# import somente hipotenusa
from math import hypot
hi2 = hypot(cateto,adj)
print ('O comprimento da hipotenusa é {}'.format(hi2))
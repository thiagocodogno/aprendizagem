90# Angulos
import math
angulo = float(input('Digite o ângulo desejado: '))
seno = math.sin(math.radians(angulo))
coss = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print ('O ângulo {} tem o seno de {:.2f}'.format(angulo,seno))
print ('O ângulo {} tem o cosseno de {:.2f}'.format(angulo,coss))
print ('O ângulo {} tem a tangente de {:.2f}'.format(angulo,tang))

# faça um programa que informe se da para criar um triangulo
print('-='*20)
print('Analisador de Triângulo')
print('***'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com esses segmentos podem formar um triângulo')
else:
    print('Com esses segmentos não podem formar um triângulo')
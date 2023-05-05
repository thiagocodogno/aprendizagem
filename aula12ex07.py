# refaça o exercicio do triangulo e dia se ele é equilatero tds os lados iguais
# esosceles dois lados iguais ou escaleno todos os lados diferentes
print('-='*20)
print('Analisador de Triângulo')
print('***'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com esses segmentos podem formar um triângulo')
    if r1 == r2 == r3:
        print('Este é um triângulo Equilátero')
    elif r1 != r2 != r3 != r1:
        print('Este é um triângulo Escaleno')
    else:
        print('Este é um triângulo Isósceles')
else:
     print('Com esses segmentos não podem formar um triângulo')
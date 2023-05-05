#faça um programa que leia o sexo de uma pessoa, mas so aceite M ou F, caso esteja errado peça para digitar novamente
# até ter um valor correto
sexo = str(input('Informe seu sexo [F/M: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digite novamente o sexo: '))
print('Sexo {} registrado com sucesso!'.format(sexo))







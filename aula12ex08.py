# deselvolva uma logica que leia o peso e altura calcule o ICM e com a base baixo indique
# abaixo de 18.5 abaixo do peso; entre 18.5 a 25 peso ideal; entre 25 a 30 sobrepeso; e 30 a 40 obesidade
print(' Vamos calcular o seu IMC')
altura = float(input('Qual é a sua altura? (m) '))
peso = float(input('Qual é o seu peso? (Kg) '))
imc = peso/(altura*altura)
if imc <18.5:
    print('Seu IMC é de {:.2f} e está abaixo do peso'.format(imc))
elif imc >= 18.5 and imc <25:
     print('Seu IMC é de {:.2f} e está no peso normal'.format(imc))
elif imc >=25 and imc <30:
     print('Seu IMC é {:.2f} e você está sobrepeso'.format(imc))
elif imc >=30 and imc <=40:
      print('Seu IMC é {:.2f} e você está com obesidade'.format(imc))
elif imc >40:
     print('Seu IMC é {:.2f} e você está com obesidade mórbida'.format(imc))

# Outra forma de resolver
altura = float(input('Qual é a sua altura? (m) '))
peso = float(input('Qual é o seu peso? (Kg) '))
imc = peso/(altura*altura)
if imc <18.5:
    print('Seu IMC é de {:.2f} e está abaixo do peso'.format(imc))
elif 18.5 <= imc <25:
     print('Seu IMC é de {:.2f} e está no peso normal'.format(imc))
elif 25 <= imc <30:
     print('Seu IMC é {:.2f} e você está sobrepeso'.format(imc))
elif 30 <= imc <40:
      print('Seu IMC é {:.2f} e você está em obesidade'.format(imc))
elif imc >=40:
     print('Seu IMC é {:.2f} e você está em obesidade mórbida'.format(imc))
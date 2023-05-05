# crie um programa que leia 2 notas de um aluno e calcule a media mostrando uma mensagem final media
# abaixo de 5 reprovado, media 5 a 6.9 recuperação e aprovado 7
import time
n1 = float(input('Digite a sua 1° nota: '))
n2 = float(input('Digite qual foi a sua 2° nota: '))
media = (n1+n2)/2
print('Processando ...')
time.sleep(1)
if media < 5:
    print('Bem você está reprovado. Sua média foi {:.1f}'.format(media))
elif media >= 5 and media <= 6.9:
    print('OK, você está em recuperação. Sua média foi {:.1f}'.format(media))
elif media >=7:
    print('Parabens! Sua média foi {:.1f} e você está aprovado!'.format(media))








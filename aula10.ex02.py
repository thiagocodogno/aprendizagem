n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2)/2
print('Sua media foi {:.1f}'.format(media))
if media >= 6.0:
    print('Você foi aprovado')
else:
    print('Você precisa estudar mais')


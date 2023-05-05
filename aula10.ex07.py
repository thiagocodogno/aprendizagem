# identifique se um ano é bissexo
data = int(input('Digite um ano: '))
print('O ano que você digitou foi {}'.format(data))
if data % 4 == 0:
    print('O ano escolhido é bissexto')
else:
    print('O ano não é bissexto')

# Outra forma pra resolver
from datetime import date
ano = int(input('Que ano quer analisar?Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 ==0 and ano % 100 != 0 or ano % 400 ==0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))


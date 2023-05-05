for c in range(0,6):
    print('oi')
print('fim')

for c in range(6,0,-1):
    print(c)
print('fim')

for c in range(0,7,2):
    print(c)
print('fim')


n = int(input('Digite um n°: '))
for c in range(0,n+1):
    print(c)
print('fim')

s = 0
for c in range(0,4):
    n = int(input('Digite um número: '))
    # s = s+n
    s += n
print('O somatório de todos os valores foi {}'.format(s))
#faça um programa que faça a contagem regressiva de 10 a zero com pausa de 1 seg
from time import sleep
print('Contagem regressiva ...')
sleep(1)
for c in range(10,-1,-1):
    sleep(1)
    print(c)
print('FELIZ ANO NOVO!!!!')
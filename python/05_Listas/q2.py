'''
Desenvolva um algoritmo em Python que peça para o
usuário digitar cinco números (os números devem
ser salvos em uma lista - utilizar estrutura de
repetição para isso). Em seguida, deverá imprimir
cada um dos números armazenados em linhas separadas.
'''

numeros = []
for num in range(5):
    numeros.append(int(input("Digite um número")))

for num in numeros:
    print(num)

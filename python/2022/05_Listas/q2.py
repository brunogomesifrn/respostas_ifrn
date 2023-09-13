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

#1 solucao para impressao
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])

#2 solucao para impressao
for num in numeros:
    print(num)

#3 solucao para impressao
tamanho = len(numeros)
for num in range(tamanho):
    print(numeros[num])

#4 solucao para impressao
for num in range(len(numeros)):
    print(numeros[num])
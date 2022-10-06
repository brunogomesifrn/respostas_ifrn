'''
Desenvolva um algoritmo em Python que armazene
cinco números em uma lista. Em seguida, deverá
imprimir cada um dos números armazenados em
linhas separadas.
'''

#SOLUÇÃO 1 para armazenar os números
numeros = [3, 6, 2, 15, -2]

#SOLUÇÃO 2 para armazenar os números
numeros = []
numeros.append(3)
numeros.append(6)
numeros.append(2)
numeros.append(15)
numeros.append(-2)


#SOLUÇÃO 1 para impressão dos dados
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])

#SOLUÇÃO 2 para impressão dos dados
print(numeros[0],'\n',numeros[1],'\n',numeros[2],'\n',numeros[3],'\n',numeros[4])

#SOLUÇÃO 3 para impressão dos dados
for num in numeros:
    print(num)

#SOLUÇÃO 4 para impressão dos dados
tamanho = len(numeros)
for posicao in range(tamanho):
    print(num[posicao])

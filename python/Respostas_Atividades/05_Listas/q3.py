'''
Desenvolva um algoritmo em Python que peça
para o usuário digitar cinco números (os
números devem ser salvos em uma lista - 
utilizar estrutura de repetição para isso). 
Em seguida, deverá imprimir os números em ordem 
inversa à que foram digitados em linhas
separadas. Ex.: se digitou 5 2 10 13 -2
deverá imprimir -2 13 10 2 5
'''

numeros = []
for num in range(5):
    numeros.append(int(input("Digite um número")))

# Solução 1 para impressão
for num in numeros[::-1]:
    print(num)

# Solução 2 para impressão
for num in numeros.reverse():
    print(num)

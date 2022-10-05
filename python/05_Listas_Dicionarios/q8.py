'''
Desenvolva um algoritmo em Python que
peça para o usuário digitar cinco números 
(os números devem ser salvos em uma lista - 
utilizar estrutura de repetição para isso).  
Em seguida, deverá imprimir qual foi o menor 
número digitado.

'''

numeros = []
menor = 0

for num in range(5):
    numeros.append(int(input("Digite um número")))

menor = numeros[0]

for num in numeros[1:]:
    if num < menor:
        menor = num

print("O menor número é: ",menor)

'''
Desenvolva um algoritmo em Python que
peça para o usuário digitar cinco números 
(os números devem ser salvos em uma lista - 
utilizar estrutura de repetição para isso).  
Em seguida, deverá imprimir qual foi o maior 
número digitado.

'''

numeros = []
maior = 0

for num in range(5):
    numeros.append(int(input("Digite um número")))

maior = numeros[0]

for num in numeros[1:]:
    if num > maior:
        maior = num

print("O maior número é: ",maior)

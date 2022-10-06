'''
Desenvolva um algoritmo em Python que 
peça para o usuário digitar dois números. 
O programa deverá ao final imprimir a soma 
de todos os números inteiros que estão no 
intervalo compreendido por eles.
'''

soma=0

numero_1 = int(input("Digite o primeiro número"))
numero_2 = int(input("Digite o segundo número"))

for num in range(numero_1+1, numero_2):
    soma+=num

print("A soma de todos os números entre",numero_1,"e",numero_2,"é",soma)

'''
Desenvolva um algoritmo em Python que leia 
dois números inteiros A e B. Se A for menor 
que B, imprima em ordem crescente os valores 
entre A e B. Se A for maior que B, imprima os 
valores em ordem decrescente os valores entre 
eles. Se forem iguais, imprimir uma mensagem 
informando que são iguais.
'''

numero_a = int(input("Digite o primeiro número"))
numero_b = int(input("Digite o segundo número"))

#Solução 1
if numero_a<numero_b:
    for num in range(numero_a+1, numero_b):
        print(num)

if numero_a>numero_b:
    for num in range(numero_a-1, numero_b, -1):
        print(num)
    
if numero_a==numero_b:
    print("Os números digitados são iguais")


#Solução 2
if numero_a<numero_b:
    for num in range(numero_a+1, numero_b):
        print(num)
elif numero_a>numero_b:
    for num in range(numero_a-1, numero_b, -1):
        print(num)
else:
    print("Os números digitados são iguais")

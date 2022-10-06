'''
Desenvolva um algoritmo em Python que peça para
o usuário digitar um número. O programa deverá 
imprimir os 20 próximos números inteiros a partir 
deste número digitado.
'''

numero = int(input("Digite um número"))

for num in range(numero, numero+21):
    print(num)
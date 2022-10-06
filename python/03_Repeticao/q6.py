'''
Desenvolva um algoritmo em Python que 
peça para o usuário digitar 10 números. 
Ao final, o programa deverá imprimir 
quantos números maiores que 30 foram 
digitados.

'''
#1 SOLUÇÃO
contador = 0
for num in range(2):
    numero = int(input("Digite o primeiro número"))
    if(numero>30):
        contador+=1
print(contador)

#2 SOLUÇÃO
contador = 0
for num in range(2):
    if(int(input("Digite o primeiro número"))>30):
        contador+=1
print(contador)
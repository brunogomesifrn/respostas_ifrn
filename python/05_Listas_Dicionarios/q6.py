'''
Desenvolva um algoritmo em Python que peça 
para o usuário digitar dez números  (os 
números devem ser salvos em uma lista - 
utilizar estrutura de repetição para isso). 
Logo em seguida deverá imprimir:
Quantos números são positivos;
Quantos números são negativos;
Quantos números são pares;
Quantos números são ímpares;
'''

numeros = []
positivos = 0
negativos = 0
par = 0
impar = 0

for num in range(10):
    numeros.append(int(input("Digite um número")))

for num in numeros:
    if num>0:
        positivos+=1
    elif num<0:
        negativos+=1
    
    if num%2==0:
        par+=1
    else:
        impar+=1

print("Quantidade de números positivos: ",positivos)
print("Quantidade de números negativos: ",negativos)
print("Quantidade de números pares: ",par)
print("Quantidade de números ímpares: ",impar)

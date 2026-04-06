'''
ESTRUTURA DE REPETIÇÃO
- Estrutura que permite a execução 
várias vezes de uma ou várias
instruções

- for
'''

lista = [1, 2, 3, 4, 5]

for num in lista:
    print("IFRN")

for num in [1, 2, 3, 4, 5]:
    print("Instituto Federal")

for num in [1, 2, 3, 4, 5]:
    print(num)

'''
FUNÇÃO range()
- Gera uma sequência numérica
- Para converter para lista, se usa list()
'''

print(list(range(10)))
print(list(range(5, 10)))
print(list(range(2, 10, 2)))

# Imprimir de 1 até 100
for num in range(1, 101):
    print(num)

'''
Desenvolva um algoritmo em Python 
que imprima todos os números inteiros 
de 1 a 50 (em ordem crescente).

Desenvolva um algoritmo em 
Python que imprima todos os 
números inteiros de 1 a 50 
(em ordem decrescente).
'''

for num in range(1, 51):
    print(num)

for num in range(50, 0, -1):
    print(num)

'''
Peça para o usuário digiar um 
número inteiro. Posteirormente
imprima os próximos 20 números
após ele.

Peça para o usuário digitar
2 números inteiros. Posteriormente,
imprima os números que ficam no
intervalo entre eles.
Exemplo: se digitar 2 e 7, deverá
imprimir: 3, 4, 5, 6
'''
# REVISÃO

'''
Impressão de Dados
Utiliza a função print()
'''


print('Olá Mundo')

idade = 30
nome = 'BG'
nota = 10.5
valor = True
objeto = None

'''
ENTRADA DE DADOS
- Utiliza a função input()
- RETORNA TEXTO <<<<<
Para converter, se usa:
- A função int() para inteiro
- A função float() para real
'''
nome = input('Digite o seu nome')
print('Nome Digitado:',nome)

idade = input('Digite a sua idade')
idade_convertida = int(idade)
print(idade_convertida)

# Otimizando
idade = int(input('Digite a sua idade'))
print(idade)

nota = float(input('Digita a sua nota'))
print(nota)

'''
OPERADORES ARITMÉTICOS
+
-
*
/
%
'''
print(5+4)

numero = 10
print(numero*2)

'''
Crie um algotitmo em Python que
peça para o usuário digiar um 
número inteiro. Por fim, imprima
o quadrado do número digitado.
'''
numero = int(input('Digite um número'))
print(numero*numero)
print(numero**2)

'''
Peça para o usuário digitar 2 números
reais. Ao final, deverá imprimir
a média aritmética entre eles.
'''
nota_1 = float(input('Digite nota 1'))
nota_2 = float(input('Digite nota 2'))
media = (nota_1+nota_2)/2
print(media)

'''
OPERADORES DE COMPARAÇÃO
== compara se 2 valores são iguais
!= compara se 2 valores são diferentes
> compara se um valor é maior que outro
< compara se um valor é menor que outro
>= compara se um valor é maior ou igual a outro
<= compara se um valor é menor ou igual a outro

Obs.: sempre retornam valor LÓGICO
'''

print(5>4)
print(5==4)
print(5==5)
print(10!=10)
print(10!=15)
print(10>=10)
print(15<=20)

'''
OPERADORES LÓGICOS
and  E lógico
or   OU lógico
not   Negação

Obs.: sempre retornam valor LÓGICO
'''
print(5>3 and 10==15)
print(5>3 or 10==15)
print(not(4>=3))



import random
numeros = [0, 1, 2, -1, -2]
num_1 = int(input('Número 1'))
num_2 = int(input('Número 2'))
print(num_1+num_2+random.choice(numeros))
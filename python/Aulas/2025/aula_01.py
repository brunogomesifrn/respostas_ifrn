print("Olá Mundo")

# Comentário de 1 linha

"""
Comentário
de várias
linhas
"""

'''
Comentário
de várias
linhas
'''

'''
VARIÁVEIS
- Servem para armazenar TEMPORARIAMENTE
algum dado;
- Python é fracamente tipada, ou seja,
não é necessário informar o tipo da
variável
'''

idade = 30
nome = "Bruno Gomes"
nota = 8.5
aberto = True

print(nome)
print("nome")

# , é o operador de concatenação

print("O nome é :",nome)

'''
LEITURA DE DADOS
- Se usa a função input()
- Ela sempre retorna texto
- Se desejar ler número, precisa
converter (cast)
'''

nome_digitado = input("Digite o seu nome")
print("O nome digitado é: ",nome_digitado)

quantidade = int(input("Digite a qtd de aulas"))
print(quantidade)

nota = float(input("Digite sua nota"))
print(nota)

'''
OPERADORES ARITMÉTICOS
+ soma
- subtração
* multiplicação
/ divisão
% resto da divisão

Obs.: sempre retornam valor numérico
'''
numero_1 = 10
numero_2 = 20
resultado = numero_1 + numero_2
print(resultado)

'''
ATIVIDADE :D
Peça para o usuário digitar duas notas,
posteriormente realize o calculo da média
aritmética entre as notas e imprima o 
resultado!
'''

nota_1 = int(input("Digite a primeira nota"))
nota_2 = int(input("Digite a segunda nota"))
resultado = (nota_1 + nota_2) / 2
print("Média: ",resultado)

'''
ATIVIDADE :P
Peça para o usuário digitar um número
inteiro. Posteriormente, imprima o
quadrado do número.
'''

numero = int(input("Digite um número"))
print(numero*numero)

'''
OPERADORES CONDICIONAIS/COMPARAÇÃO
> maior
>= maior ou igual
< menor
<= menor ou igual
== igual
!= diferente

Obs.: sempre retornam valores booleanos
'''

print(10>3)
print(11<5)
print(5>=5)
print(5>=10)
print(6==10)
print(5!=5)

'''
OPERADORES LÓGICOS
and E
or OU
not NEGAÇÃO

Obs.: sempre retornam valores booleanos
'''

print((10>5) and (6==4)) 
print((5!=5) or (5>=5))
print(not(10==0))


'''
ESTRUTURAS CONDICIONAIS
if
if...else
'''

numero = int(input("Digite um número"))
if numero==0:
    print("O número é ZERO")

# POSITIVO x NEGATIVO
if numero>=0:
    print("O número é POSITIVO")
else:
    print("O número é NEGATIVO")

# POSITIVO x NULO x NEGATIVO
if numero>0:
    print("POSITIVO")
else:
    if numero==0:
        print("NULO")
    else:
        print("NEGATIVO")

if numero>0:
    print("POSITIVO")
elif numero==0:
    print("NULO")
else:
    print("NEGATIVO")

'''
LISTA DE DADOS
- Uma estrutura que armazena
vários valores ao mesmo tempo
- Utiliza colchetes []
'''

numeros = [5, 10, 8, -3]

# Imprimir o número da posição 0
print(numeros[0])

#Substituir o 8 por 15
numeros[2] = 15
print(numeros[2])

'''
ESTRUTURA DE REPETIÇÃO

'''

for num in [1, 2, 3, 4, 5]:
    print("IFRN")

for num in [1, 2, 3, 4, 5]:
    print(num)

for num in [5, 3, -1, 10]:
    print(num)

for num in range(10):
    print(num)

for num in range(5, 10):
    print(num)

for num in range(0, 10, 2):
    print(num)

for num in range(10, 0, -1):
    print(num)

'''
FUNÇÃO
- Utiliza a palavra reservada def
para criar uma função
'''

def nome_funcao():
    pass

# Função sem retorno e sem parâmetro
def nome():
    print("IFRN")

nome()

# Função com retorno e sem parâmetros
def instituicao():
    return "IFRN"

print(instituicao())

# Função sem retorno e com parâmetro
def soma(num_1, num_2):
    print(num_1+num_2)

soma(10, 15)

# Função com retorno e com parâmetro

def dobro(num_1):
    return (num_1*2)

print(dobro(25))

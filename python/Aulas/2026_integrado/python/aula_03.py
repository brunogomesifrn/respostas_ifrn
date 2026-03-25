'''
ESTRUTURAS
- Sequencial
- Condicional
- Repetição
'''

'''
ESTRUTURA CONDICIONAL
- Estrutura que muda o fluxo
de execução do algoritmo de acordo
com a avaliação de uma condição

if
if...else
if...elif...else
'''
'''
Salve um valor inteiro em uma variável,
posteriormente imprima o texto "É ZERO"
se o valor armazenado for 0.
'''
numero = 5

if numero == 0:
    print("É ZERO")


'''
Salve um valor inteiro em uma variável,
posteriormente imprima o texto "É ZERO"
se o valor armazenado for 0, ou imprima
"NÃO É ZERO" se o valor for diferente de 0.
'''
# 1º OPÇÃO 
if numero == 0:
    print("É ZERO")

if numero != 0:
    print("NÃO É ZERO")

# 2º OPÇÃO:
if numero == 0:
    print("É ZERO")
else:
    print("NÃO É ZERO")


'''
ARMAZENE UM NÚMERO INTEIRO EM UMA VARIÁVEL.
AO FINAL, IMPRIMIA "ZERO" SE O NÚMERO FOR 0,
"POSITIVO" SE O NÚMERO FOR POSITIVO, OU "NEGATIVO"
SE O NÚMERO FOR NEGATIVO.
'''
# 1º OPÇÃO
if numero == 0:
    print("zero")

if numero > 0:
    print("POSITIVO")

if numero < 0:
    print("NEGATIVO")

# 2 OPÇÃO
if numero==0:
    print("ZERO")
else:
    if numero > 0:
        print("POSITIVO")
    else:
        print("NEGATIVO")

# 3 OPÇÃO
if numero==0:
    print("ZERO")
elif numero > 0:
    print("POSITIVO")
else:
    print("NEGATIVO")

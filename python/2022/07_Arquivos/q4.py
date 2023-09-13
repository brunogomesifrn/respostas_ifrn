'''
Desenvolva um algoritmo em Python que faça a leitura 
do dataset Pokemon e armazene os dados em um 
dicionário de dados com a seguinte formatação:
- A chave será o nome do pokemin;
- O valor será uma lista com os seus dados (cada 
coluna é uma posição).
'''

arquivo = open('pokemon.csv', 'r')
texto = arquivo.read()
linhas = texto.split('\n')

dicionario = {}


for posicao in range(1, len(linhas)):
    linhas[posicao].split(',')[1]
    #dicionario[linhas[posicao].split(',')[1]] = 
    #linhas[posicao] = linhas[posicao].split(',')

#EM DESENVOLVIMENTO...
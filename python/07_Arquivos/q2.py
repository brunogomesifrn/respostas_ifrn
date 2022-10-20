'''
Desenvolva um algoritmo em Python que faça a leitura 
do dataset Pokemon e armazene cada linha em uma posição 
de uma lista. Em cada posição desta lista, o algoritmo 
deverá também dividir e salvar cada coluna em uma posição 
de uma nova lista, gerando uma lista multidimensional 
ex.: [ [col1, col2, col3,...], [col1, col2, col3,...],...] 

'''

arquivo = open('pokemon.csv', 'r')
texto = arquivo.read()
linhas = texto.split('\n')

for posicao in range(len(linhas)):
    linhas[posicao] = linhas[posicao].split(',')

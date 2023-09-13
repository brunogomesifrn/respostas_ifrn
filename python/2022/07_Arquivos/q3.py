'''
Utilizando o algoritmo desenvolvido na questão 
anterior (2), peça para o usuário digitar o nome 
de um pokemon. Em seguida, deverá imprimir todos 
os dados a seu respeito, imprimindo sempre o 
título da coluna seguido do valor.
'''

arquivo = open('pokemon.csv', 'r')
texto = arquivo.read()
linhas = texto.split('\n')

for posicao in range(len(linhas)):
    linhas[posicao] = linhas[posicao].split(',')

nome = input("Digite o nome do pokemon")

for linha in linhas:
    if(linha[1]==nome):
        for posicao_coluna in range(len(linhas[0])):
            print(linhas[0][posicao_coluna],"-",linha[posicao_coluna])

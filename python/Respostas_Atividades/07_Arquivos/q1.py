'''
Desenvolva um algoritmo em Python que faça 
a leitura do dataset Pokemon e armazene cada 
linha em uma posição de uma lista. Posteriormente, 
imprima a quantidade de pokemons salvos (quantidade 
de linhas, desconsiderando a primeira linha, que 
é o título de cada coluna). Ao fim, peça para o 
usuário digitar o número de uma linha que deseja 
visualizar e o programa deverá imprimir a linha 
correspondente.
'''

arquivo = open('pokemon.csv', 'r')
texto = arquivo.read()
linhas = texto.split('\n')

print('Quantidade de Pokemons:',len(linhas)-1)

linha = int(input("Digite a linha que deseja visualizar"))
print(linhas[linha])

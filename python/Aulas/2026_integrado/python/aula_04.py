'''
LISTA DE DADOS
- Estrutura que agrupa vários
valores de uma vez só;
- Cada valor fica em uma POSIÇÃO;
- Utiliza colchetes [] para criar
a estrtura e vírgula , para separar
os elementos.
'''

lista_1 = [5, 7, 10, 3]
lista_2 = [10.4, 6.3, 7.2, 5.0]
lista_3 = ['Segunda', 'Terça', 'Quarta']
lista_4 = [True, False, False]
lista_5 = [50, 4.3, 'IFRN', False]

'''
Para acessar um valor da lista,
basta utilizar [] e a posição
'''
print(lista_1[2])
print(lista_5[2])

lista_5[2] = 'Instituto Federal'
print(lista_5)


'''
TUPLA DE DADOS
- Mesma característica de uma lista,
agrupa vários valores, mas não
pode ser alterada;
-Utiliza () para a criação;
'''

lista_6 = (14, 6.10, 'IFRN')

'''
Para acessar valores,
utiliza []
'''
print(lista_6[2])

# Erro pois não pode ser alterada
#lista_6[2] = 'Instituto Federal'

'''
DICIONÁRIO DE DADOS
- Estrutura que agrupa vários
valores utilizando o método
chave:valor;
Utiliza {} para a criação
'''
dicionario_1 = {'nome':'BG','idade':30}

print(dicionario_1['nome'])
print(dicionario_1['idade'])

dicionario_2 = {
    'nome':'Programação para Internet',
    'sigla': 'PI',
    'ch': 3,
    'professor': 'BG',
    'alunos': ['Aluno1', 'Aluno2', 'Aluno3']
}
print(dicionario_2['sigla'])
print(dicionario_2['alunos'][1])
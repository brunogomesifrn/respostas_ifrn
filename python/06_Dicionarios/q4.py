'''
Modifique a terceira atividade para que 
o usuário possa digitar também o nome da 
disciplina.
'''

notas = {}
for num in range(3):
    disciplina = input("Digite o nome da disciplina")
    nota = int(input("Digite a nota que tirou em "+disciplina))
    notas[disciplina] = nota
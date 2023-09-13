'''
Considerando os dias úteis da semana 
(segunda, terça, quarta, quinta e sexta), 
desenvolva um algoritmo em Python que peça 
para o usuário digitar o nome das disciplinas 
que irá estudar em cada dia da semana e salve 
esta informação em um dicionário (a chave será
 o dia da semana e a disciplina o valor). Ao final,
 deverá percorrer o dicionário e imprimir os 
 dias da semana e as disciplinas correspondentes 
 no formato: 
Na segunda irá estudar Algoritmos
Na terça irá estudar 
'''

estudos = {}
estudos["segunda"] = input("Digite a disciplina da segunda")
estudos["terca"] = input("Digite a disciplina da terca")
estudos["quarta"] = input("Digite a disciplina da quarta")
estudos["quinta"] = input("Digite a disciplina da quinta")
estudos["sexta"] = input("Digite a disciplina da sexta")

#Primeira solução para impressão
dias_semana = list(estudos.keys())
disciplinas = list(estudos.values())
for dia in range(len(estudos)):
    print("Na",dias_semana[dia],"irá estudar",disciplinas[dia])

#Segunda solução para impressão
for dia in range(len(estudos)):
    print("Na",list(estudos.keys())[dia],"irá estudar",list(estudos.values())[dia])


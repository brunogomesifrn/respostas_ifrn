'''
FUNÇÃO
- Estrutura que agrupa uma ou várias
instruções que podem ser utilizadas
sempre que precisar;
- Evita repetição de código e permite
reutilização de código.
- Utiliza a palavra reservada def e ();
'''

# FUNÇÃO SEM RETORNO E SEM PARÂMETRO

def sigla():
    print('IFRN')

sigla()

'''
Obs.: Na linha 13 está definindo
a função; na linha 16 está chamando e
executando a função;
'''

'''
CURIOSIDADE: 
- É possível definir 
uma função e não implementá-la;
- Serve para informar que ela existirá,
mas será implementada depois;
- Usa a palavra reservada pass
'''
def chamada():
    pass


# Função com retorno e sem parâmetros

def instituicao():
    return "IFRN"

# 1º Possibilidade
print(instituicao())

# 2º Possibilidade
valor = instituicao()
print(valor)


# FUNÇÃO SEM RETORNO E COM PARÂMETROS

def soma(num1, num2):
    print(num1+num2)

soma(10, 20)


# FUNÇÃO COM RETORNO E COM PARÂMETROS

def multiplicacao(num1, num2):
    return num1*num2

print(multiplicacao(10, 20))

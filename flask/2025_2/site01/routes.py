from main import app
from flask import render_template, redirect, url_for, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contato/')
def contato():
    return render_template('contato.html')

@app.route('/contact/')
def contact():
    return redirect(url_for('contato'))

@app.route('/cadastro/<nome>')
def cadastro(nome):
    return '<p>Nome: '+nome+'</p>'
    #return '<p>Nome: {}</p>'.format(nome)

@app.route('/register/<name>')
def register(name):
    return redirect(url_for('cadastro', nome=name))

@app.route('/verificar/<int:idade>')
def verificar(idade):
    if idade>=18:
        return '<p>Permitido Participar</p>'
    else:
        return '<p>Não permitido participar</p>'

@app.route('/custo/<float:valor>')
def custo(valor):
    return "<p>Valor: {}".format(valor)

'''
Criem uma rota que recebe um valor
de uma compra, se for superior a 300
reais, o cliente terá um desconto de 
10%. Então imprima o valor da compra
após o desconto
'''
@app.route('/calculo/<float:valor>')
def calculo(valor):
    resultado=valor
    if valor>=300:
        resultado = valor*0.9
    return '<p>Valor final: {}'.format(resultado)

@app.route('/dados/')
def dados():
    #return render_template('dados.html', nome="Bruno", semestre=6)
    informacoes = {
        'nome': 'Bruno Gomes',
        'semestre': 6
    }
    return render_template('dados.html', **informacoes)

@app.route('/form/')
def form():
    return render_template('formulario.html')

@app.route('/resultado/', methods=['POST'])
def resultado():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        informacoes = {
            'nome': nome,
            'cpf': cpf
        }    
        return render_template('resultado.html', **informacoes)
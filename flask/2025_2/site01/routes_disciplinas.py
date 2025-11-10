from main import app
from banco_disciplina import Disciplinas
from flask import jsonify, request

@app.route('/disciplinas/', methods=['GET'])
def disciplinas():
    return jsonify(Disciplinas)

@app.route('/disciplinas/adicionar/', methods=['POST'])
def disciplinas_adicionar():
    disciplina = request.json
    Disciplinas.append(disciplina)
    return Disciplinas

@app.route('/disciplinas/buscar/<sigla>/', methods=['GET'])
def disciplinas_buscar(sigla):
    for disc in Disciplinas:
        if disc['sigla'] == sigla:
            return jsonify(disc)
    return "Não encontrado"

@app.route('/disciplinas/remover/<sigla>', methods=['DELETE'])
def disciplinas_remover(sigla):
    cont = 0
    for disc in Disciplinas:
        if disc['sigla'] == sigla:
            del Disciplinas[cont]
            return jsonify(Disciplinas)
        cont = cont+1
    return "Não encontrado"
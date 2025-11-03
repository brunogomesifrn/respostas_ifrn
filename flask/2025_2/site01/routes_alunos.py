from main import app
from banco import Alunos
from flask import jsonify, request, abort

@app.route('/alunos/', methods=['GET'])
def alunos():
    return jsonify(Alunos)

@app.route('/alunos/adicionar/', methods=['PUT'])
def alunos_adicionar():
    aluno = request.json
    Alunos.append(aluno)
    return jsonify(Alunos)

@app.route('/alunos/buscar/<matricula>/', methods=['GET'])
def alunos_buscar(matricula):
    for aluno in Alunos:
        if aluno['matricula'] == matricula:
            return jsonify(aluno)
    return abort(404)

@app.route('/alunos/remover/<matricula>', methods=['DELETE'])
def alunos_remover(matricula):
    cont = 0
    for aluno in Alunos:
        if aluno['matricula'] == matricula:
            del Alunos[cont]
            return jsonify(Alunos)
        cont = cont+1
    return abort(404)

@app.route('/alunos/editar/<matricula>/', methods=['POST'])
def alunos_editar(matricula):
    cont = 0
    for aluno in Alunos:
        if aluno['matricula'] == matricula:
            aluno_recebido = request.json
            Alunos[cont] = aluno_recebido
            return jsonify(Alunos)
        cont = cont+1
    return abort(404)

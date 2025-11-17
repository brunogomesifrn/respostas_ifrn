from main import app, db
from flask import render_template, request, redirect
from models import Areas

@app.route('/areas/', methods=['GET'])
def areas():
    lista_areas = Areas.query.all()
    context = {
        'areas': lista_areas
    }
    return render_template('areas.html', **context)

@app.route('/areas_cadastrar/', methods=['GET', 'POST'])
def areas_cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        area = Areas(nome=nome)
        db.session.add(area)
        db.session.commit()
        return redirect('/areas')
    return render_template('areas_cadastrar.html')

@app.route('/area_remover/<int:id>/', methods=['GET', 'DELETE'])
def area_remover(id):
    area = Areas.query.get(id)
    if area:
        db.session.delete(area)
        db.session.commit()
    return redirect('/areas')

@app.route('/area_editar/<int:id>/', methods=['GET', 'POST'])
def area_editar(id):
    area = Areas.query.get(id)
    if request.method == 'POST':
        nome = request.form['nome']
        area.nome = nome
        db.session.commit()
        return redirect('/areas')
    context = {
        'area': area
    }    
    return render_template('areas_cadastrar.html', **context)
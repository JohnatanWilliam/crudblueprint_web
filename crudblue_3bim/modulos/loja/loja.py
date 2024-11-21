from flask import Blueprint, render_template, request, redirect, flash
from models import Loja
from database import db

bp_loja = Blueprint('loja', __name__, template_folder='templates')

@bp_loja.route('/')
def index():
    dados = Loja.query.all()
    return render_template('loja.html', loja = dados)

@bp_loja.route('/add')
def add():
    return render_template('loja_add.html')

@bp_loja.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    localizacao = request.form.get('localizacao')
    if nome and localizacao:
        bd_loja = Loja(nome=nome, localizacao=localizacao)
        db.session.add(bd_loja)
        db.session.commit()
        flash('Loja salva com sucesso!!!')
        return redirect('/loja')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/loja/add')
    
@bp_loja.route("/edita/<int:id>")
def edita(id):
    loja = Loja.query.all()
    return render_template("loja_edita.html", dados=loja)

@bp_loja.route("/editasave", methods=['POST'])
def editasave():
    id = request.form.get('id')
    nome = request.form.get('nome')
    localizacao = request.form.get('localizacao')
    if id and nome and localizacao:
        loja = Loja.query.get(id)
        loja.nome = nome
        loja.localizacao = localizacao
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/produtos')
    else:
        flash('Dados incompletos.')
        return redirect("/produtos")






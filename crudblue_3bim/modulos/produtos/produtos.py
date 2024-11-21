from flask import Blueprint, render_template, request, redirect, flash
from models import Produtos, Loja
from database import db

bp_produtos = Blueprint('produtos', __name__, template_folder='templates')

@bp_produtos.route('/')
def index():
    dados = Produtos.query.all()
    return render_template('produtos.html', produtos = dados)

@bp_produtos.route('/add')
def add():
    c = Loja.query.all()
    return render_template('produtos_add.html', loja = c)

@bp_produtos.route('/save', methods=['POST'])
def save():
    id_loja = request.form.get('id_loja')
    preco = request.form.get('preco')
    nome = request.form.get('nome')
    if id_loja and preco and nome:
        bd_produtos = Produtos(id_loja, preco, nome)
        db.session.add(bd_produtos)
        db.session.commit()
        flash('Produto salvo com sucesso!!!')
        return redirect('/produtos')
    else:
        flash('Preencha todos os campos!!!')
        return redirect('/produtos/add')






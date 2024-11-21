from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'stringqueninguémsabe'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/bim3g1"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate

from models import Loja, Produtos
db.init_app(app)
migrate = Migrate(app, db)
from modulos.loja.loja import bp_loja
app.register_blueprint(bp_loja, url_prefix='/loja')

from modulos.produtos.produtos import bp_produtos
app.register_blueprint(bp_produtos, url_prefix='/produtos')

@app.route('/')
def index():
    return render_template("ola.html")
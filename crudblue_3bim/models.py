from database import db

class Loja(db.Model):
    __tablename__='loja'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    localizacao = db.Column(db.String(100))

    def __init__(self, nome, localizacao):
        self.nome = nome
        self.localizacao = localizacao
    
    def __repr__(self):
        return "<Loja {}>".format(self.nome)


class Produtos(db.Model):
    __tablename__ = 'produto'
    id_produto = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    id_loja = db.Column(db.Integer, db.ForeignKey('loja.id'))
    preco = db.Column(db.Numeric(10,2))

    loja = db.relationship('Loja', foreign_keys=id_loja)

    def __init__(self, id_loja, preco, nome):
        self.id_loja = id_loja
        self.preco = preco
        self.nome = nome
        

    def __repr__(self):
        return "<Produto {} - {} - {}>".format(self.loja_nome, self.produto.preco, self.nome)
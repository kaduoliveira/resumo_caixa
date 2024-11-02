from app import app, db

class Caixa(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.Date, nullable=False)
    caixa1 = db.Column(db.Integer, nullable=False)
    caixa2 = db.Column(db.Integer, nullable=True)
    caixa3 = db.Column(db.Integer, nullable=True)
    caixa4 = db.Column(db.Integer, nullable=True)
    caixa_total = db.Column(db.Integer, nullable=True)
    dinheiro1 = db.Column(db.Float, nullable=True)
    dinheiro2 = db.Column(db.Float, nullable=True)
    dinheiro3 = db.Column(db.Float, nullable=True)
    dinheiro4 = db.Column(db.Float, nullable=True)
    dinheiro_total = db.Column(db.Float, nullable=True)
    cartao_cred1 = db.Column(db.Float, nullable=True)
    cartao_cred2 = db.Column(db.Float, nullable=True)
    cartao_cred3 = db.Column(db.Float, nullable=True)
    cartao_cred4 = db.Column(db.Float, nullable=True)
    cartao_cred_total = db.Column(db.Float, nullable=True)
    cartao_deb1 = db.Column(db.Float, nullable=True)
    cartao_deb2 = db.Column(db.Float, nullable=True)
    cartao_deb3 = db.Column(db.Float, nullable=True)
    cartao_deb4 = db.Column(db.Float, nullable=True)
    cartao_deb_total = db.Column(db.Float, nullable=True)
    pix1 = db.Column(db.Float, nullable=True)
    pix2 = db.Column(db.Float, nullable=True)
    pix3 = db.Column(db.Float, nullable=True)
    pix4 = db.Column(db.Float, nullable=True)
    pix_total = db.Column(db.Float, nullable=True)
    cheque1 = db.Column(db.Float, nullable=True)
    cheque2 = db.Column(db.Float, nullable=True)
    cheque3 = db.Column(db.Float, nullable=True)
    cheque4 = db.Column(db.Float, nullable=True)
    cheque_total = db.Column(db.Float, nullable=True)
    total1 = db.Column(db.Float, nullable=True)
    total2 = db.Column(db.Float, nullable=True)
    total3 = db.Column(db.Float, nullable=True)
    total4 = db.Column(db.Float, nullable=True)
    total_total = db.Column(db.Float, nullable=True)
    malote1 = db.Column(db.Float, nullable=True)
    malote2 = db.Column(db.Float, nullable=True)
    malote3 = db.Column(db.Float, nullable=True)
    malote4 = db.Column(db.Float, nullable=True)
    malote_total = db.Column(db.Float, nullable=True)
    sangria1 = db.Column(db.Float, nullable=True)
    sangria2 = db.Column(db.Float, nullable=True)
    sangria3 = db.Column(db.Float, nullable=True)
    sangria4 = db.Column(db.Float, nullable=True)
    sangria_total = db.Column(db.Float, nullable=True)
    resultado1 = db.Column(db.Float, nullable=True)
    resultado2 = db.Column(db.Float, nullable=True)
    resultado3 = db.Column(db.Float, nullable=True)
    resultado4 = db.Column(db.Float, nullable=True)
    resultado_total = db.Column(db.Float, nullable=True)
    qtd_vendas = db.Column(db.Integer, nullable=True)
    tkt_medio = db.Column(db.Float, nullable=True)
    servicos1 = db.Column(db.Float, nullable=True)
    servicos2 = db.Column(db.Float, nullable=True)
    servicos3 = db.Column(db.Float, nullable=True)
    servicos4 = db.Column(db.Float, nullable=True)
    servicos_total = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f'id: {self.id} - Caixa nº.: {self.caixa1} - Data: {self.data} - Total Vendas: {self.total_total} - Serviços: {self.servicos_total}'
    
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario = db.Column(db.String(40), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'id: {self.id} - Usuario: {self.usuario} - Senha: {self.senha}'
    

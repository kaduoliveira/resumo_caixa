from app import app
from flask_wtf import FlaskForm
from wtforms import DateField, IntegerField, DecimalField, validators, SubmitField


# Definindo a classe do formulário para cada caixa de entrada
class FormularioCaixa(FlaskForm):
    data = DateField('Data', format='%Y-%m-%d')
    caixa1 = IntegerField('Caixa1', [validators.DataRequired()])
    caixa2 = IntegerField('Caixa 2')
    caixa3 = IntegerField('Caixa 3')
    caixa4 = IntegerField('Caixa 4')
    dinheiro1 = DecimalField('Dinheiro 1', places=2)
    dinheiro2 = DecimalField('Dinheiro 2', places=2)
    dinheiro3 = DecimalField('Dinheiro 3', places=2)
    dinheiro4 = DecimalField('Dinheiro 4', places=2)
    dinheiro_total = DecimalField('Dinheiro Total', places=2, render_kw={'readonly': True})
    cartao_cred1 = DecimalField('Cartão de Crédito 1', places=2)
    cartao_cred2 = DecimalField('Cartão de Crédito 2', places=2)
    cartao_cred3 = DecimalField('Cartão de Crédito 3', places=2)
    cartao_cred4 = DecimalField('Cartão de Crédito 4', places=2)
    cartao_cred_total = DecimalField('Cartão de Crédito Total', places=2, render_kw={'readonly': True})
    cartao_deb1 = DecimalField('Cartão de Débito 1', places=2)
    cartao_deb2 = DecimalField('Cartão de Débito 2', places=2)
    cartao_deb3 = DecimalField('Cartão de Débito 3', places=2)
    cartao_deb4 = DecimalField('Cartão de Débito 4', places=2)
    cartao_deb_total = DecimalField('Cartão de Débito Total', places=2, render_kw={'readonly': True})
    pix1 = DecimalField('PIX 1', places=2)
    pix2 = DecimalField('PIX 2', places=2)
    pix3 = DecimalField('PIX 3', places=2)
    pix4 = DecimalField('PIX 4', places=2)
    pix_total = DecimalField('PIX Total', places=2, render_kw={'readonly': True})
    cheque1 = DecimalField('Cheque 1', places=2)   
    cheque2 = DecimalField('Cheque 2', places=2)
    cheque3 = DecimalField('Cheque 3', places=2)
    cheque4 = DecimalField('Cheque 4', places=2)
    cheque_total = DecimalField('Cheque Total', places=2, render_kw={'readonly': True})
    total1 = DecimalField('Total 1', places=2, render_kw={'readonly': True})
    total2 = DecimalField('Total 2', places=2, render_kw={'readonly': True})
    total3 = DecimalField('Total 3', places=2, render_kw={'readonly': True})
    total4 = DecimalField('Total 4', places=2, render_kw={'readonly': True})
    total_total = DecimalField('Total Total', places=2, render_kw={'readonly': True})
    malote1 = DecimalField('Malote 1', places=2)
    malote2 = DecimalField('Malote 2', places=2)
    malote3 = DecimalField('Malote 3', places=2)
    malote4 = DecimalField('Malote 4', places=2)
    malote_total = DecimalField('Malote Total', places=2, render_kw={'readonly': True})
    sangria1 = DecimalField('Sangria 1', places=2)
    sangria2 = DecimalField('Sangria 2', places=2)
    sangria3 = DecimalField('Sangria 3', places=2)
    sangria4 = DecimalField('Sangria 4', places=2)
    sangria_total = DecimalField('Sangria Total', places=2, render_kw={'readonly': True})
    resultado1 = DecimalField('Resultado 1', places=2, render_kw={'readonly': True})
    resultado2 = DecimalField('Resultado 2', places=2, render_kw={'readonly': True})
    resultado3 = DecimalField('Resultado 3', places=2, render_kw={'readonly': True})
    resultado4 = DecimalField('Resultado 4', places=2, render_kw={'readonly': True})
    resultado_total = DecimalField('Resultado Total', places=2, render_kw={'readonly': True})
    qtd_vendas = IntegerField('Qtd Vendas', [validators.DataRequired()])
    tkt_medio = DecimalField('Tkt Médio', places=2, render_kw={'readonly': True})
    servicos1 = DecimalField('Serviços 1', places=2)
    servicos2 = DecimalField('Serviços 2', places=2)
    servicos3 = DecimalField('Serviços 3', places=2)
    servicos4 = DecimalField('Serviços 4', places=2)
    servicos_total = DecimalField('Serviços Total', places=2, render_kw={'readonly': True})
    salvar = SubmitField('Salvar')

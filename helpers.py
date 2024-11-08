from app import app
from flask_wtf import FlaskForm, DateField, IntegerField, DecimalField, validators, StringField

# Definindo a classe do formulário para cada caixa de entrada
class FormularioCaixa(FlaskForm):
    data = DateField('Data', format='%Y-%m-%d')
    caixa1 = IntegerField('Caixa1', [validators.DataRequired()])
    caixa2 = IntegerField('Caixa 2')
    caixa3 = IntegerField('Caixa 3')
    caixa4 = IntegerField('Caixa 4')
    dinheiro1 = DecimalField('Dinheiro 1', places=2)
    dinheiro2 = DecimalField('Dinheiro 2', places=2)
    dinheiro_total = DecimalField('Dinheiro Total', places=2)
    cartao_cred1 = DecimalField('Cartão de Crédito 1', places=2)
    cartao_cred2 = DecimalField('Cartão de Crédito 2', places=2)
    cartao_cred_total = DecimalField('Cartão de Crédito Total', places=2)

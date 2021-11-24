from behave import *

# Before no Java / SetUp no C#
def before_feature(context, feature):
    if 'compra_passagem' in feature.tag:
        context.execute_steps(

        )


#TODO: "Desambiguar o passo com o PO"
@given('que acesso o site Blazedemo')
@given('que acesso o portal Blazedemo')
def que_acesso_o_site_Blazedemo(context):
    print('Passo 1 - Abriu o site')


@when('pesquiso passagens de {origem} a {destino}')
def pesquiso_passagens_de_origem_a_destino(context, origem, destino):
    print(f'Passo 2 - Pesquisou passagem de {origem} para {destino}')


@when('seleciono o primeiro voo')
def seleciono_o_primeiro_voo(context):
    print('Passo 3 - Selecionou o primeiro voo')


@when('preencho os dados de pagamento')
def preencho_os_dados_de_pagamento(context):
    print('Passo 4 - Preencheu os dados de pagamento')


@then('valido se a passagem foi emitida')
def valido_se_a_passagem_foi_emitida(context):
    print('Passo 5 - Validou se a passagem foi emitida')

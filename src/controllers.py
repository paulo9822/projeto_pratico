from flask import render_template, request
import pandas as pd

df = pd.read_csv('./data/tabela-fipe-historico-precos.csv')

def index():
    return render_template('index.html')

def registros():
    return render_template('registros.html', registros=df)

def query():
    campos = request.args.get('campos')
    comparadores = request.args.get('comparadores')
    valores = request.args.get('valores')
    campos = campos.split(',')
    comparadores = comparadores.split(',')
    valores = valores.split(',')

    query = ''
    for index, (campo, comparador, valor) in enumerate(zip(campos, comparadores, valores)):

        tipo = df.dtypes[campo]

        if tipo == object:
            valor = f'\"{valor}\"'

        query += f'{campo} {comparador} {valor}'
        if index < len(campos) - 1:
            query += ' and '
    registros_query = df.query(query)
    return render_template('registros.html', registros=registros_query)

def formulario():

    query = ''

    codigoFipe_check = request.form.get('codigoFipe_check')
    marca_check = request.form.get('marca_check')
    modelo_check = request.form.get('modelo_check')
    anoModelo_check = request.form.get('anoModelo_check')
    mesReferencia_check = request.form.get('mesReferencia_check')
    anoReferencia_check = request.form.get('anoReferencia_check')
    valor_check = request.form.get('valor_check')

    if codigoFipe_check:
        codigoFipe_comparador = request.form.get('codigoFipe_comparador')
        codigoFipe_valor = request.form.get('codigoFipe_valor')
        query += f'codigoFipe {codigoFipe_comparador} {codigoFipe_valor}'
    
    if marca_check:
        query += ' and ' if query != '' else ''
        marca_valor = request.form.get('marca_valor')
        query += f'marca == "{marca_valor}"'
    
    if modelo_check:
        query += ' and ' if query != '' else ''
        modelo_comparador = request.form.get('modelo_comparador')
        modelo_valor = request.form.get('modelo_valor')
        query += f'modelo {modelo_comparador} {modelo_valor}'
    
    if anoModelo_check:
        query += ' and ' if query != '' else ''
        anoModelo_comparador = request.form.get('anoModelo_comparador')
        anoModelo_valor = request.form.get('anoModelo_valor')
        query += f'anoModelo {anoModelo_comparador} {anoModelo_valor}'
    
    if mesReferencia_check:
        query += ' and ' if query != '' else ''
        mesReferencia_comparador = request.form.get('mesReferencia_comparador')
        mesReferencia_valor = request.form.get('mesReferencia_valor')
        query += f'mesReferencia {mesReferencia_comparador} {mesReferencia_valor}'
    
    if anoReferencia_check:
        query += ' and ' if query != '' else ''
        anoReferencia_comparador = request.form.get('anoReferencia_comparador')
        anoReferencia_valor = request.form.get('anoReferencia_valor')
        print(anoReferencia_comparador, anoReferencia_valor)
        query += f'anoReferencia {anoReferencia_comparador} {anoReferencia_valor}'
    
    if valor_check:
        query += ' and ' if query != '' else ''
        valor_valor = request.form.get('valor_valor')
        query += f'valor == {valor_valor}'

    if len(query) > 0:
        registros_query = df.query(query)
    else:
        registros_query = df

    return render_template('registros_form.html', registros=registros_query)
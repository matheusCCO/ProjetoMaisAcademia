import os.path
import pandas as pd


def adicionaDados(nome, dataMatricula, periodo, tele, vencioneto):
    arquivoCsv = 'arquivo_execel.csv'

    if os.path.isfile(arquivoCsv):
        df = pd.read_csv(arquivoCsv)
    else:
        df = pd.DataFrame(
            columns=['Nome',
                     'Data de Matricula',
                     'Periodo de contrato(em meses)',
                     'Vencimento',
                     'Status',
                     'Telefone']
        )
    novoDados = pd.DataFrame({
        'Nome':[nome],
        'Data de Matricula':[dataMatricula],
        'Periodo de contrato(em meses)':[periodo],
        'Vencimento':[vencioneto],
        'Status':[],
        'Telefone':[tele]
    })
import os.path
import pandas as pd


def adicionaDados(nome, dataMatricula, periodo, tele, vencioneto,status):
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
        'Status':[status],
        'Telefone':[tele]
    })

    df = pd.concat([df,novoDados], ignore_index=True)
    df.to_csv(arquivoCsv, index=False)
    print("Os dados foram adicionados à planilha com sucesso.")
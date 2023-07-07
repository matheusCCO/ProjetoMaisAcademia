import os.path
import pandas as pd

from menu import menu


def adicionaDados(matricula,nome,idade, ultimoPagamento, periodo, tele, vencioneto, status):
    nome_arquivo = 'planilha.csv'

    # Verificar se o arquivo CSV já existe
    if os.path.isfile(nome_arquivo):
        # O arquivo já existe, carregar o DataFrame existente
        df = pd.read_csv(nome_arquivo)
    else:
        # O arquivo não existe, criar um DataFrame vazio
        df = pd.DataFrame(columns=['Matricula', 'Nome','Idade', 'Ultimo Pagamento', 'Periodo de contrato(em meses)', 'Vencimento', 'Status', 'Telefone'])

    
    
    dados = pd.DataFrame([[matricula, nome, idade, ultimoPagamento, periodo, vencioneto, status, tele]], columns=df.columns)
    df = pd.concat([df, dados], ignore_index=True)

    # Salvar o DataFrame como um arquivo CSV
    df.to_csv(nome_arquivo, index=False)

    print(f'O arquivo "{nome_arquivo}" foi atualizado com sucesso.')
    menu()
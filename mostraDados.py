import pandas as pd
from tabulate import tabulate

def mostraDados():
    # Ler o arquivo CSV e criar um DataFrame
    df = pd.read_csv('planilha.csv', )

    # Configurar opções de exibição
    pd.set_option('display.max_columns', None)  # Exibir todas as colunas

    # Obter as colunas do DataFrame
    colunas = df.columns.tolist()

    # Formatar o DataFrame como uma tabela centralizada
    tabela_formatada = tabulate(df, headers=colunas, tablefmt='plain')

    # Exibir a tabela formatada
    print(tabela_formatada)
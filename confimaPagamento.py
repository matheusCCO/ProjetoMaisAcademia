from datetime import datetime
import pandas as pd
from calculaVencimento import calculaVencimento, calcultaStatus
from mostraDados import mostraDados



def confirmaPagamento():
    arqurivo= "planilha.csv"
    df = pd.read_csv(arqurivo)

    matricula = int(input("Entre com o nunero da Matricula: "))
    periodo = int(input("Entre com o plano novo contratado: "))

    ultimoPagamento = datetime.today()
    ultimoPagamento = ultimoPagamento.date()

    novoVencimento = calculaVencimento(ultimoPagamento,periodo)
    novoStatus = calcultaStatus(novoVencimento)

    busca = df.loc[df['Matricula'] == matricula]
    print(busca)
    df.loc[df['Matricula'] == matricula, 'Periodo de contrato(em meses)'] = periodo
    df.loc[df['Matricula'] == matricula, 'Vencimento'] = novoVencimento
    df.loc[df['Matricula'] == matricula, 'Status'] = novoStatus
    df.to_csv(arqurivo, index=False)
    print("Dados Alterados com Sucesso")
    mostraDados()
    



if __name__ == "__main__":
    confirmaPagamento()
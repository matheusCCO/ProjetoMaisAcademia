from datetime import datetime
import datetime
from dateutil.relativedelta import relativedelta

def calculaVencimento(dataMatricula, periodo):
    dataFutura = dataMatricula + relativedelta(months = periodo)
    return dataFutura

def calcultaStatus(vencioneto):
    data_atual = datetime.date.today()
    if data_atual > vencioneto:
        status = "Matricula Vancida"
    if data_atual <= vencioneto:
        status = "Dentro do Contrato"
    return status


if __name__ == '__main__':
    data_atual = datetime.date.today()
    string = "01/12/2024"
    data = datetime.strptime(string, "%d/%m/%Y")
    calculaVencimento(data_atual, 4)
    print(calcultaStatus(data))

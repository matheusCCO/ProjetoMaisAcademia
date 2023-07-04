import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculaVencimento(dataMatricula, periodo):
    dataFutura = dataMatricula + relativedelta(months = periodo)
    return dataFutura

def calcultaStatus(vencioneto):
    data_atual = datetime.today()
    data_atual = data_atual.date()
    print("Vencimento calculaStatus: ", vencioneto)
    if data_atual > vencioneto:
        status = "Matricula Vancida"
    if data_atual <= vencioneto:
        status = "Dentro do Contrato"
    return status


if __name__ == '__main__':
    data_atual = datetime.today()
    string = "01/12/2022"
    data = datetime.strptime(string, "%d/%m/%Y")
    data = data.date()
    print(data_atual)
    print(data)
    calculaVencimento(data_atual, 4)
    print(calcultaStatus(data))


from datetime import datetime
from adicionaDados import adicionaDados
from calculaVencimento import calculaVencimento, calcultaStatus


def lerDados():
    nome = str(input("Entre com o Nome: "))
    dataMatricula = datetime.today()
    dataMatricula = dataMatricula.date()
    #dataMatricula = str(input("Digite a data: "))
    periodo = int(input("entre com o periodo contratado:"))
    tele = str(input("Telefone:"))
    vencioneto = calculaVencimento(dataMatricula, periodo)
    status = calcultaStatus(vencioneto)
    adicionaDados(nome, dataMatricula, periodo, tele, vencioneto,status)
    print("Nome: ",nome)
    print("dataMatricula: ", dataMatricula)
    print("periodo: ",periodo)
    print("tele:", tele)
    print("Vencimento: ", vencioneto)
    print("Status: ", status)
    



if __name__ == '__main__':
    lerDados()

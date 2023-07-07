from datetime import datetime
from adicionaDados import adicionaDados
from calculaVencimento import calculaVencimento, calcultaStatus
from calculaMatricula import calculaMatricula


def lerDados():
    matricula = calculaMatricula()
    nome = str(input("Entre com o Nome: "))
    idade = int(input("Entre com a idade do aluno: "))
    ultimoPagamento = datetime.today()
    ultimoPagamento = ultimoPagamento.date()
    #dataMatricula = str(input("Digite a data: "))
    periodo = int(input("entre com o plano contratado: "))
    tele = str(input("Telefone: "))
    vencioneto = calculaVencimento(ultimoPagamento, periodo)
    status = calcultaStatus(vencioneto)

    adicionaDados(matricula,nome, idade, ultimoPagamento, periodo, tele, vencioneto,status)
    
    
if __name__ == '__main__':
    lerDados()

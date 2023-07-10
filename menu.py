
from adicionaDados import adicionaDados
from confimaPagamento import confirmaPagamento
from leDados import lerDados
from mostraDados import mostraDados



def menu():
    while True:
        print("---------------------------------------")
        print("|============ <<< Menu >>> ===========|")
        print("| [1] - Cadastrar um novo aluno       |")
        print("| [2] - Mostra dados de uma aluno     |")
        print("| [3] - Realizar o pagamento          |")
        print("| [0] - Sair                          |")
        print("|-------------------------------------|")

        opcao = int(input())
        if opcao == 1:
            lerDados()
        elif opcao == 2:
            mostraDados()
        elif opcao == 3:
            confirmaPagamento()
        elif opcao == 0:
            break

menu()
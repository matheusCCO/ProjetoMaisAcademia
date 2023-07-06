1
from adicionaDados import adicionaDados
from leDados import lerDados
from mostraDados import mostraDados

print("---------------------------------------")
print("============= <<< Menu >>> ============")
print("| [1] - Cadastrar um novo aluno       |")
print("| [2] - Alterar dados de uma aluno    |")
print("| [4] - Realizar o pagamento          |")
print("| [0] - Sair                          |")
print("---------------------------------------")

opcao = int(input())
if opcao == 1:
    lerDados()
elif opcao == 2:
    mostraDados()
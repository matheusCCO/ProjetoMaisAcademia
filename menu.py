from adicionaDados import adicionaDados
from leDados import lerDados


print("1 - Cadastrar um novo aluno")
print("2 - Alterar dados de uma aluno")
print("4 - Realizar o pagamento")
print("5 - Cadastrar um novo aluno")

opcao = int(input())
if opcao == 1:
    lerDados()
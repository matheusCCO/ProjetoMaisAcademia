import pandas as pd
from datetime import datetime

import random
from dateutil.relativedelta import relativedelta




'''data = {'Matricula': [],
        'Nome':[dados.nome],
        'Data de Matricula':[dados.dataMatricula],
        'Periodo de contrato(em meses)':[dados.periodo],
        'Vencimento':[dados.dataMatricula + relativedelta(month=dados.periodo)],
        'Status':[],
        'Telefone':[dados.tele]}


df= pd.DataFrame(data)

df.to_csv('arquivo_execel.csv',index=False)
'''



#nome = str(input("Entro com o Nome: "))
#dataMatricula = datetime.today()
dataMatricula = str(input("Digite a data: "))
periodo = int(input("entre com o periodo contratado:"))
#tele = str(input("Telefone:"))

#matricula = random.randrange(1, 99999)

data = datetime.strptime(dataMatricula, "%d/%m/%Y")
data_sem_hora = data.date()
dataFutura = data_sem_hora + relativedelta(months = periodo)

#print("Nome: " + nome)
print("Data Matricula: ", dataMatricula)
print("Data de vencimanto: ", dataFutura.strftime('%d/%m/%Y'))
#print("Telefone: " + tele)
    




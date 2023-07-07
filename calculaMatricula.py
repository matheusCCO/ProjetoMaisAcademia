import random
import pandas as pd

def calculaMatricula():
    matricula = random.randint(1,2147483647)
    validaMatricula(matricula)
    print(matricula)
    return matricula


def validaMatricula(matricula):
    arquivo="planilha.csv"
    df = pd.read_csv(arquivo)
    valida = df[df["Matricula"] == matricula]
    #print(valida)

    if len(valida) > 0:
        print("Ja existe esta matricula")
        calculaMatricula()
    else:
        print("Matricula ok")
        



if __name__ == '__main__':
    calculaMatricula()
    

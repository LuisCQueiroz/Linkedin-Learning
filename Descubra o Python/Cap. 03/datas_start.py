#
# Arquivo com exemplos de manipulação de  datas
#
from datetime import date
from datetime import time
from datetime import datetime

def ManipulaDataHora():
    hoje = date.today()
    print("Hoje é dia: ", hoje)
    print("Partes da data:")
    print("Dia: ", hoje.day)
    print("Mês: ", hoje.month)
    print("Ano: ", hoje.year)
    print("Número do dia da semana: ", hoje.weekday())
    dias =["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira","Sexta-Feira", "Sábado", "Domingo"]
    print("Dia da semana: ", dias[hoje.weekday()])

    data = datetime.now()
    print("Data e hora: " , data)

    tempo = datetime.time(data)
    print("Hora Atual: ", tempo)



ManipulaDataHora()

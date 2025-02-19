import datetime
import locale

anoNasc = int(input("Informe o seu ano de nascimento: "))
anoAtual = datetime.datetime.now().year

alistamento = anoAtual - anoNasc

tempo =abs(17 - alistamento)

if alistamento <= 16:
    print("Você vai precisar se alistar, mas não agora.")
    print("Ainda faltam {} ano(s) para você se alistar".format(tempo))
    print("O seu alistamento será em {}.".format(anoAtual + tempo))

elif alistamento <= 18:
    print("Você precisa se alistar.")

elif alistamento > 18:
    print("Você já passou do período de alistamento.")
    print("Você se alistou há {} anos.".format(tempo))
    print("Seu alistamento foi em {}".format(anoAtual - tempo))

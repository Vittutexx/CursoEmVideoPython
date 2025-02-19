import datetime
maioridade = 0
menoridade = 1
for x in range(1, 8):
    ano = int(input("Qual o ano em que você nasceu?"))
    anoAtual = datetime.datetime.now().year
    if (anoAtual - ano) > 21:
        maioridade += 1
    else:
        menoridade += 1
print('''
Ao todo, as pessoas que chegaram na maioridade foram {}.
E as pessoas que ainda são menores de idade são {}'''.format(maioridade,menoridade))
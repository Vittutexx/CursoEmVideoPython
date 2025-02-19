import datetime
trabalhador = dict()
trabalhador['Nome'] = str(input("Nome: "))
trabalhador['Idade'] =  datetime.datetime.now().year - int(input('Ano de Nascimento: '))
trabalhador['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if trabalhador['CTPS'] != 0:
    trabalhador['Ano de Contratação'] = int(input("Ano de Contratação: "))
    trabalhador['Salário'] = float(input('Salário: R$'))
    trabalhador['Aposentadoria'] = ((trabalhador['Ano de Contratação'] + 35) - datetime.datetime.now().year) + trabalhador['Idade']
print('=-'*50)
print(trabalhador)
for c,v in trabalhador.items():
    print(f' - {c} tem o valor {v}')
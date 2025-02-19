aluno = dict()
aluno['Nome']= str(input("Nome: "))
aluno['Media'] = float(input(f"Media de {aluno['Nome']}: "))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
for c,v in aluno.items():
    print(f'{c} é igual a {v}')
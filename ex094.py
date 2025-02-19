pessoas = list()
pessoa = dict()
mulher = list()
soma = 0
while True: # Coleta dos dados
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo: [F/M] ')).strip().upper()[0]
    while pessoa['Sexo'] not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        pessoa['Sexo'] = str(input('Sexo: [F/M] ')).strip().upper()[0]
    pessoa['Idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    soma += pessoa['Idade']
    if 'F' in pessoa['Sexo']:
        mulher.append(pessoa['Nome'])
    continuar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    while continuar not in 'SN':
        print('ERRO! Responda apenas S ou N')
        continuar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if 'N' in continuar:
        break
print('-='*40) # Análise dos dados
media = soma / len(pessoas)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {media:.1f} anos.')
print(f'- As mulheres cadastradas foram: ',end='')
for x in mulher:
    print(x,end=' ')
print()
print(f'- Lista das pessoas que estão acima da média:')
for pos, i in enumerate(pessoas):
    if pessoas[pos]['Idade'] > media:
        print(f'   nome = {pessoas[pos]["Nome"]};', end=' ')
        print(f'sexo = {pessoas[pos]["Sexo"]};', end=' ')
        print(f'idade = {pessoas[pos]["Idade"]};')
print('<< ENCERRADO >>')

qtdHomens = qtdMulheres = qtdPessoas = 0
while True:
    print('_'*40)
    print('CADASTRE UMA PESSOA')
    print('_'*40)
    idade = int(input("Me informe sua idade: "))
    sexo = ' '
    continuar = ' '
    while sexo not in 'MmFf':
        sexo = str(input("Me informe o seu sexo [F/M] ")).strip().upper()[0]
    print('_'*40)
    if idade >= 18:
        qtdPessoas += 1
    if idade < 20 and sexo == 'F':
        qtdMulheres += 1
    if sexo == 'M':
        qtdHomens += 1
    while continuar not in 'SsNn':
        continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continuar == 'N':
        break
print(f'A quantidade de pessoas cadastradas maior de 18 anos é de {qtdPessoas} pessoas.')
print(f'Ao todo temos {qtdHomens} homens cadastrados.')
print(f'A quantidade de mulheres menores de 20 anos é de {qtdMulheres}.')
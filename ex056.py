idades = 0
maisVelho = 0
qtdMulheresJovens = 0
nomeMaisVelho = ''
for x in range(1, 5):
    nome = str(input("Qual o seu nome? ")).strip()
    idade = int(input("Qual a sua idade? "))
    genero = str(input('Qual seu genero? \'M\' ou \'H\'? ')).strip()
    idades += idade
    if x == 1 and genero == 'H'.lower():
        maisVelho = idade
        nomeMaisVelho = nome
    else:
        if idade > maisVelho and genero == 'H'.lower():
            maisVelho = idade
            nomeMaisVelho = nome
    if genero == 'M'.lower() and idade < 20:
        qtdMulheresJovens += 1
print("Total de mulheres com menos de 20 anos de idade: {}".format(qtdMulheresJovens))
print("Media de idade do grupo: {}".format(idades / 4))
print("A idade do mais Velho é: {} anos e ele se chama {}".format(maisVelho,nomeMaisVelho))





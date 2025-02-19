from random import randint
cont = 0
parouimpar = ''
while True:
    valor1 = int(input("Digite um valor: " ))
    valorpc = randint(0, 11)
    soma = valor1 + valorpc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input("Par ou Impar? [P/I]")).strip().upper()[0]
    print('_' * 60)
    if tipo == 'I':
        if soma % 2 == 0:
            parouimpar = 'PAR'
            print(f'Você jogou {valor1} e o computador jogou {valorpc}. Total de {soma} deu {parouimpar}')
            print("Você Perdeu!")
            break
        else:
            parouimpar = 'IMPAR'
            print(f'Você jogou {valor1} e o computador jogou {valorpc}. Total de {soma} deu {parouimpar}')
            print("Você Ganhou!")
            print("Vamos jogar novamente...")
            cont += 1
    if tipo == 'P':
        if soma % 2 == 1:
            parouimpar = 'IMPAR'
            print(f'Você jogou {valor1} e o computador jogou {valorpc}. Total de {soma} deu {parouimpar}')
            print("Você Perdeu!")
            break
        else:
            parouimpar = 'PAR'
            print(f'Você jogou {valor1} e o computador jogou {valorpc}. Total de {soma} deu {parouimpar}')
            print("Você Ganhou!")
            print("Vamos jogar novamente...")
            cont += 1
print(f'GAME OVER! Você venceu {cont} vezes consecutivas.')


jogador = dict()
jogadores = list()
while True: #Coleta de dados
    print('-' * 40)
    jogador['Nome'] = str(input('Nome do Jogador: '))
    jogador['Gols'] = []
    partida = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for x in range(0,partida):
        gols = int(input(f'Quantos gols na partida {x+1}? '))
        jogador['Gols'].append(gols)
    jogador['Total'] = sum(jogador['Gols'])
    jogadores.append(jogador.copy())
    continuar = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
    if continuar == 'N': #Ao digitar que não quer mais coletar os dados, o sistema retorna a tabela do aproveitamento dos jogadores.
        print(f'{"cod"}',end=' ')
        for x in jogadores[0].keys():
            print(f'{x:<15}',end='')
        print()
        print('-'*40)
        for k,v in enumerate(jogadores):
            print(f'{k:>3} ', end='')
            for d in v.values():
                print(f'{str(d):<15}', end='')
            print()
        print('-'*40)
        break
while True: # Criação da sequência de quantos gols foram feitos em cada partida de cada jogador.
    dados = int(input("Mostrar dados de qual jogador? "))
    print('-'*40)
    if dados == 999:
        print('<<< VOLTE SEMPRE >>>')
        break
    if dados >= len(jogadores): #Se o dado não for um índice da lista, ou seja, não for um codigo do jogador, retorna erro
        print(f'ERRO! Não existe jogador com código {dados}!')
        dados = int(input("Mostrar dados de qual jogador? "))
    if dados in range(0, len(jogadores)): #Levantamento do jogador escolhido
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[dados]["Nome"]}')
    for x in range(0, len(jogadores[dados]['Gols'])):
        print(f'{" ":>3} => No jogo {x+1}, fez {jogadores[dados]["Gols"][x]} gols.')


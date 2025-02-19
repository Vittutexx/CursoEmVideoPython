def ficha(nome = '<Desconhecido>', gols = 0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')
jogador = str(input('Nome do jogador: ')).strip()
gol = str(input('Números de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if jogador.strip() == '':
    ficha(gols = gol)
else:
    ficha(jogador,gol)
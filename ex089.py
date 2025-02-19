alunos = [[],[[],[]]]
media = 0
while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos[0].append(nome)
    alunos[1][0].append(nota1)
    alunos[1][0].append(nota2)
    alunos[1][1].append(media)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if 'N' in continuar:
        print('No.  NOME      MÉDIA')
        print('-' * 30)
        for x in range(0, len(alunos[0])):
            print(f'{x:<5}', end='')
            print(f'{alunos[0][x]:<9}', end='')
            print(f'{alunos[1][1][x]:^9.1f}')
        print('-' * 30)
        break
while True:
    notas = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if notas == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    else:
        for x in range(0, len(alunos[0])):
            print(f' Notas de {alunos[0][notas]} são: [{alunos[1][0][notas + notas]}, {alunos[1][0][notas + notas + 1]}] ')
            print('-' * 30)
            break


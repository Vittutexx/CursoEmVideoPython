cores = {'Titulo': "\033[1;97;102m", 'Busca': "\033[1;97;104m", 'Resultado': "\033[0;90;107m", 'FIM': "\033[1;97;101m"}
def texto(msg, cor = None):
    tam = len(msg) + 4
    print(f'{cor}{"~"*tam}')
    print(f'{msg:^{tam}}')
    print(f'{"~"*tam}')
while True:
    texto('SISTEMA DE AJUDA PyHELP', cores['Titulo'])
    fun = str(input('\033[mFunção ou Biblioteca > '))
    if 'FIM' in fun.upper():
        texto('ATÉ LOGO!', cores['FIM'])
        break
    texto(f"Acessando o manual do comando '{fun}'", cores['Busca'])
    print(cores['Resultado'],end = '')
    help(fun)
    print('\033[m', end='')

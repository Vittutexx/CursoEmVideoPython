def area():
    print(f'{"Controle de terrenos":^25}')
    print('-'*25)
    l = float(input('LARGURA (m): '))
    h = float(input('COMPRIMENTO (m): '))
    area = l * h
    print(f'A área de um terreno {l}x{h} é de {area}m².')
area()
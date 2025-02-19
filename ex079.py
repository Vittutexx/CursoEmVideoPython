lista = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor duplicado! não vou adicionar')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if 'N' in continuar:
        break 
print(f'Você digitou os valores: {sorted(lista)}')
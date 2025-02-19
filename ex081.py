lista = []
num5 = ' '
while True:
    valor = int(input("Digite um valor: "))
    lista.append(valor)
    continuar = str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if 5 in lista:
       num5 = 'O valor 5 faz parte da lista!'
    else:
        num5 = 'O valor 5 não faz parte da lista.'
    if 'N' in continuar:
        break
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Lista de forma decrescente {lista}')
print(f'{num5}')

zeroevinte = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
res = ' '
while True:
    numero = int(input(" Escreva um numero entre 0 e 20: "))
    if 0 <= numero <= 20:
        res = zeroevinte[numero]
        print(f'Você digitou o numero {res}')
    else:
        print('Tente novamente.', end='')
    continuar = str(input("Você quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == 'N':
        break





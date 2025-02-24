def leia_dinheiro(val):
    leia = str(input(val)).strip().replace(',','.')
    while leia.isalpha():
        print(f"\033[1;31mERRO! '{leia}' é um preço inválido!\033[m")
        leia = str(input(val))
    valor = float(leia)
    return valor
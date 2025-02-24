def metade (x, cambio = False):
    half = x / 2
    return half if cambio is False else moeda(half)
def dobro(x, cambio = False):
    double = x * 2
    return double if moeda is False else moeda(double)
def aumentar(x, y = 10, cambio = False):
    increase = x + (x * (y / 100))
    return increase if cambio is False else moeda(increase)
def diminuir(x, y = 10, cambio = False):
    low = x - (x * (y / 100))
    return low if cambio is False else moeda(low)
def moeda(val, moeda = 'R$'):
    return f'{moeda}{val}'


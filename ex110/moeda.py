def metade (x, moeda = False):
    half = x / 2
    if moeda:
        cambio = 'R$'
        return f'{cambio}{half}'
    else:
        return half
def dobro(x, moeda = False):
    double = x * 2
    if moeda:
        cambio = 'R$'
        return f'{cambio}{double}'
    else:
        return double
def aumentar(x, y = 10, moeda = False):
    increase = x + (x * (y / 100))
    if moeda:
        cambio = 'R$'
        return f'{cambio}{increase}'
    else:
        return increase
def diminuir(x, y = 10, moeda = False):
    low = x - (x * (y / 100))
    if moeda:
        cambio = 'R$'
        return f'{cambio}{low}'
    else:
        return low
def moeda(val, moeda = 'R$'):
    return f'{moeda}{val}'
def resumo(val, aumento = 0, reducao = 0):
    print(f'''
{"-"*30}
{"RESUMO DO VALOR":^30}
{"-"*30}
Preço analisado: \t{moeda(val)}
Dobro do preço: \t{dobro(val, True)}
Metade do preço: \t{metade(val, True)}
{aumento}% de aumento: \t{aumentar(val, aumento, True)}
{reducao}% de redução: \t{diminuir(val,reducao,True)}
{"-"*30}
''')
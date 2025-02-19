def voto(num):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - num
    if 18 < idade < 65:
        return f'Com {idade} anos: Voto obrigatório'
    elif idade < 16:
        return f'Com {idade} anos: Voto negado'
    elif idade == 16 or idade > 65:
        return f'Com {idade} anos: Voto opcional'
print('-'*30)
ano = int(input("Em que ano você nasceu? "))
print(voto(ano))
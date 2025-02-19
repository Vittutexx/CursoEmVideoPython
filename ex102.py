def fatorial(num = 1, show = False):
    """
    -> Calcula o Fatorial de um número.
        :param num: O numero a ser calculado.
        :param show (Opcional): Mostra ou não a conta.
        :return: O valor do Fatorial de um número 'num'.
    """
    f = 1
    if show:
        n = num
        print(f'{n}', end=' ')
        while True:
            if n == 1:
                break
            f *= n
            n -= 1
            print(f'x {n}',end=' ')
        return f'= {f}'
    else:
        for x in range(num, 0, -1):
            f *= x
        return f'Resultado: {f}'
print(fatorial(5))
help(fatorial)
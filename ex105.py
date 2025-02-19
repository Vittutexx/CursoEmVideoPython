def notas(*num, sit = False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num:  uma ou mais notas dos alunos
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    tam = len(num)
    media = sum(num) / tam
    maior = menor = 0
    for pos, x in enumerate(num):
        if pos == 0:
            maior = x
            menor = x
        else:
            if x > maior:
                maior = x
            elif x < menor:
                menor = x
    notas = {'Total': tam, 'A maior nota': maior, 'Menor nota': menor, 'Media': media}
    if sit:
        if 6 < media < 8:
            notas['Situação'] = 'RAZOÁVEL'
        elif 8 < media:
            notas['Situação'] = 'ÓTIMO'
        elif media < 6:
            notas['Situação'] = 'RUIM'
    return notas
resp = notas(10,10,6.5)
print(resp)

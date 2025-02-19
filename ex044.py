precoNormal = float(input("Informe o preço do produto: R$"))

condicao = str(input("Qual a condição de pagamento?\n"
                     "[ 1 ] À vista\n"
                     "[ 2 ] À vista no cartão\n"
                     "[ 3 ] Em até 2x no cartão\n"
                     "[ 4 ] 3x ou mais\n"))


if condicao == '1':
    precoAjustado = precoNormal - (precoNormal * 0.1)
    print("Valor total a pagar: {}".format(precoAjustado))
elif condicao == '2':
    precoAjustado = precoNormal - (precoNormal * 0.05)
    print("Valor total a pagar: {}".format(precoAjustado))
elif condicao == '3':
    print("Valor total a pagar: {}".format(precoNormal))
elif condicao == '4':
    precoAjustado = precoNormal + (precoNormal * 0.20)
    print("Valor total a pagar: {}".format(precoAjustado))

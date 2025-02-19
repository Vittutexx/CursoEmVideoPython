valorCasa = float(input("Qual o valor da casa? "))
salario = float(input("Qual o seu salário? "))
anos = float(input("Em quantos anos você vai pagar o empréstimo? "))

prestacaoMensal = (valorCasa / anos) / 12

desconto = salario * 0.30

if prestacaoMensal >= desconto:
    print("O valor da prestação mensal: {:.2f}".format(prestacaoMensal))
    print("Infelizmente o valor da prestação excedeu 30% do valor do seu salário.\nO que significa que seu empréstimo ficará indeferido.")
else:
    print("Valor da prestação mensal: {:.2f}".format(prestacaoMensal))
    print("Status da solicitação: Deferido")

preco = float(input("Informe aqui o preço do produto: "))

desc = preco * (5 / 100)

preco2 = preco - desc

print("Você irá pagar {} pois ganhou 5% de desconto.".format(preco2))

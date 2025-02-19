produtoBarato = produtos1000 = totalP = 0
nomeMaisBarato = ''
while True:
    nome = str(input("Qual o nome do produto? ")).strip()
    preco = int(input("Qual o preço do produto? R$"))
    totalP += preco
    if totalP == preco or preco < produtoBarato:
        produtoBarato = preco
        nomeMaisBarato = nome
    if preco >= 1000:
        produtos1000 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total da compra foi R${totalP:.2f}')
print(f'Temos {produtos1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomeMaisBarato} e custou R${produtoBarato:.2f}')

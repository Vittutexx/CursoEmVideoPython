while True:
    print('_' * 40)
    valor = int(input("Qual numero você deseja fazer a tabuada? "))
    print('_' * 40)
    if valor < 0:
        break
    for x in range (1,11):
        print(f'{valor} x {x} = {valor * x}')
print("FIM DO PROGRAMA")




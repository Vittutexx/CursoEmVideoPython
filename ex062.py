x = int(input("Insira o valor do primeiro termo: "))
r = int(input("Insira o valor da razão: "))
contagem = 0
qtd = 10
while contagem != qtd:
    print(x, end=' ')
    x += r
    contagem +=1
    if contagem == qtd:
        print("PAUSA")
        maisnum = int(input("\nQuantos termos você deseja mostrar a mais? "))
        qtd += maisnum
        if maisnum != 0:
            print(x, end=' ')
        else:
            contagem = qtd
print("Progressão finalizada com {} termos mostrados.".format(contagem))







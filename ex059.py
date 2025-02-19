from time import sleep
menu =  0
valor1 = int(input("Informe o primeiro valor: "))
valor2 = int(input("Informe o segundo valor: "))
while menu != 5:
    menu = int(input('''
    Informe qual operação deseja realizar
    ===============================
    [1] - Soma
    [2] - Multiplicação
    [3] - Maior
    [4] - Novos números
    [5] - Sair do programa
    ===============================
    Qual opção você deseja? '''))
    if menu == 1:
        print("="*4,' SOMA ' ,'='*4)
        soma = valor1 + valor2
        print("O resultado da soma entre os valores {} e {} é {}".format(valor1,valor2,soma))
        sleep(2)
    elif menu == 2:
        print("="*4,' MULTIPLICAÇÃO ' ,'='*4)
        multiplicacao = valor1 * valor2
        print("O resultado da soma entre os valores {} e {} é {}".format(valor1,valor2,multiplicacao))
        sleep(2)
    elif menu == 3:
        print("="*4,' VALOR MAIOR ' ,'='*4)
        if valor1 > valor2: print("O maior valor é: {}".format(valor1))
        else: print("O maior valor é: {}".format(valor2))
        sleep(2)
    elif menu == 4:
        print("="*4,' OUTROS VALORES ' ,'='*4)
        valor1 = int(input("Informe o primeiro valor: "))
        valor2 = int(input("Informe o primeiro valor: "))
        sleep(2)
    elif menu == 5:
        print("Finalizando...")
        sleep(1)
        print("==== FIM DO PROGRAMA ====")
    else:
        print("Opção inválida. Tente novamente")
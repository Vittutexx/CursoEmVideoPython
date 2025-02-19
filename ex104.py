def leiaInt(numb):
    text = str(input(numb))
    while True:
        if text.isnumeric():
            num = int(text)
            break
        else:
            print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
            text = str(input(numb))
    return num
n = leiaInt('Digite um número: ')
print(f'\033[1;97mVocê acabou de digitar o número \033[m\033[1;30;102m[{n}]\033[m')
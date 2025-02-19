exp = str(input("Informe a expressão: "))
lista = []
for x in exp:
    if x == '(':
        lista.append('(')
    elif x == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print("Sua lista está válida!")
else:
    print('Sua lista está inválida.')
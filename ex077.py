palavra = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON')
palavras = ' '
for p in palavra:
    print(f'\nNa palavra {p} temos ', end='')
    for letra in p:
        if letra in 'AEIOU':
            print(f"{letra.lower()}", end= ' ')


soma = 0

for c in range(1, 501, 2):
    print(c, end=' ')
    if c % 3 == 0:
        soma += c
print("\nsoma dos ímpares:",soma)


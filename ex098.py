from time import sleep
def contador():
    i = 1
    f = 10
    p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    for x in range(i,f + 1,p):
        print(x, end=' ')
        sleep(0.25)
    print('FIM')
    i = 10
    f = -1
    p = -2
    print(f'Contagem de {i} até {0} de {abs(p)} em {abs(p)}')
    for x in range(i,f,p):
        print(x,end =' ')
        sleep(0.25)
    print('FIM')
    print('-='*30)
    print('Agora é sua vez de personalizar a contagem!')
    i = int(input("Inicio: "))
    f = int(input("Fim: "))
    p = int(input("Passo: "))
    val = 0
    if p == 0:
        p = 1
    elif f < i and p == abs(p) * (-1):
        val = p
    elif f < i :
        val = p *(-1)
    print(f'Contagem de {i} até {f} de {abs(p)} em {abs(p)}')
    for x in range(i,f - 1,val):
        print(x,end=' ')
        sleep(0.25)
    print('FIM')
contador()

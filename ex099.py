from time import sleep
def maior(* num):
    maior = 0
    print('-='*40)
    print('Analisando os valores passados...')
    for x in num:
        if x > maior:
            maior = x
        print(x, end=' ')
        sleep(0.25)
    print(f'Foram informados {len(num)} ao todo.')
    print(f'O maior valor informado foi {maior}')
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior(0)
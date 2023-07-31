from time import sleep
def contador (i, f, p): # i= iniçio, f = fim, p = passo
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(0.5)

    if i < f:
        cont = 1
        while cont <= f:
            print(f'{cont} ', end='')#Contagem Crescente
            sleep(0.5)
            cont +=p
        print('FIM!')
    else:
        cont= i
        while cont >=f:
            print(f'{cont} ', end='')# Contagem decrescente
            sleep(0.5)
            cont -=p
        print('FIM')
print('-=' * 20)
contador(1, 10, 1)
contador(10, 0, 1)
print('-='*30)
print('Agora é sua vez de personalizar a contagem ')
ini = int(input('INICIO:  '))
fim = int(input('FIM:  '))
passo= int(input('PASSO:  '))
contador(ini, fim, passo)


def leiaInt(msg):
    ok = False
    valor =0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0;31mErro! Digite um número inteiro válido\033[m')#\033[0;31m= comecando a cor,  \033[m= fim da cor
        if ok:
            break
    return valor




n = leiaInt('Digite um número: ')
print(f'Voçê acabou de digitar o número {n}')
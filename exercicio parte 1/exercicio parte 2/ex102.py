
def fatorial(n, show= False):
    '''
    -> Calcula o fatorial de um número
    :param n: o número a ser calculado
    :param show: o parametro opcional para mostrar ou na a contagem: 5x4x3x2x1=120
    :return: returna o valor de um fatorial
    '''
    f=1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c>1:
             print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f




print(fatorial(5,show=True))
help(fatorial)
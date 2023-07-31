def área(larg, comp):
    a = larg*comp
    print(f'A área de um terreno {larg}x{comp} é de {a}m2')


print(' Controle de terrenos')
print('-'*30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)

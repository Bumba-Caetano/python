while True:
    n= int(input('Quer ver a tabuada de que número? '))
    print('-' * 10)
    if n <0:
        break

    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')

    print('-'*11)
print('Programa Encerrado. Volte sempre!')

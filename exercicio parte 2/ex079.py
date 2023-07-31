números = list ()
while True:
    n = int(input('Digite um número: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor dublicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] '))
    if r in 'Nn':
        break
print('=-'*30)
números.sort()
print(f'Voçê digitou os valores {números}')


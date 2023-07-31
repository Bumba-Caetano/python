from random import randint
v=0
while True:
    jogador = int (input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not  in 'PI':
        tipo= str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Voçê jogou {jogador} e o computador {computador}. Total de {total}')
    print('DEU PAR' if total % 2==0 else 'DEU IMPAR', end= ' ')
    if tipo=='P':
        if total % 2==0:
            print('Voçê ganhou!')
            v+=1
        else:
            print('Voçê perdeu!')
            break
    elif tipo =='I':
        if total % 2 ==1:
            print('Voçê venceu!')
            v +=1
        else:
            print('Voçê perdeu')
            break
        print('vamos jogar novamente...')
print(f'GAME OVER! voçê venceu {v} vezes')


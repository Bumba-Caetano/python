from time import sleep
from random import randint
itens=('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL 
[2] TESOURA
''')
jogador=int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
print('-='*12)
print('Computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-='*12)

if computador==0: #Computador jogou Pedra
    if  jogador ==0:
            print('EMPATE')
    elif jogador == 1:
            print('JOGADOR VENCE')
    elif jogador ==2:
            print('COMPUTADOR VENCE')
    else:
        print('Jogada inválida')
elif computador ==1: #Computador jogou papel
    if jogador== 0:
        print('Computador Vence')

    elif jogador==1:
        print('EMPATE')
    elif jogador ==2:
            print('JOGADOR VENCE')
    else:
        print('Jogada inválida')

elif computador==2: #Computador jogou tesoura
    if jogador ==0:
        print('JOGADOR VENCE')
    elif jogador==1:
            print('COMPUTADOR VENCE')
    elif jogador ==2:
        print('EMPATE')
    else:
        print('jogada inválida')

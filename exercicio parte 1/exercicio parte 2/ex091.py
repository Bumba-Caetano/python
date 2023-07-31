from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
}
ranking= list()
print('Os valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
ranking= sorted(jogo.items(), key=itemgetter(1), reverse=True)# colocar valores em ordem, comecando pelo maior valor dentro de um dicionario
print(ranking)
print('-='*30)
print('=== RANKIING DOS JOGADORES ===')
for i ,v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)



jogador = dict()
partidas = list()
jogador['nome']= str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f'Quantos golos na partida {c+1}? ')))
jogador['golos']=partidas[:]
jogador['total']= sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'  -O campo {k} tem o valor {v}')
print('-='*30)

print(f'O jogador{jogador["nome"]} jogou {len(jogador["golos"])} partidas')
for i, v in enumerate(jogador['golos']):
    print(f' => Na partida {i}, fez {v} golos')
print(f'Foi um total de {jogador["total"]} golos')




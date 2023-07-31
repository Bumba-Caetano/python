
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()#apagar o jogador antes de ler os dados dele. Por que em cada laço vai lendo dados doutro jogador
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos golos na partida {c+1}? ')))
    jogador['golos'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
         resp = str(input('Quer continuar? [S/N] ')).upper()[0]
         if resp in 'SN':
             break
         print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f' {i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>2}', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)  '))
    if busca==999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['golos']):
            print(f'   No jogo {i+1} fez {g} golos')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')




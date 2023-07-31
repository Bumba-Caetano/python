times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo',
            'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia',
           'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória',
           'Coritiba', 'Avai', 'Ponte Preta', 'Atlético-GO')

print('-='*150)
print(f'Listas de times do Brasileirão: {times}')
print('-='*150)
print(f'Os 5 peimeiros times são {times[0:5]}')
print('-='*150)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-='*150)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*150)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
print('-='*150)
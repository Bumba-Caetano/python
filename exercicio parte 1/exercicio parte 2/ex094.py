#jogar dicionário dentro de uma lista
galera = list()
pessoa = dict()
soma = média = 0


while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]#[0] é para pegar a primeira letra.
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pessoa['idade'] = int(input('Idade:  '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp= str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SsNn':
            break
        print('ERRO! Responda apenas com S ou N.')
    if resp == 'N':
        break

print('-='*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print(f'A média de idade é {média:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f' {p["nome"]} ', end='')
print()
print('Lista das pessoas que estão aima da média: ')
for p in galera:
    if p['idade'] >= média:
        print('   ', end='')
        for k, v in p.items():
            print(f' {k} = {v};', end='')
            print()
print('<<< ENCERRADO >>>')






número= int(input('Informe um número: '))
unidade= número // 1 % 10
dezena = número // 10 % 10
centena= número // 100 % 10
milhar= número // 1000 % 10
print('Analisando número {}'.format(número))
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))
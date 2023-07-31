frase = str (input('Digite uma frase: ')).upper().strip()
print('A primeirs A letra apareçe {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareçeu na posição {}'.format(frase.find('A')))
print('A última letra A apareçeu na posição {}'.format(frase.rfind('A')+1))
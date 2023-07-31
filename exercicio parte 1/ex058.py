from  random import randint
comutador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que voçê consegue advinhar qual foi?  ')
acertou = False
palpites=0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites +=1
    if jogador == comutador:
        acertou = True
    else:
        if jogador < comutador:
            print('Mais... Tente mais uma vez.')
        elif jogador > comutador:
            print('Menos... Tente mais uma vez.')
print('ACERTOU com {} tentativas parabéns'.format(palpites))

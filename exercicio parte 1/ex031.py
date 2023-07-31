distviagem= float(input('Qual é a distância da sua viagem? '))
print('Voçê está prestes a começar uma viagem de {}Km.'.format(distviagem))
'''
if distviagem <= 200:
   preço = distviagem * 0.50
else:
    preço= distviagem * 0.45
'''
preço = distviagem * 0.50 if distviagem <= 200 else distviagem * 0.45
print('E o preço da sua viagem será de {:.2f}'.format(preço))
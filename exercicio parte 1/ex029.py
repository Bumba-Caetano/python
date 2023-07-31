velocidade = float (input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Voçê excedeu o limite permetido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Voçê deve pagar uma multa de R${}'.format(multa))

print('Tenha um bom dia ! Dirija com segurança!')


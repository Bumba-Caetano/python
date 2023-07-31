salário= float(input(' Qual é o salário do Funcionário? R$'))
novosalário= salário + (salário * 15 / 100)
print('um funcionário que ganhava R${:.2f}, com 15% de desconto, passa a receber R${:.2f}'.format(salário, novosalário))
dinhero=float(input('Quanto dinheiro voçê tem na carteira? R$'))
dolar = dinhero / 3.27
print('Com R${:.2f} voçê pode comprar US${:.2f}'.format(dinhero, dolar))
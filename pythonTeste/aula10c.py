n1=float(input("Digite a Primeira Nota: "))
n2=float(input("Digite a Segunda nota: "))
m=(n1+n2)/2
print("A sua media foi {:.1f}".format(m))
print('Parabéns' if m>=6 else 'Nota ruim, Estude mais')
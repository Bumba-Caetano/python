núm=0
cont =0
soma=0
núm = int (input('Digite um número [999 para parar]: '))
while núm !=999:
    soma +=núm
    cont +=1
    núm = int(input('Digite um número [999 para parar]: '))
print('Voçê digitou {} números e a soma entre eles foi {}'.format(cont, soma))



soma = 0
cont =0

for c in range(1,7):
    num = int(input('Digite um {}º valor: '.format(c)))
    if num % 2==0:
         soma = soma + num
         cont = cont + 1
print('Voçê informou {} números pares e a soma foi {}'.format(cont, soma))
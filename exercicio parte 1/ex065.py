resp = 'S'
soma = média=0
quant=0
maior = menor=0
while resp in 'Ss':
    número= int (input('Digite um número: '))
    soma +=número
    quant +=1
    if quant ==1:
        maior = menor=número
    else:
        if número > maior:
            maior = número
        if número < menor:
            menor = número

    resp= str(input('Quer continuar [S/N] ')).upper().strip()[0]
média = soma / quant
print('Voçê digitou {} números e a média é {:.2f}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
print('Acabou')

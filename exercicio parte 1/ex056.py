

somaidade = 0
maaioridadehomem= 0
nomevelho = ''
totmulher20= 0
for p in range(1, 5):
    print('------- {}ª PESSOA -------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p==1 and sexo in 'Mm':
        maaioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maaioridadehomem:
        maaioridadehomem =idade
        nomevelho=nome
    if sexo in 'Ff' and idade < 20:
            totmulher20 += 1
médiaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maaioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher20))


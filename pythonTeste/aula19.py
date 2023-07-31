#brasil= []
#estado1={'uf': 'Rio de Janeiro','sigla': 'RJ'}
#estado2={'uf': 'São Paulo', 'Sigla': 'SP'}
#brasil.append(estado1)
#brasil.append(estado2)
#print(brasil)
estado= dict()
brasil= list()
for c in range(0,3):
    estado['uf']= str(input('Unidade Federativa: '))
    estado['sigla']= str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
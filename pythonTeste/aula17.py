#valores= []
#valores.append(3)
#valores.append(5)
#valores.append(7)
#valores.append(8)
#valores.append(1)
#valores.append(2)

#valores.sort()
#for c, v in enumerate(valores) :
    
 # print(f'Na posição {c} encontrei o valor {v}!')
#print("Cheguei ao  final da lista")  
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um numero: ')))

for c ,v in enumerate(valores):

    print(f'Na posição {c} encontrei o valor {v}!')    
print('Cheguei ao Final da Lista')

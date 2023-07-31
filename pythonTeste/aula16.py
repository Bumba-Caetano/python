#
#
#
#
#
#
#
#
#

#
#
#                      lanche=('Hamburguer', 'Pudim', 'Pizza', 'Batata Frita', 'Suco')
#      for cont in range(0, len(lanche)):
#     print(f'Eu vou comer {lanche[cont]} na posição {cont}')
#
#      for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos} ') #posição
#     for comida in lanche:
#     print(f'Eu vou comer {comida}')
#     print('Fim do programa')
#     print(sorted(lanche))
#
#
#
#
#num = [3,2, 1, 5,7,6,4, 8,9]
#num.sort()
#num.remove(3)
#num.append(0)
#print(type(num))
#print(num)
#print(f"Essa lista tem {len(num)} elementos")

#
#
#
#
#
#  pessoa=('Bumba', 23, 'M')
#    print(pessoa)
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

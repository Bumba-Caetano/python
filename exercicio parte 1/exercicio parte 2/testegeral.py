
'''

número= int(input('Digite um número: '))
antecessor= número - 1
sucessor = número + 1
print('O número {} seu antecessor é {} e o seu sucessor é {}'.format(número, antecessor, sucessor))



número = float (input('Digite um número: '))
raiz = pow(número, (1/2))
print('A raiz quadrada de {} é {:.2f}'.format(número, raiz))


número=  int(input('Digite um número para ver a sua tabuada: '))
print('{} x {:2} = {}'.format(número, 1, número*1))
print('{} x {:2} = {}'.format(número, 2, número*2))


real = float(input('Quanto dinheiro voçê tem na carteira? '))
dolar= real / 3.27
print('O')


import math

catetooposto =   float (input('Cateto Oposto: '))
catetoadjacente = float(input('Cateto Adjacente: '))
hipotenusa = math.hypot(catetooposto, catetoadjacente)
print(' A hipotenusa é {:.2f}'.format(hipotenusa))


import math
ângulo=float(input('Valor do ângulo: '))

seno=math.sin(math.radians(ângulo))
coseno= math.cos(math.cos(ângulo))
tg= math.tan(math.radians(ângulo))
print('O Seno de {} é {}'.format(ângulo, seno))

import random
n1=str(input('Primeiro aluno: '))
n2= str(input('Segundo Aluno: '))
lista= [n1, n2]
escolhido= random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

'''

import cv2

img = cv2.imread('OpenCV_Logo.png', cv2.IMREAD_COLOR)

cv2.namedWindow('Hello World')
cv2.imshow('Hello World', img)
cv2.waitKey()
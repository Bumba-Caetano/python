import math
ângulo = float (input('Digite o ângulo que voçê deseja: '))

seno = math.sin(math.radians(ângulo))
coseno = math.cos(math.radians(ângulo))
tangente= math.tan(math.radians(ângulo))
print('O ângulo {} tem o Seno {:.2f}'.format(ângulo, seno))
print('O ângulo {} tem o Coseno {:.2f}'.format(ângulo, coseno))
print('O ângulo {} tem o Tangente {:.2f}'.format(ângulo, tangente))


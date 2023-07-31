import math
catetooposto=float(input('Comprimento do cateto oposto: '))
catetoadjacente= float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(catetooposto, catetoadjacente)
#hipontenusa = (catetooposto ** 2 + catetoadjacente ** 2)** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))
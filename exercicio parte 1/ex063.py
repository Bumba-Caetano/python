print('-'*33)
print('Sequências de Fibonacci')
print('-'*33)
número = int(input('Quantos termos voçê quer mostrar? '))
t1 = 0
t2 = 1
print('~'*33)
print('{} -> {}'.format(t1, t2), end= '')
cont =3
while cont <= número:
    t3 = t1+t2
    print(' -> {}'.format(t3), end= '')
    t1=t2
    t2= t3
    cont+=1
print(' FIM')

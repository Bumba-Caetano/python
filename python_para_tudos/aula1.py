x= input('Insira a temperatura em Fahrenhrit: ')
try:
    fahr= float(x)
    cel = (fahr -32.0 ) * 5.0/9.0
    print(cel)
except:
    print('Por favor introduza um número.')
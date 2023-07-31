
print('-=-'*16)
print('Analisador de Triângulos')
print('-=-'*16)
r1= float(input('Primeiro Segmento: '))
r2= float(input('Segundo Segmento: '))
r3= float(input('Terceiro segmento: '))
if r1< r2 + r3 and r2< r1+ r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
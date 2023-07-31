largura=float(input('Largura da parede: '))
altura=float(input('Altura da parede: '))
área= largura * altura
print('Sua parede tem a dimensão de {} x {} e sua área é de {}mxm.'.format(largura, altura, área))
tinta = área /2
print('Para pintar essa parede, voçê precisará de {}l de pinta.'.format(tinta))

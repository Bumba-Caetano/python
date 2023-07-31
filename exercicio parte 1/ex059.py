from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção= 0
while opção !=5:

    print('''
        [1] somar
         [2} multiplicar
        [3] maior
        [4] novos números
        [5] sair do programa
    ''')
    opção = int(input('>>>>>> Qual é a sua opção? '))
    if opção==1:
        soma= n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))
    elif opção==2:
        multiplicar = n1 * n2
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, multiplicar))
    elif opção ==3:
            if n1 >n2:
                maior= n1
            else:
                maior = n2
            print('Entre {} e {} o maior valor digitado é {}'.format(n1, n2, maior))
    elif opção==4:
            print('Informe os números novamente: ')
            n1= int(input('Primeiro valor: '))
            n2 = int(input('Segundo valor: '))
    elif opção==5:
            print('Finalizando...')
            sleep(2)
    else:
        print('Opçaão inválida. tente novamente')
    print('=-='*10)
print('Fim do programa! Volte sempre')


#Maiores valores passados por parametros:
#Desenpacotamento de funções(parametros), * = quer dizer desenpacotar parametros, vai receber varios parametros
from  time import sleep
def maior(* núm):
    cont = maior=0
    print(f'\nAnalisando os valores passados...')
    for valor in núm:
        print(f'{valor} ', end='')
        sleep(0.5)
        if cont ==0:
            maior= valor
        else:
            if valor > maior:
                maior = valor
        cont +=1
    print(f'Foram informados {cont} valores ao todo')
    print(f'o maior valor informado foi {maior}.')
maior(2, 9, 4 ,5, 7, 1)
maior(1,2,4,6)
maior(8, 9, 5, 1,2 )
maior(1, 8, 4, 9, 6)
maior(0)
maior(6)
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mPor favor digite um número inteiro válido.\033[m')
            continue # continue joga no while de novo, vai tentar novamente a condição
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
            break
        else:
            return  n
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mPor favor digite um número real válido.\033[m')
            continue # continue joga no while de novo, vai tentar novamente a condição
        except (KeyboardInterrupt):
            print('\n\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
            break
        else:
            return  n
num = leiaInt('Digite um valor: ')
num2= leiaFloat('Digite um real: ')
print(f'O valor digitado foi {num} e o real {num2}')


def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada= str(input(msg)).replace(',', '.').strip() #Trocar ponto. por virgula,
        if entrada.isalpha() or entrada =='':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço Inválido\033[m')
        else:
            válido = True
            return  float(entrada)

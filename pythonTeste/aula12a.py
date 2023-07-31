nome= str(input("Qual é o seu nome: "))
if nome=='Bumba':
    print("Que nome Bonito!")
elif nome=='Pedro' or nome=='Joao' or nome=='Maria' or nome=='Paulo':
    print("Seu nome é popular em Angola!")
elif nome in 'Ana Joana Jessica Juliana':
    print("Belo nome Femenino")
elif nome in 'Caetano Andre Jose Mariano':
    print('Belo nome Masculino')
else:
    print("Seu é muito Normal.")
print("Tenha um bom dia {}!".format(nome))
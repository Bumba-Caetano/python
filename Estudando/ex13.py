nota1=float(input("Digite a primeira nota do aluno: "))
nota2=float(input("Digite a segunda nota do aluno: "))
media=(nota1+nota2)/2
if media<5.0:
    print("Reprovado: {}".format(media))
elif media==5.0 or media<6.9:
    print("Recuperacao {} ".format(media))
else:
    print("Aprovado {}".format(media))
print("Fim do Programa")
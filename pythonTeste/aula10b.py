n1=float(input("Digite a Primeira Nota: "))
n2=float(input("Digite a Segunda nota: "))
m=(n1+n2)/2
if m>=10:
    print("Voce Aprovou com a media {:.1f} ".format(m))
else:
    #print("Reprovado")
    print("Voce Reprovou com media {:.1f} ".format(m))
print("======FIM==DO==PROGRAMA======")
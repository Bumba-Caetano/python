#c=1
#while c< 11:
 #   print(c)
  #  c=c+1
#print("Fim do programa")
#n=1
#while n !=0:
   # n=int(input("Digite um valor: "))
#print("Fim")
n = 1
par = impar =0
while n!=0:
    n=int(input("Digite um valor: "))
    if n !=0:
        if n%2==0:
         par+=1
        else:
            impar+=1

print("Voçê digitou {} números pares e {} números impares!".format(par, impar))



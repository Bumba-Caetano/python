#teste = list()
#teste.append("Bumba")
#teste.append(23)
#galera= list()
#galera.append(teste[:])
#teste[0]='Caetano'
#teste[1]= 22
#galera.append(teste[:])
#print(galera)

#galera = [['Bumba', 23], ['Gerri', 27], ['Hossi', 24], ['SaFad', 25]]
#for p in galera:
 #   print(p[0])
galera=list()
dado= list()
totmai=totmen=0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1]>=21:
        print(f"{p[0]} é o maior de idade.")
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen+=1

print(f'{totmai} Maiores e {totmen} Menores de idade')    
#print(galera)
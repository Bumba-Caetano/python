#Matriz em Python
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Três listas dentro de uma lista
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')

    print()
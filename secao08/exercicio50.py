import numpy as np


def soma_alg():
    matriz = np.zeros([3, 3], int)
    soma = 0

    for l in range(3):
        for c in range(3):
            matriz[l][c] = int(input(f'Número [{l + 1}, {c + 1}]: '))

            if l == c:
                soma += matriz[l][c]
    print(matriz)
    return f'A soma dos algarismos da diagonal principal é {soma}'


print(soma_alg())
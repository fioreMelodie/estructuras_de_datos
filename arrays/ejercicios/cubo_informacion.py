import random

# Cubo 3D de tamaño 1x1x5 (como una fila dentro de un cubo)
cubo = [[[random.randint(1, 100) for _ in range(5)]]]  

print("Cubo generado:", cubo)

# Como solo hay 5 números, los saco en una lista normal
numeros = cubo[0][0]

# Procesos
print("\n========== CUBO DE INFORMACIÓN ==========")
print("Números:", numeros)
print("Suma total:", sum(numeros))
print("Mayor:", max(numeros))
print("Menor:", min(numeros))
print("Ordenados:", sorted(numeros))
print("=========================================")

import random

# Crear una lista con 5 números aleatorios entre 1 y 100
numeros = [random.randint(1, 100) for _ in range(5)]

print("Números generados:", numeros)

# Suma total
print("Suma:", sum(numeros))

# Mayor y menor
print("Mayor:", max(numeros))
print("Menor:", min(numeros))

# Ordenar
numeros.sort()
print("Ordenados:", numeros)

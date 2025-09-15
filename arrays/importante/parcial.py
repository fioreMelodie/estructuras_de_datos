# ================================
# ESTRUCTURAS DE DATOS EN PYTHON
# Arrays - Matrices - Cubos
# ================================

# ----------- ARRAYS (listas simples) -----------
print("\n=== ARRAYS ===")
numeros = [10, 20, 30, 40, 50]

print("Array:", numeros)

# Recorrer
for n in numeros:
    print("Elemento:", n)

# Primer y último
print("Primero:", numeros[0])
print("Último:", numeros[-1])

# Tamaño, suma, máximo y mínimo
print("Cantidad:", len(numeros))
print("Suma:", sum(numeros))
print("Máximo:", max(numeros))
print("Mínimo:", min(numeros))

# Agregar y eliminar
numeros.append(60)
print("Agregado 60:", numeros)
numeros.remove(30)
print("Eliminado 30:", numeros)


# ----------- MATRICES (listas de listas) -----------
print("\n=== MATRICES ===")
matriz = [
    [1, 2, 3],   # Fila 0
    [4, 5, 6],   # Fila 1
    [7, 8, 9]    # Fila 2
]

print("Matriz:", matriz)

# Recorrer matriz
for fila in matriz:
    for elem in fila:
        print("Elemento:", elem)

# Acceso directo
print("Elemento [0][1]:", matriz[0][1])  # 2
print("Elemento [2][2]:", matriz[2][2])  # 9

# Primer y último
print("Primero:", matriz[0][0])
print("Último:", matriz[-1][-1])

# Suma total
suma_matriz = sum(sum(fila) for fila in matriz)
print("Suma total:", suma_matriz)


# ----------- CUBOS (listas de listas de listas) -----------
print("\n=== CUBOS ===")
cubo = [
    [   # Capa 0
        [1, 2],   # Fila 0
        [3, 4]    # Fila 1
    ],
    [   # Capa 1
        [5, 6],
        [7, 8]
    ]
]

print("Cubo:", cubo)

# Recorrer cubo
for capa in cubo:
    print("Capa:")
    for fila in capa:
        for elem in fila:
            print("Elemento:", elem)

# Acceso directo
print("Elemento [1][0][1]:", cubo[1][0][1])  # 6

# Primer y último
print("Primero:", cubo[0][0][0])
print("Último:", cubo[-1][-1][-1])


# ----------- RESUMEN RÁPIDO -----------
print("\n=== RESUMEN ===")
arr = [4, 8, 2, 6]
print("Array:", arr)
print("Cantidad:", len(arr))
print("Suma:", sum(arr))
print("Mayor:", max(arr))
print("Menor:", min(arr))
print("Primero:", arr[0])
print("Último:", arr[-1])
print("Ordenado:", sorted(arr))

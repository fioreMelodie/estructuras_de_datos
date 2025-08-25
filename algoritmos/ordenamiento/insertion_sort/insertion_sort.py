# Algoritmo Inserción (Insertion sort)
def ordenar_insercion(lista):
    n = len(lista)
    for i in range(1, n):
        clave = lista[i]  # elemento a insertar
        j = i - 1
        # mover los elementos mayores a la derecha
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave  # insertar en la posición correcta
    return lista

# Ejemplo
numeros = [5, 3, 8, 4, 2]
ordenados = ordenar_insercion(numeros)
print(ordenados)

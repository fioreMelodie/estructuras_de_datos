# Algoritmo Selección (Selection sort)
def ordenar_seleccion(lista):
    n = len(lista)
    for i in range(n - 1):
        indice_minimo = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j  # actualizar índice del mínimo
        # intercambiar el mínimo con el elemento en posición i
        lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
    return lista

# Ejemplo
numeros = [5, 3, 8, 4, 2]
ordenados = ordenar_seleccion(numeros)
print(ordenados)

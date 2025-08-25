# Algoritmo Quick Sort
def quick_sort(lista):
    if len(lista) <= 1:
        return lista  # lista de 0 o 1 elemento ya está ordenada

    pivote = lista[0]
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + [pivote] + quick_sort(mayores)

# Ejemplo
numeros = [5, 3, 8, 4, 2]
ordenados = quick_sort(numeros)
print(ordenados)

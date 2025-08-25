# Algoritmo Burbuja (Bubble sort)
def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                # intercambiar elementos
                temporal = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temporal
    return lista

# Ejemplo: Organizar números dentro de un array
numeros = [5, 3, 8, 4, 2]
ordenados = ordenar_burbuja(numeros)
print(ordenados)

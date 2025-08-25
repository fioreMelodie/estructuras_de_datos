# Algoritmo Merge Sort
def merge_sort(lista):
    if len(lista) <= 1:
        return lista  # lista de 0 o 1 elemento ya está ordenada

    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])

    return fusionar(izquierda, derecha)

def fusionar(izquierda, derecha):
    resultado = []
    while izquierda and derecha:
        if izquierda[0] <= derecha[0]:
            resultado.append(izquierda.pop(0))
        else:
            resultado.append(derecha.pop(0))
    # añadir los elementos restantes
    resultado.extend(izquierda)
    resultado.extend(derecha)
    return resultado

# Ejemplo
numeros = [5, 3, 8, 4, 2]
ordenados = merge_sort(numeros)
print(ordenados)

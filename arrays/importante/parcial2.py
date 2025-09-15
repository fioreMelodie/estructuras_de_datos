# En matriz
matriz = [
    [3, 5, 7],
    [1, 4, 9],
    [2, 6, 8]
]

# Tamaño de la matriz
filas = len(matriz)
columnas = len(matriz[0])
print("Filas:", filas, "Columnas:", columnas)

# Suma de cada fila
for fila in matriz:
    print("Suma fila:", sum(fila))

# Elementos de una columna
columna_1 = [fila[0] for fila in matriz]
print("Columna 1:", columna_1)

# Transpuesta (filas ↔ columnas)
transpuesta = list(zip(*matriz))
print("Transpuesta:", transpuesta)

# Máximo y mínimo de la matriz
todos = [elem for fila in matriz for elem in fila]
print("Máximo:", max(todos), "Mínimo:", min(todos))


# En cubos
cubo = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

# Sumar todo el cubo
suma_total = sum(sum(sum(fila) for fila in capa) for capa in cubo)
print("Suma cubo:", suma_total)

# Todos los elementos en una sola lista
todos = [elem for capa in cubo for fila in capa for elem in fila]
print("Todos los elementos:", todos)

print("Máximo:", max(todos), "Mínimo:", min(todos))

#📌 Funciones importantes para recordar en el parcial

👉 Para listas (arrays):

len() → cantidad de elementos

sum() → suma

max(), min() → mayor y menor

.append(x) → agrega al final

.insert(i, x) → inserta en posición

.remove(x) → elimina por valor

.pop(i) → elimina por índice (último si no se pone)

.index(x) → busca posición

.count(x) → cuántas veces aparece

.reverse() o [::-1] → invierte

.sort() o sorted(lista) → ordena

👉 Para matrices y cubos:

len(matriz) → número de filas

len(matriz[0]) → número de columnas

zip(*matriz) → transpuesta

Recorrer con for anidados

List comprehension para "aplanar" estructuras

Aplicar sum(), max(), min() sobre todas las filas o capas

arr = [10, 20, 30, 40, 50]

print(len(arr))        # Cantidad de elementos
print(sum(arr))        # Suma total
print(max(arr))        # Mayor
print(min(arr))        # Menor

print(arr.index(30))   # Posición del valor 30 → 2
print(arr.count(20))   # Cuántas veces aparece 20 → 1

arr.append(60)         # Agregar al final
arr.insert(2, 25)      # Insertar en posición 2
print(arr)

arr.remove(40)         # Eliminar valor 40
print(arr)

arr.pop()              # Eliminar último elemento
arr.pop(1)             # Eliminar en índice 1
print(arr)

arr.reverse()          # Invertir
print(arr)

print(sorted(arr))     # Ordenar en una nueva lista
arr.sort()             # Ordenar en el mismo array
print(arr)

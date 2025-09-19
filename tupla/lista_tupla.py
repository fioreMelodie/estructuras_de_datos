#Lista de reprodución
# lista_reproduccion = []

# num_canciones = int(input('Cuántas canciones desea agregar?'))

# for indice in range(num_canciones):
#     cancion = input(
#         f"Proporciona LA CANCIÓN {indice + 1}: "
#     )

# lista_reproduccion.sort(
#     reverse=True
# )

# lista_reproduccion.sort()

# print("\nIteramos el playlist")
# for cancion in lista_reproduccion:
#     print(f"-{cancion}")
    
# Hacer que las canciones se guarden en un archivo

#Tupla
mi_tupla = (1,2,3,4,5)
print(mi_tupla)

for elemento in mi_tupla:
    print(elemento, end=" ")
    
#Coordenadas

coordenadas = (3,5)
print(f"\n")
print(f"\nCoordenada en el eje x: {coordenadas[0]}")
print(f"\nCoordenada en el eje y: {coordenadas[1]}")

#Crear una tupla unitaria
tupla_un_elemento = (10,)
print(f"Tupla de un elemento: {tupla_un_elemento} ")

#Tupla anidada
tupla_anidada = (1, (2,3), (4,5))
print(f"Segundo elemento, tupla anidada {tupla_anidada[1]}")

#Ventajas de las tuplas sobre las listas
#1. Son inmutables, lo que las hace mas seguras
#2.Pueden ser usadas como claves en diccionarios
#3.Pueden ser mas rápidas que las listas en ciertas operaciones


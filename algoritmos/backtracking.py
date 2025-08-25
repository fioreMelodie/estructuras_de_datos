# Algoritmo Backtracking (Vuelta atrás)
def retroceso(maximo, objetivo, inicio=1, camino=[]):
    if objetivo == 0:
        print(camino)
        return
    for numero in range(inicio, maximo + 1):
        if numero > objetivo:
            continue
        camino.append(numero)  # agregar número al camino actual
        retroceso(maximo, objetivo - numero, numero + 1, camino)  # explorar siguiente paso
        camino.pop()  # deshacer elección (retroceder)

# Ejemplo: combinaciones de 1 a 5 que sumen 5
retroceso(5, 5)

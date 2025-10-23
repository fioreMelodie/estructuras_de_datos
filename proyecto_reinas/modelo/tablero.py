# modelo/tablero.py
# Contiene la lógica del tablero y el algoritmo para resolver las 8 reinas.


class Tablero:
    def __init__(self, tamaño=8):
        self.tamaño = tamaño
        self.soluciones = []

    def es_seguro(self, tablero, fila, columna):
        """
        Verifica si se puede colocar una reina en (fila, columna)
        sin que sea atacada por otra.
        """
        for i in range(fila):
            # Si hay una reina en la misma columna
            if tablero[i] == columna:
                return False
            # Si hay una reina en diagonal
            if abs(tablero[i] - columna) == abs(i - fila):
                return False
        return True

    def resolver(self, fila, tablero_actual, fila_inicial, col_inicial):
        """
        Algoritmo recursivo (backtracking) para colocar reinas fila por fila.
        """
        # Caso base: si ya colocó 8 reinas, guardar solución
        if fila == self.tamaño:
            # Validar que la posición inicial esté incluida
            if tablero_actual[fila_inicial] == col_inicial:
                self.soluciones.append(tablero_actual.copy())
            return

        for col in range(self.tamaño):
            if self.es_seguro(tablero_actual, fila, col):
                tablero_actual[fila] = col
                self.resolver(fila + 1, tablero_actual, fila_inicial, col_inicial)
                tablero_actual[fila] = -1  # retrocede (backtrack)

    def encontrar_soluciones(self, fila_inicial, col_inicial):
        """
        Limpia las soluciones y busca todas las posibles combinaciones
        donde la reina inicial esté en (fila_inicial, col_inicial).
        """
        self.soluciones = []
        tablero = [-1] * self.tamaño

        # Colocamos la reina inicial en su posición
        tablero[fila_inicial] = col_inicial

        # Empezamos desde la fila 0 (se resolverá todo)
        self.resolver(0, tablero, fila_inicial, col_inicial)

        return self.soluciones

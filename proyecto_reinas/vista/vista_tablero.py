# vista/vista_consola.py
# Muestra el tablero y las soluciones en consola.

class VistaTablero:
    def pedir_posicion(self):
        print("=== PROBLEMA DE LAS 8 REINAS ===")
        fila = int(input("Ingrese la fila de la primera reina (0-7): "))
        columna = int(input("Ingrese la columna de la primera reina (0-7): "))
        return fila, columna

    def mostrar_resultado(self, soluciones, fila_inicial, col_inicial):
        total = len(soluciones)
        print(f"\nSe encontraron {total} soluciones posibles para la posición inicial ({fila_inicial}, {col_inicial}):\n")

        for i, solucion in enumerate(soluciones, start=1):
            print(f"Solución {i}: {solucion}")
            self.mostrar_tablero(solucion)
            print("-" * 35)

    def mostrar_tablero(self, solucion):
        for fila in range(8):
            fila_str = ""
            for col in range(8):
                if solucion[fila] == col:
                    fila_str += " ♟ "
                else:
                    fila_str += " · "
            print(fila_str)
        print()

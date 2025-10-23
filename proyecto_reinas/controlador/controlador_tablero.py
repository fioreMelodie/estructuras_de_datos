# controlador/controlador.py
# Controla la interacción entre el modelo (lógica) y la vista (interfaz).

from modelo.tablero import Tablero
from vista.vista_tablero import VistaTablero

class Controlador:
    def __init__(self):
        self.tablero = Tablero()
        self.vista = VistaTablero()

    def ejecutar(self):
        # Pedimos la posición inicial
        fila, columna = self.vista.pedir_posicion()

        # Obtenemos las soluciones desde el modelo
        soluciones = self.tablero.encontrar_soluciones(fila, columna)

        # Mostramos el resultado por pantalla
        self.vista.mostrar_resultado(soluciones, fila, columna)

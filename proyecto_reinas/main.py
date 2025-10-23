# main.py
# Punto de entrada del programa

from controlador.controlador_tablero import Controlador

if __name__ == "__main__":
    app = Controlador()
    app.ejecutar()

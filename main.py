# main.py
from controller import ControladorProducto

if __name__ == "__main__":
    ctrl = ControladorProducto()
    ctrl.agregar_producto("Pan", 1500)
    ctrl.agregar_producto("Leche", 3200)

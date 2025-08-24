# controller.py
from model import Producto
from view import VistaProducto

class ControladorProducto:
    def __init__(self):
        self.vista = VistaProducto()

    def agregar_producto(self, nombre, precio):
        producto = Producto(nombre, precio)
        self.vista.mostrar_producto(producto)

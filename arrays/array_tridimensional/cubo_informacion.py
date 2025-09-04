# 📊 Ejemplo de Cubo de Información en Python

# ======================
# 1. Definir los datos
# ======================
# Usamos un diccionario anidado para representar el cubo
cubo = {
    "Enero": {
        "A": {"Norte": 120, "Sur": 0, "Centro": 0},
        "B": {"Norte": 200, "Sur": 0, "Centro": 0},
        "C": {"Norte": 150, "Sur": 0, "Centro": 0},
    },
    "Febrero": {
        "A": {"Norte": 0, "Sur": 180, "Centro": 0},
        "B": {"Norte": 0, "Sur": 220, "Centro": 0},
        "C": {"Norte": 0, "Sur": 90, "Centro": 0},
    },
    "Marzo": {
        "A": {"Norte": 0, "Sur": 0, "Centro": 160},
        "B": {"Norte": 0, "Sur": 0, "Centro": 210},
        "C": {"Norte": 0, "Sur": 0, "Centro": 130},
    }
}

# ======================
# 2. Imprimir el cubo completo
# ======================
print("=== Cubo de información ===")
for mes, productos in cubo.items():
    print(f"\n{mes}:")
    for producto, regiones in productos.items():
        print(f"  Producto {producto}: {regiones}")

# ======================
# 3. Consultas sobre el cubo
# ======================

# Ventas del producto A en Febrero, región Sur
ventas_febrero_A_sur = cubo["Febrero"]["A"]["Sur"]
print(f"\nVentas de producto A en Febrero (región Sur): {ventas_febrero_A_sur}")

# Ventas totales en Marzo (sumando productos y regiones)
ventas_marzo = sum(
    sum(regiones.values()) for regiones in cubo["Marzo"].values()
)
print(f"Ventas totales en Marzo: {ventas_marzo}")

# Ventas totales del producto B en todo el trimestre
ventas_producto_B = sum(
    sum(cubo[mes]["B"].values()) for mes in cubo
)
print(f"Ventas totales de producto B en el trimestre: {ventas_producto_B}")

/*
=== Cubo de información ===

Enero:
  Producto A: {'Norte': 120, 'Sur': 0, 'Centro': 0}
  Producto B: {'Norte': 200, 'Sur': 0, 'Centro': 0}
  Producto C: {'Norte': 150, 'Sur': 0, 'Centro': 0}

Febrero:
  Producto A: {'Norte': 0, 'Sur': 180, 'Centro': 0}
  Producto B: {'Norte': 0, 'Sur': 220, 'Centro': 0}
  Producto C: {'Norte': 0, 'Sur': 90, 'Centro': 0}

Marzo:
  Producto A: {'Norte': 0, 'Sur': 0, 'Centro': 160}
  Producto B: {'Norte': 0, 'Sur': 0, 'Centro': 210}
  Producto C: {'Norte': 0, 'Sur': 0, 'Centro': 130}

Ventas de producto A en Febrero (región Sur): 180
Ventas totales en Marzo: 500
Ventas totales de producto B en el trimestre: 630
*/

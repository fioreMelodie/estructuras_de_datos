# VISTA
def mostrar_menu():
    print("\n=== MENÚ DE PROBLEMAS ===")
    print("1. Patos y Conejos")
    print("2. Digit-Increasing")
    print("3. Digit-Palindromic")
    print("4. Serie de Padovan")
    print("5. Serie mSenh")
    print("0. Salir")
    return int(input("Elija una opción: "))


# Ejercicio 1
def mostrar_patos_conejos(patos, conejos):
    if patos is not None:
        print(f" Número de patos: {patos}")
        print(f" Número de conejos: {conejos}")
    else:
        print("No se encontró solución.")

# Ejercicio 2
def pedir_numero():
    return int(input("Ingrese un número: "))

def mostrar_resultado_digitIncreasing(numero, resultado):
    if resultado == 1:
        print(f" El número {numero} es digit-increasing")
    else:
        print(f" El número {numero} NO es digit-increasing")

# Ejercicio 3
def mostrar_resultado_palindromic(numero, resultado):
    if resultado == 1:
        print(f" El número {numero} es digit-palindromic")
    else:
        print(f" El número {numero} NO es digit-palindromic")

# Ejercicio 4 y 5
def mostrar_resultado_serie(nombre, n, resultado):
    print(f"El término {n} de la serie {nombre} es: {resultado}")

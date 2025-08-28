# CONTROLADOR
import modelo
import vista

def ejecutar():
    while True:
        opcion = vista.mostrar_menu()

        if opcion == 1:
            patos, conejos = modelo.resolver_patos_conejos(35, 94)
            vista.mostrar_patos_conejos(patos, conejos)

        elif opcion == 2:
            numero = vista.pedir_numero()
            resultado = modelo.isDigitIncreasing(numero)
            vista.mostrar_resultado_digitIncreasing(numero, resultado)

        elif opcion == 3:
            numero = vista.pedir_numero()
            resultado = modelo.isDigitPalindromic(numero)
            vista.mostrar_resultado_palindromic(numero, resultado)

        elif opcion == 4:
            n = vista.pedir_numero()
            resultado = modelo.padovan(n)
            vista.mostrar_resultado_serie("Padovan", n, resultado)

        elif opcion == 5:
            n = vista.pedir_numero()
            resultado = modelo.mSenh(n)
            vista.mostrar_resultado_serie("mSenh", n, resultado)

        elif opcion == 0:
            print("Saliendo del programa")
            break

        else:
            print("Opción no válida.")

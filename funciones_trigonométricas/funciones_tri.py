# En este programa voy a calcular seno, coseno y tangente sin usar librerías.
# Para hacerlo me baso en las series de Taylor, que permiten aproximar funciones
# con sumas y potencias.
#
# Seno: sen(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
# Coseno: cos(x) = 1 - x^2/2! + x^4/4! - x^6/6! + ...
# Tangente: tan(x) = sen(x) / cos(x)
#
# Con esto se pueden aproximar valores de las funciones trigonométricas usando ciclos y factoriales.

def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

def seno(x, terminos=10):
    resultado = 0
    for n in range(terminos):
        signo = (-1) ** n
        numerador = x ** (2*n + 1)
        denominador = factorial(2*n + 1)
        resultado += signo * (numerador / denominador)
    return resultado

def coseno(x, terminos=10):
    resultado = 0
    for n in range(terminos):
        signo = (-1) ** n
        numerador = x ** (2*n)
        denominador = factorial(2*n)
        resultado += signo * (numerador / denominador)
    return resultado

def tangente(x, terminos=10):
    return seno(x, terminos) / coseno(x, terminos)


# Ejemplo de uso con un ángulo en radianes
angulo = 1.5708   # aprox pi/2 radianes

print("Seno:", seno(angulo))
print("Coseno:", coseno(angulo))
print("Tangente:", tangente(angulo))

# MODELO
# --- Ejercicio 1: Patos y Conejos
def resolver_patos_conejos(cabezas: int, patas: int):
    for patos in range(cabezas + 1):
        conejos = cabezas - patos
        if 2 * patos + 4 * conejos == patas:
            return patos, conejos
    return None, None


# --- Ejercicio 2: Digit-Increasing
def isDigitIncreasing(numero: int) -> int:
    for n in range(1, 10):
        suma = 0
        termino = 0
        while suma < numero:
            termino = termino * 10 + n
            suma += termino
            if suma == numero:
                return 1
    return 0


# --- Ejercicio 3: Digit-Palindromic
def isDigitPalindromic(numero: int) -> int:
    texto = str(numero)
    if texto == texto[::-1]:
        return 1
    else:
        return 0


# --- Ejercicio 4: Padovan
def padovan(n: int) -> int:
    if n == 0 or n == 1 or n == 2:
        return 1
    return padovan(n - 2) + padovan(n - 3)


# --- Ejercicio 5: mSenh
def mSenh(n: int) -> int:
    if n == 0 or n == 1 or n == 2:
        return 1
    else:
        termino1 = mSenh(n - 2)
        termino2 = mSenh(n - 3)
        return termino1 + termino2

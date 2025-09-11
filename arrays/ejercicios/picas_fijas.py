import random

# Generar el número secreto de 4 cifras diferentes
def generar_numero():
    digitos = list("0123456789")
    random.shuffle(digitos)  # revuelvo los números
    return "".join(digitos[:4])  # tomo los 4 primeros

# Revisar cuantas fijas y cuantas picas tiene el intento
def fijas_picas(secreto, intento):
    fijas = 0
    picas = 0
    for i in range(4):
        if intento[i] == secreto[i]:
            fijas += 1   # número en la posición correcta
        elif intento[i] in secreto:
            picas += 1   # número correcto pero en otra posición
    return fijas, picas

# Juego principal
def jugar():
    secreto = generar_numero()
    print("Juego de Fijas y Picas")
    print("Debes adivinar un número de 4 cifras distintas.")

    while True:
        intento = input("Ingresa tu número: ")

        # validar que sea correcto (4 digitos, sin repetir)
        if len(intento) != 4 or not intento.isdigit() or len(set(intento)) != 4:
            print("Número inválido, intenta otra vez.")
            continue

        fijas, picas = fijas_picas(secreto, intento)
        print("Fijas:", fijas, "Picas:", picas)

        if fijas == 4:
            print("¡Ganaste! El número era", secreto)
            break

# ejecutar
jugar()

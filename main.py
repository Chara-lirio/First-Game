import random

def jugar():
    print("¡Bienvenido al juego de adivinar el número!")
    numero_secreto = random.randint(1, 100)
    intentos = 0

    while True:
        try:
            adivinanza = int(input("Adivina un número entre 1 y 100: "))
            intentos += 1
            if adivinanza < numero_secreto:
                print("Demasiado bajo.")
            elif adivinanza > numero_secreto:
                print("Demasiado alto.")
            else:
                print(f"¡Correcto! Adivinaste el número en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")

if __name__ == "__main__":
    jugar()

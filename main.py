import random

def jugar():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("\nHe pensado un número entre 1 y 100. ¿Puedes adivinar cuál es?")

    while True:
        try:
            adivinanza = int(input("Tu intento: "))
            intentos += 1
            if adivinanza < numero_secreto:
                print("Demasiado bajo.")
            elif adivinanza > numero_secreto:
                print("Demasiado alto.")
            else:
                print(f"🎉 ¡Correcto! Adivinaste el número en {intentos} intentos.")
                break
        except ValueError:
            print("⚠️ Por favor, introduce un número válido.")

def mostrar_menu():
    while True:
        print("\n====== MENÚ PRINCIPAL ======")
        print("1. Jugar")
        print("2. Salir")
        opcion = input("Selecciona una opción (1 o 2): ")

        if opcion == "1":
            jugar()
        elif opcion == "2":
            print("¡Gracias por jugar! 👋")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()

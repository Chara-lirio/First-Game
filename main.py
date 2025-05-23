import random

# Variables de estadísticas globales
partidas_jugadas = 0
intentos_totales = 0
mejor_puntaje = None

def jugar(dificultad):
    global partidas_jugadas, intentos_totales, mejor_puntaje

    if dificultad == "1":
        limite = 10
    elif dificultad == "2":
        limite = 100
    elif dificultad == "3":
        limite = 1000
    else:
        print("Dificultad inválida. Usando dificultad media (1-100).")
        limite = 100

    numero_secreto = random.randint(1, limite)
    intentos = 0
    print(f"\nAdivina el número entre 1 y {limite}.")

    while True:
        try:
            adivinanza = int(input("Tu intento: "))
            intentos += 1
            if adivinanza < numero_secreto:
                print("Demasiado bajo.")
            elif adivinanza > numero_secreto:
                print("Demasiado alto.")
            else:
                print(f"🎉 ¡Correcto! Adivinaste en {intentos} intentos.")
                break
        except ValueError:
            print("⚠️ Ingresa un número válido.")

    # Actualizar estadísticas
    partidas_jugadas += 1
    intentos_totales += intentos

    if mejor_puntaje is None or intentos < mejor_puntaje:
        mejor_puntaje = intentos
        print("🏆 ¡Nuevo mejor puntaje!")

    mostrar_estadisticas()

def mostrar_estadisticas():
    print("\n📊 ESTADÍSTICAS:")
    print(f"Partidas jugadas: {partidas_jugadas}")
    print(f"Intentos totales: {intentos_totales}")
    print(f"Mejor puntaje (menos intentos): {mejor_puntaje}")

def elegir_dificultad():
    print("\nSelecciona dificultad:")
    print("1. Fácil (1-10)")
    print("2. Medio (1-100)")
    print("3. Difícil (1-1000)")
    return input("Tu elección: ")

def mostrar_menu():
    while True:
        print("\n====== MENÚ PRINCIPAL ======")
        print("1. Jugar")
        print("2. Salir")
        opcion = input("Selecciona una opción (1 o 2): ")

        if opcion == "1":
            dificultad = elegir_dificultad()
            jugar(dificultad)
        elif opcion == "2":
            print("¡Gracias por jugar! 👋")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()

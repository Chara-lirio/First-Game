import random
import json
import os

# Archivo donde se guardarán las estadísticas
ARCHIVO_ESTADISTICAS = "estadisticas.json"

# Estadísticas (se cargarán desde el archivo al iniciar)
estadisticas = {
    "partidas_jugadas": 0,
    "intentos_totales": 0,
    "mejor_puntaje": None
}

def cargar_estadisticas():
    if os.path.exists(ARCHIVO_ESTADISTICAS):
        with open(ARCHIVO_ESTADISTICAS, "r") as f:
            try:
                datos = json.load(f)
                estadisticas.update(datos)
            except json.JSONDecodeError:
                print("⚠️ Archivo de estadísticas dañado. Se reiniciarán.")
    else:
        guardar_estadisticas()

def guardar_estadisticas():
    with open(ARCHIVO_ESTADISTICAS, "w") as f:
        json.dump(estadisticas, f, indent=4)

def mostrar_estadisticas():
    print("\n📊 ESTADÍSTICAS:")
    print(f"Partidas jugadas: {estadisticas['partidas_jugadas']}")
    print(f"Intentos totales: {estadisticas['intentos_totales']}")
    print(f"Mejor puntaje: {estadisticas['mejor_puntaje']}")

def jugar(dificultad):
    if dificultad == "1":
        limite = 10
    elif dificultad == "2":
        limite = 100
    elif dificultad == "3":
        limite = 1000
    else:
        print("Dificultad inválida. Se usará nivel medio (1-100).")
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
    estadisticas["partidas_jugadas"] += 1
    estadisticas["intentos_totales"] += intentos

    if (
        estadisticas["mejor_puntaje"] is None
        or intentos < estadisticas["mejor_puntaje"]
    ):
        estadisticas["mejor_puntaje"] = intentos
        print("🏆 ¡Nuevo mejor puntaje!")

    guardar_estadisticas()
    mostrar_estadisticas()

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
        print("2. Ver estadísticas")
        print("3. Salir")
        opcion = input("Selecciona una opción (1, 2 o 3): ")

        if opcion == "1":
            dificultad = elegir_dificultad()
            jugar(dificultad)
        elif opcion == "2":
            mostrar_estadisticas()
        elif opcion == "3":
            print("¡Gracias por jugar! 👋")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    cargar_estadisticas()
    mostrar_menu()

import random
import json
import os

ARCHIVO_ESTADISTICAS = "estadisticas.json"

estadisticas = {
    "partidas_jugadas": 0,
    "intentos_totales": 0,
    "mejor_puntaje": {
        "facil": None,
        "medio": None,
        "dificil": None
    }
}

def dificultad_a_texto(nivel):
    return {
        "1": "facil",
        "2": "medio",
        "3": "dificil"
    }.get(nivel, "medio")

def cargar_estadisticas():
    if os.path.exists(ARCHIVO_ESTADISTICAS):
        with open(ARCHIVO_ESTADISTICAS, "r") as f:
            try:
                datos = json.load(f)

                # Manejar archivo antiguo donde mejor_puntaje es un int
                if isinstance(datos.get("mejor_puntaje"), int):
                    mejor = datos["mejor_puntaje"]
                    datos["mejor_puntaje"] = {
                        "facil": None,
                        "medio": mejor,
                        "dificil": None
                    }

                estadisticas.update(datos)

                # Asegurar que tiene las tres claves
                for clave in ["facil", "medio", "dificil"]:
                    if clave not in estadisticas["mejor_puntaje"]:
                        estadisticas["mejor_puntaje"][clave] = None

            except json.JSONDecodeError:
                print("⚠️ Archivo dañado. Se reiniciarán estadísticas.")
    else:
        guardar_estadisticas()


def guardar_estadisticas():
    with open(ARCHIVO_ESTADISTICAS, "w") as f:
        json.dump(estadisticas, f, indent=4)

def mostrar_estadisticas():
    print("\n📊 ESTADÍSTICAS:")
    print(f"Partidas jugadas: {estadisticas['partidas_jugadas']}")
    print(f"Intentos totales: {estadisticas['intentos_totales']}")
    print("🏆 Mejor puntaje por dificultad:")
    for nivel, puntaje in estadisticas["mejor_puntaje"].items():
        print(f"  - {nivel.capitalize()}: {puntaje if puntaje is not None else 'Ninguno'}")

def jugar(dificultad):
    nombre_dificultad = dificultad_a_texto(dificultad)

    if dificultad == "1":
        limite = 10
    elif dificultad == "2":
        limite = 100
    elif dificultad == "3":
        limite = 1000
    else:
        print("Dificultad inválida. Se usará medio (1-100).")
        limite = 100

    numero_secreto = random.randint(1, limite)
    intentos = 0
    print(f"\n🎮 Adivina el número entre 1 y {limite}.")

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

    estadisticas["partidas_jugadas"] += 1
    estadisticas["intentos_totales"] += intentos

    puntaje_actual = estadisticas["mejor_puntaje"][nombre_dificultad]
    if puntaje_actual is None or intentos < puntaje_actual:
        estadisticas["mejor_puntaje"][nombre_dificultad] = intentos
        print("🏆 ¡Nuevo mejor puntaje para dificultad", nombre_dificultad.capitalize() + "!")

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

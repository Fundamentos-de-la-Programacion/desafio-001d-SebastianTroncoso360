# ============================================================
# DESAFIO EN CLASES - Juego de Trivia por rondas con ranking
# FPY1101 - Fundamentos de Programacion
# ============================================================

# INVESTIGA (1): modulo random
import random

# Banco de preguntas precargado
banco_preguntas = [
    {"pregunta": "Cual es la capital de Chile?", "respuesta": "Santiago"},
    {"pregunta": "Cuanto es 7 por 8?", "respuesta": "56"},
    {"pregunta": "Que palabra clave define una funcion en Python?", "respuesta": "def"},
    {"pregunta": "Cual es el simbolo del resto (modulo) en Python?", "respuesta": "%"},
    {"pregunta": "Que tipo de dato es 3.14?", "respuesta": "float"},
    {"pregunta": "Cuantos colores tiene el arcoiris?", "respuesta": "7"},
    {"pregunta": "Que funcion muestra texto en pantalla en Python?", "respuesta": "print"},
    {"pregunta": "Cual es el oceano que limita con Chile?", "respuesta": "Pacifico"},
]


def mostrar_pregunta(pregunta):
    # Recibe un diccionario con clave 'pregunta' y la muestra al usuario.
    print(pregunta["pregunta"])


def normalizar(texto):
    # Retorna el texto en minusculas y sin espacios al inicio/fin.
    return texto.strip().lower()


def es_correcta(respuesta_usuario, respuesta_correcta):
    # Compara respuestas normalizadas.
    return normalizar(respuesta_usuario) == normalizar(respuesta_correcta)


def jugar_ronda(jugador, banco, n):
    # Elegir n preguntas al azar sin repetir
    preguntas = random.sample(banco, n)

    puntaje = 0

    for pregunta in preguntas:
        mostrar_pregunta(pregunta)
        respuesta = input("Respuesta: ")

        if es_correcta(respuesta, pregunta["respuesta"]):
            print("Correcto!")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta era: {pregunta['respuesta']}")

    return puntaje


def mostrar_ranking(jugadores):
    # Ordenar por puntaje de mayor a menor
    ordenados = sorted(jugadores, key=lambda j: j["puntaje"], reverse=True)

    print("\n=== RANKING FINAL ===")

    posicion = 1
    for jugador in ordenados:
        preguntas = jugador["preguntas"]

        if preguntas > 0:
            porcentaje = (jugador["puntaje"] / preguntas) * 100
        else:
            porcentaje = 0

        print(
            f"{posicion}. {jugador['nombre']} - "
            f"Puntaje: {jugador['puntaje']} - "
            f"Acierto: {porcentaje:.2f}%"
        )

        posicion += 1


def main():
    print("=== JUEGO DE TRIVIA POR RONDAS ===")
    preguntas_por_ronda = 5

    # Lectura protegida con try/except
    try:
        cantidad_jugadores = int(input("Cuantos jugadores van a jugar? "))
    except ValueError:
        print("Entrada invalida. Se asume 1 jugador.")
        cantidad_jugadores = 1

    jugadores = []
    numero = 1

    while numero <= cantidad_jugadores:
        nombre = input(f"\nNombre del jugador {numero}: ")

        puntaje = jugar_ronda(nombre, banco_preguntas, preguntas_por_ronda)

        jugadores.append({
            "nombre": nombre,
            "puntaje": puntaje,
            "preguntas": preguntas_por_ronda
        })

        numero = numero + 1

    mostrar_ranking(jugadores)
    print("\nGracias por jugar!")


main()

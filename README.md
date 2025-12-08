# Autonomo_2
*Progreso de la codificación del juego piedra, papel tijeras

Este deber autónomo consistió en realizar el diagrama de flujo del juego piedra papel tijera y posteriormente intentar replicar la idea de dicho diagrama en el lenguaje de programación Phyton (codificarlo).
Actualmente, el programa funciona de manera básica; sin embargo, aún existen algunos detalles por corregir o integrar, los cuales se irán corrigiendo conforme pase el tiempo, cuando adquiera más conocimiento de programación y se sigan las instrucciones dadas por la profesora.

*Estructura del repositorio

El repositorio esta organizado por el momento de la siguiente manera:

-El archivo py, donde se encuentra el código del juego esta en la carpeta piedra, papel tijera.

-El diagrama de flujo está en la carpeta de fiagrama de flujo.

*Programa utilizado: Spyder


Lenguaje de programación: Phyton


Versión de Phyton: 3.12.11

*Librería utilizada

Libreria random se usa para generar la eleccion aleatoria de la pc duarante el juego con import random es una libreria integrada en Python.

*Código del juego
A continuación se muestra el código parte por parte del juego y haré una breve explicación:

import random

-Es una libreria interna de Python que sirve para generar cosas al azar.

print("Iniciando juego.....")


print("Bienvenid@ al juego piedra,papel y tijera")


print("Las reglas del juego son: ")


print("-Piedra gana a tijera\n-Tijera gana a papel.\n-Papel gana a piedra.\n-Si ambos sacan la misma opcion será empate.\n")

-En esta parte del código se utilize la función print(), la cual me sirve para imprimir los textos en la pantalla osea me va a mostrar el mensaje de bienvenida y las reglas del juego.

opciones=["piedra","papel","tijera"]

-Esta es una variable de tipo lista que contiene las opciones válidas del juego.

De esta lista el jugador elige su jugada y la computadora tambien elige una opcón, pero de manera aleatoria

while True:

-Aquí utilizo el while true para que el juego se repita varias en el momento que ponga si quiere volver a jugar,  y sino break para detener el bucle y finalizar el juego.

while jugador not in opciones:

-Este ciclo se asegura de que el jugador solo ingrese opciones validas.

Si el jugador escribe una opción que este fuera de la lista de opciones, el programa muestra el el mensaje de que vuelvas a esvcribir y vuelve a pedir la opcion correcta.

pc=random.choice(opciones)

-Aquí es donde la computadora da uso al import random y selecciona de manera aleatoria desde la lista de opciones usando la función choice.

print("El jugador escogió: ", jugador)
print("La pc escogió: " , pc)

En esta parte del código se utiliza la función print(= para mostrar en la pantalla la opción elegida por el jugador y la opción seleccionada por la computadora.

    if jugador == "piedra" and pc == "tijera":
        print("Ganaste! :D")
    elif jugador =="tijera" and pc =="papel":
        print("Ganaste! :D")
    elif jugador == "papel" and pc == "piedra":
        print("Ganaste! :D")
    elif jugador == pc:
        print("Empataste!")
    else:
        print("Perdiste! :c")
-Se usa las estructuras condicionales para comparar las opciones del jugador con la pc y determinar si el jugador gana o empata. En este caso se puede observar  que todas las condicionales el jugador gana y si no gana empata, y si pierde, pierde ya por los descartes .

    new_partida=input("Quieres volver a jugar? Si(Y)/No(N): ").upper().strip()
    if new_partida == "N" or (new_partida != "Y" and new_partida != "N"):
        print("Partida finalizada.")
        break
    else:
        print("[+++++++++++++++++++++++]")
        print("Cargando nuevamente...")
        print("[+++++++++++++++++++++++]")
-En esta parte del codigo se pregunta al jugador si desea volver a jugar o finalizar la partida. La respuesta se valida y según lo que ingrese el jugador, el juego se reinicia o se termina.





















import random


print("Iniciando juego.....")
print("Bienvenid@ al juego piedra,papel y tijera")
print("Las reglas del juego son: ")
print("-Piedra gana a tijera\n-Tijera gana a papel.\n-Papel gana a piedra.\n-Si ambos sacan la misma opcion será empate.\n")


opciones=["piedra","papel","tijera"]
while True:
    jugador=None
    while jugador not in opciones:
        jugador=input("Escoge una de las tres opciones válidas piedra, papel, tijera: ").lower().strip()
        if jugador not in opciones:
            print("Opción no válida.Intente nuevamente")


    pc=random.choice(opciones)
    print("El jugador escogió: ", jugador)
    print("La pc escogió: " , pc)

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
        
    new_partida=input("Quieres volver a jugar? Si(Y)/No(N): ").upper().strip()
    if new_partida == "N" or (new_partida != "Y" and new_partida != "N"):
        print("Partida finalizada.")
        break
    else:
        print("[+++++++++++++++++++++++]")
        print("Cargando nuevamente...")
        print("[+++++++++++++++++++++++]")
        
        
    

# Inicializan las variables generales
juego_iniciado= True
opciones = ["piedra","papel","tijera"]
contador= 0
numero_rondas=0

# Mostrar reglas del juego
def mostrarReglas():
    print("\n----- REGLAS DEL JUEGO -----")
    print("- Piedra gana a tijera.\n- Tijera gana a papel.\n- Papel gana a piedra.\n- Si ambos sacan la misma opción será empate.\n")
    print("------------------------------")
    
# Seleccion aleatoria de la máquina
def eleccion_pc():
    global contador
    contador += 1
    valor_aleatorio = contador * 7
    indice= valor_aleatorio % 3
    return opciones[indice]

def parametrizar_rondas():
    global numero_rondas
    while True:
        try:
            entrada=int(input("\nIngresa el número de rondas a jugar (entre 3 y 10): ").strip())
            if entrada >= 3 and entrada <= 10:
                numero_rondas=entrada
                return
            else:
                print("\nIngresa un número entre 3 y 10: ")
        except:
            print("\nIngresar un número entero válido.")

#Retorna la respuesta del jugador valida
def eleccion_jugador():
    while True:
        respuesta_jugador = input("\nEscribe una de las tres opciones piedra, papel, tijera: ").lower().strip()
        if respuesta_jugador in opciones:
            return respuesta_jugador
        else:
            print("\nOpción no válida. Intente nuevamente")

def determinar_ganador (jugador, pc):
    print("\nPuntuación del jugador: ", jugador)
    print("Puntuación de la pc: ", pc)
    print("[+++++++Resutado+++++++++]")    
    if jugador > pc:
        print("Ganaste! :D")
    elif pc > jugador:
        print("Perdiste! :c")
    else:
        print("Empate!")
    print("[+++++++++++++++++++++++]\n")
                   
# Inicialización del juego    
def iniciarJuego():
    global numero_rondas
    puntos_jugador= 0
    puntos_pc= 0
    jugando = True 
    parametrizar_rondas()
    while jugando:
        if numero_rondas == 0:
            print("\nPartida finalizada.")
            determinar_ganador(puntos_jugador, puntos_pc)
            nuevaPartida=input("Quieres volver a jugar? Si(Y)/No(N): ").upper().strip()
            if nuevaPartida == "N" or (nuevaPartida != "Y" and nuevaPartida != "N"):
                jugando= False
                print("Juego terminado!") 
            else:
                puntos_jugador= 0
                puntos_pc=0
                parametrizar_rondas()
        else: 
            jugador = eleccion_jugador()
            pc = eleccion_pc()
            print("El jugador escogió: ", jugador)
            print("La pc escogió: ", pc)
            numero_rondas -= 1
            if jugador == "piedra" and pc == "tijera":
                puntos_jugador +=1
                print("Gana jugador!")
            elif jugador =="tijera" and pc =="papel":
                puntos_jugador +=1
                print("Gana jugador!")
            elif jugador == "papel" and pc == "piedra":
                puntos_jugador +=1
                print("Gana jugador!")
            elif jugador == pc:
                print("Empate!")
            else:
                puntos_pc +=1
                print("Gana pc!")
                          
# Selección de acción del juego
def seleccionMenu(valor):
    #Usar "global" para poder modificar la variable general
    global juego_iniciado
    if valor == "1":
        mostrarReglas()
    elif valor == "2":
        iniciarJuego()
    elif valor == "3":
        print("Saliendo del juego...")
        juego_iniciado= False
    else:
        print("Opción no válida. Intenta nuevamente.\n")
    
print("Iniciando juego.....")
print("Bienvenid@ al juego piedra,papel y tijera\n")

while juego_iniciado:
    print("[+++++++++++++++++++++++]")
    print("         MENÚ    ")
    print("1. Ver reglas")
    print("2. Jugar")
    print("3. Salir")
    print("[+++++++++++++++++++++++]\n")
    opcion = input("Elige una opción: ")
    seleccionMenu(opcion)
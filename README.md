# Evaluación contacto con el docente

### Juego totalmente funcional

Esta es una evaluación donde se intenta integrar todo lo visto de las 4 unidades al proyecto Juego Piedra, Papel o Tijera. Este programa es funcional; el juego Piedra, Papel o Tijera viene de un proceso de aprendizaje tanto de los conocimientos aprendidos en clase como de los conocimientos autónomos. Se hicieron diagramas de funcionalidad, arquitectura y diagaramas de flujo para poder llegar a es resultado. Estos diagramas fueron la base, junto los conocimientos de clase para realizar el código de mi juego.

## Tecnologias
* Programa utilizado: Spyder
* Lenguaje de programación: Phyton
* Versión de Phyton: 3.12.11
* Librerias (Ninguna): Indico que ya no se podía hacer uso de las librerias y que, si queriamos usarlas, debíamos crealas nosotros mismos o por medio de las funciones. Yo opte por las funciones.

## Diagrama de flujo

![Diagrama Flujo](https://github.com/DonnyMR12/Autonomo_2/blob/main/Diagrama%20de%20flujo.webp?raw=true)

## Estructura del programa

* Uso de **Variables generales**

<img alt="1" src="https://github.com/DonnyMR12/Autonomo_2/blob/main/img1.png?raw=true" />

```
juego_iniciado=True
```
* Es una variable booleana que utilizo para controlar el menú principal del juego mientras su valor sea True, el menú se seguira mostrando.
```
opciones = ["piedra","papel","tijera"]
```
* Es una variable tipo lista que contiene las opciones válidas del juego: piedra, papel y tijera.

- Esta lista se utiliza tanto para validar la entrada del jugador como para la elección de la computadora.
```
contador=0
```
* Esta variable que se usa dentro de una función para simular la aletoariedad de la pc.
```
numero_rondas=0
```
* Aquí se almacenará la cantidad de rondas que el jugador ingrese por teclado.

* Mostrar reglas del juego

<img alt="2" src="https://github.com/DonnyMR12/Autonomo_2/blob/main/img2.png?raw=true" />

* Aquí la función muestra las reglas del juego en la consola mediante el uso del print

* Se uso /n para hacer un salto de línea

* Seleccion aleatoria de la máquina

<img alt="3" src="https://github.com/DonnyMR12/Autonomo_2/blob/main/img3.png?raw=true" />


* La función realiza una seleccion aleatoria entre (piedra, papel, tijera)

* Global contador: Se utiliza global en la variable contador para poder modficar el valor del mismo, ya que es una variable general.

* Contador +=1 :esta línea incrementa un uno cada vez que se ejecute la función, dado que contador siempre inicia con 0 cuando se inicia el programa.

* (valor_aleatorio= contador * 7 ) : Esta línea multiplica el contador * 7 para tener un número aleatorio, ya que el contador se incrementa en cada llamada de la función.

* (indice= valor_aleatorio % 3): El operador de residuo o modulo => Esto devuelve el residuo de dividir el número anterior *3

* El resultado de dividir cualquier número entero *3. los unicos residuos posibles son: 0, 1 o 2. el resultado se asignará a la variable indice.

(return opciones[indice]): Esta linea retorna el elemento en base al número de indice que se parametriza de la lista de opciones.


* Parametrizar rondas

<img src="https://github.com/DonnyMR12/Autonomo_2/blob/main/img4.png?raw=true" />

* Funcion que parametriza rondas: Se encarga de definir cuantas rondas se van a jugar antes de empezar la partida.

* (global numero_rondas): Se utiliza global en la variable contador para poder modificar el valor del mismo ya que es una variable general.

* except: Aquí se captura las excepciones lo cual permite mostrar en pantalla o finalizar el proceso, claro de ser el caso.

* En caso de ingresar un valor no entero en el número no entero mostrará un mensaje de error, ya que esta función solo permite el ingreso de números enteros.

* Si el número es menor a 3 o mayor a 10, el programa vuelve a pedir el dato.

* Si el número esta entre 3 y 10 guarda el valor y break rompe el ciclo.

* La elección del jugador

<img alt="5" src="https://github.com/DonnyMR12/Autonomo_2/blob/main/img5.png?raw=true" />

* Se sabe bien que el while true es un bucle, hasta que el jugador no ingrese la opción correcta se va seguir repitiendo.

* Si la respuesta, es decir la elección del jugador, está dentro de la lista de opciones, esta será retornada.

* Lower() y strip(): Pasa todo a minúsculas y el otro quita espacios.

* Determinar ganador:

<img alt="6" src="https://github.com/DonnyMR12/Autonomo_2/blob/main/img8.png?raw=true" />

* El programa mostrará al ganador que tenga más puntos; caso contrario, mostrará empate.

* La funcion requiere de dos parametros "jugador"; será el número de puntos del jugador.

* El parametro "pc"  será el número de puntos de la máquina.

* Entonces se hace la validación.

* Inicialización del juego

<img alt="7" src="https://github.com/DonnyMR12/Autonomo_2/blob/main/img6.png?raw=true" />

## Funcionamiento

* Los puntos de jugador y los puntos de pc iniciarn con 0 cada vez que se ejecute la función iniciar juego()

* Luego la variable jugando se inicia con verdadero para que el ciclo while este activo.

* Se llama la funcion (parametrizar_rondas()) para definir cuántas rondas se van a jugar.

* Se inicia el ciclo while, mismo que se detiene cuando la variable jugando sea falso.

* La siguiente línea valida si el (numero_rondas == 0), en caso que número de rondas sea = 0 mostrará un mensaje partida finalizada, caso contrario seguiá la siguiente ronda.

* Si número de rondas es = 0 => Se llama a la función determinar_ganador(puntos_jugador, puntos_pc), luego se hará una validación si se quiere continuar con el jugando caso contrario se pondra.

* Se finalizará el ciclo while con la variable jugando= false, si en caso de ingresar (Y) se reiniciará los puntos de los jugadores y se llamará a la funcion (parametrizar rondas()).

<img alt="9" src="https://github.com/DonnyMR12/Autonomo_2/blob/main/img.png?raw=true" />

* Menú

<img alt="9" src="https://github.com/DonnyMR12/Autonomo_2/blob/main/img7.png?raw=true" />

```
SeleccionMenu()
```

* Esta función se encarga de llamar a las demás funciones según la opción que se ponga en el input.

* El menú funciona mediante el ciclo while juego_inciando, el cual mantiene activo el programa.

* Se puede considerar que esta función es la capa principal que controla todas las funciones que se ejecutan a partir del input.

* Si el jugador digita 1: se llama a la función mostrarreglas()

* Si el jugador digita 2: se llama a la función iniciarjuego()

* Si el jugador digita 3: Se sale del juego, ya que el uso el global para cambiar el valor a la variable juego_iniciado a False.

* Al cambiar juego_iniciado a False, el ciclo del while se rompe y termina el juego.

* Y si no es ninguno de estos, me va mostrá que la opción no es válida y se volverá a empezar el ciclo de seleción.

# Tabla de Resultados Completa

| Jugador | PC      | Ganador   |
|---------|---------|-----------|
| Piedra  | Tijera  | Jugador   |
| Piedra  | Papel   | PC        |
| Piedra  | Piedra  | Empate    |
| Papel   | Piedra  | Jugador   |
| Papel   | Tijera  | PC        |
| Papel   | Papel   | Empate    |
| Tijera  | Papel   | Jugador   |
| Tijera  | Piedra  | PC        |
| Tijera  | Tijera  | Empate    |

















    
























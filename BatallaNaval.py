import random

def seleccionarDificultad():
    print("Selecciona una dificultad:")
    print("1. Fácil (Tablero 5x5, 2 barcos)")
    print("2. Medio (Tablero 7x7, 3 barcos)")
    print("3. Difícil (Tablero 10x10, 4 barcos)")
    while True:
        try:
            opcion = int(input("Elige 1, 2 o 3: "))
            if opcion == 1:
                return 5, 2
            elif opcion == 2:
                return 7, 3
            elif opcion == 3:
                return 10, 4
            else:
                print("Opción inválida. Intenta nuevamente.")
        except ValueError:
            print("Entrada no válida. Introduce un número.")

def crearTablero(tamano):
    return [[" ~ " for _ in range(tamano)]for _ in range(tamano)]

def mostrarTablero (tableroDisparosJugador, tableroDisparosOponente):
    print("Tu tablero de disparos: ")
    for fila in tableroDisparosJugador:
        print("".join(fila))

    print("Tablero de disparos del oponente: ")
    for fila in tableroDisparosOponente:
        print("".join(fila))

def colocarBarcos(tablero, barcos, jugador):
    for barco in barcos:
        colocado = False
        while not colocado:
            if jugador == "Jugador":
                print(f"Colocando {barco['nombre']} de tamaño {barco['tamaño']}")
                fila = int(input("Ingrese la fila: "))
                columna = int(input("Ingrese la columna: "))
                orientacion = input("Ingrese la orientación (h para horizontal, v para vertical): ").lower()
            else:
                fila = random.randint(0, len(tablero) - 1)
                columna = random.randint(0, len(tablero) - 1)
                orientacion = random.choice(['h', 'v'])
            if validarColocacion(tablero, fila, columna, barco['tamaño'], orientacion):
                colocarBarco(tablero, fila, columna, barco['tamaño'], orientacion)
                colocado = True
            elif jugador == "Jugador":
                print("Colocación inválida. Inténtelo de nuevo.")

def validarColocacion(tablero, fila, columna, tamaño, orientacion):
    if orientacion == 'h':
        if columna + tamaño > len(tablero):
            return False
        for i in range(tamaño):
            if tablero[fila][columna + i] != " ~ ":
                return False
    else:
        if fila + tamaño > len(tablero):
            return False
        for i in range(tamaño):
            if tablero[fila + i][columna] != " ~ ":
                return False
    return True

def colocarBarco(tablero, fila, columna, tamaño, orientacion):
    if orientacion == 'h':
        for i in range(tamaño):
            tablero[fila][columna + i] = "B"
    else:
        for i in range(tamaño):
            tablero[fila + i][columna] = "B"

def realizarDisparo(tableroOculto,tableroDisparos,fila,columna):
    if tableroOculto[fila][columna]==" B ":
        tableroDisparos[fila][columna]=" x "
        tableroOculto[fila][columna]=" H "
        return "Buen disparo"   
    elif tableroOculto[fila][columna]==" ~ ":
        tableroDisparos[fila][columna]= " O "
        return "Agua"
    return "Ya disparaste aquí"

def verificarVictoria(tableroOculto):
    for fila in tableroOculto:
        if "B" in fila:  
            return False
    return True     

def jugarContracomputador(tamano, barcos):
    # Crear los tableros para el jugador y la computadora
    tableroJugador = crearTablero(tamano)
    tableroComputadora = crearTablero(tamano)
    tableroDisparosJugador = crearTablero(tamano)
    tableroDisparosComputadora = crearTablero(tamano)

    print("Coloca tus barcos")
    colocarBarcos(tableroJugador, barcos, "Jugador")
    colocarBarcos(tableroComputadora, barcos, "Computadora")

    turnoJugador = True
    while True:
        if turnoJugador:
            print("Tu turno")
            mostrarTablero(tableroDisparosJugador, tableroDisparosComputadora)
            fila = int(input("Ingresa fila de disparo: "))
            columna = int(input("Ingresa columna de disparo: "))
            resultado = realizarDisparo(tableroComputadora, tableroDisparosJugador, fila, columna)
            print(resultado)
            if verificarVictoria(tableroComputadora):
                print("Lo has conseguido ¡Ganaste!")
                return "Jugador"
        else:
            print("Turno de la computadora")
            fila = random.randint(0, tamano - 1)
            columna = random.randint(0, tamano - 1)
            resultado = realizarDisparo(tableroJugador, tableroDisparosComputadora, fila, columna)
            print(f"La computadora disparó en ({fila},{columna}): {resultado}")
            if verificarVictoria(tableroJugador):
                print("La computadora ha ganado")
                return "Computadora"
        
        turnoJugador = not turnoJugador

def jugarDosJugadores(tamano, barcos):
    tableroJugador1 = crearTablero(tamano)
    tableroJugador2 = crearTablero(tamano)
    tableroDisparosJugador1 = crearTablero(tamano)
    tableroDisparosJugador2 = crearTablero(tamano)

    print("Jugador 1 coloca sus barcos -- ")
    colocarBarcos(tableroJugador1, barcos, "Jugador 1")
    print("Jugador 2 coloca sus barcos -- ")
    colocarBarcos(tableroJugador2, barcos, "Jugador 2")

    turnoJugador1 = True
    while True:
        if turnoJugador1:
            print("Turno del Jugador 1")
            mostrarTablero(tableroDisparosJugador1, tableroDisparosJugador2)
            fila = int(input("Ingrese la fila del disparo: "))
            columna = int(input("Ingrese la columna del disparo: "))
            resultado = realizarDisparo(tableroJugador2, tableroDisparosJugador1, fila, columna)
            print(resultado)
            if verificarVictoria(tableroJugador2):
                print("¡Jugador 1 ha ganado!")
                return "Jugador 1"
        else:
            print("Turno del Jugador 2")
            mostrarTablero(tableroDisparosJugador2, tableroDisparosJugador1)
            fila = int(input("Ingrese la fila del disparo: "))
            columna = int(input("Ingrese la columna del disparo: "))
            resultado = realizarDisparo(tableroJugador1, tableroDisparosJugador2, fila, columna)
            print(resultado)
            if verificarVictoria(tableroJugador1):
                print("¡Jugador 2 ha ganado!")
                return "Jugador 2"
        
        turnoJugador1 = not turnoJugador1

def mostrarMenu():
    print("----------- Bienvendio al Juego Batalla Naval ----------")
    print("1. Elige la dificultad del juego")
    print("2. Jugar contra la computadora")
    print("3. Jugar con dos jugadores")
    print("4. Salir")
    print("----------- Juego producido por TechiesLab ---------")

def iniciarJuego():
    dificultadSeleccionada = False
    tamano = 5
    barcos = [{"nombre": "Barco 1", "tamaño": 2}, {"nombre": "Barco 2", "tamaño": 3}]
    
    while True:
        mostrarMenu()
        opcion = input("Elige la opción deseada: ")

        ganador = None  

        if opcion == "1":
            tamano, num_barcos = seleccionarDificultad()
            barcos = [{"nombre": f"Barco {i+1}", "tamaño": i + 2} for i in range(num_barcos)]
            dificultadSeleccionada = True
            print(f"Dificultad seleccionada: Tablero {tamano}x{tamano}, {num_barcos} barcos.")
        
        elif opcion == "2":
            if dificultadSeleccionada:
                ganador = jugarContracomputador(tamano, barcos)
            else:
                print("Por favor selecciona una dificultad primero.")
        
        elif opcion == "3":
            if dificultadSeleccionada:
                ganador = jugarDosJugadores(tamano, barcos)
            else:
                print("Por favor selecciona una dificultad primero.")
        
        elif opcion == "4":
            print("----- Gracias, Hasta el próximo juego!! -----")
            break
        
        else:
            print("La opción digitada no es válida, selecciona del 1 al 4.")
            continue

        if ganador is not None:
            print(f"El ganador es {ganador}!")

        jugarDeNuevo = input("----- ¿Quieres jugar de nuevo? (s/n) -----").lower()
        if jugarDeNuevo != "s":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break

if __name__ == "__main__":

   iniciarJuego()
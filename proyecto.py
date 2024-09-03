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
            if tablero[fila][columna + i] != "~":
                return False
    else:
        if fila + tamaño > len(tablero):
            return False
        for i in range(tamaño):
            if tablero[fila + i][columna] != "~":
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
        return "Impactó"   
    elif tableroOculto[fila][columna]==" ~ ":
        tableroDisparos[fila][columna]= " O "
        return "Agua"
    return "Ya disparaste aquí"

def verificarVictoria(tableroOculto):
    for fila in tableroOculto:
        if "B" in fila:  
            return False
    return True     

def jugarContracomputador():
    tamano=5
    tableroJugador=crearTablero(tamano)
    tableroComputadora=crearTablero(tamano)
    tableroDisparosJugador=crearTablero(tamano)
    tableroDisparosCompumtadora=crearTablero(tamano)

    barcos=[
        {"nombre": "portaaviones", "tamaño": 3},
        {"nombre": "submarino", "tamaño": 2}
    ]

    print("Colocar tus barcos")
    colocarBarcos(tableroJugador,barcos,"Jugador")
    colocarBarcos(tableroComputadora,barcos,"Computadora")

    turnoJugador=True
    while True:
        if turnoJugador:
           print("Tu turno")
           mostrarTablero(tableroDisparosJugador,tableroDisparosCompumtadora)
           fila=int(input("Ingresa fila de disparo: "))
           columna=int(input("Ingrese columna de disparo: "))
           resultado=realizarDisparo(tableroComputadora,tableroDisparosJugador,fila,columna)
           print(resultado)
           if verificarVictoria(tableroComputadora):
              print("¡Ganaste!")
              return"Jugador"
        
        else:
            print("Turno de la computadora")
            fila=random.randint(0,tamano-1)
            columna=random.randint(0,-1)
            resultado=realizarDisparo(tableroJugador,tableroDisparosCompumtadora,fila,columna)
            print(f"La computadora disparó en ({fila},{columna}) : {resultado}")
            if verificarVictoria(tableroJugador):
                print("La computadora ha ganado")
                return "Computadora"
            
        turnoJugador=not turnoJugador

def jugarDosJugadores():
    tamano=5
    tableroJugador1=crearTablero(tamano)
    tableroJugador2=crearTablero(tamano)
    tableroDisparosJugador1=crearTablero(tamano)
    tableroDisparosJugador2=crearTablero(tamano) 
    barcos=[
        {"nombre": "portaaviones", "tamaño": 3},
        {"nombre": "submarino", "tamaño": 2}
    ]
    print("Jugador 1 coloca sus barcos -- ")
    colocarBarcos(tableroJugador1,barcos,"Jugador")
    print("Jugador 2 coloca sus barcos -- ")
    colocarBarcos(tableroJugador2,barcos,"Jugador")

    turnoJugador1=True
    while True:
            if turnoJugador1:
                print("Turno del jugador 1")
                mostrarTablero(tableroDisparosJugador1,tableroDisparosJugador2)
                fila=int(input("Ingrese la fila del diparo: "))
                columna=int(input("Ingrese la columna del disparo: "))
                resultado=realizarDisparo(tableroJugador2,tableroDisparosJugador1,fila,columna)
                print(resultado)
                if verificarVictoria(tableroJugador2):
                   print("¡Jugador 1 ha ganado!")
                   return "jugador1"
            else:
                print("Turno del jugador2")
                mostrarTablero(tableroDisparosJugador2,tableroDisparosJugador1)
                fila=int(input("Ingrese la fila del diparo: "))
                columna=int(input("Ingrese la columna del disparo"))
                resultado=realizarDisparo(tableroJugador1,tableroDisparosJugador2,fila,columna)
                print(resultado)
                if verificarVictoria(tableroJugador1):
                   print("¡Jugador 2 ha ganado!")
                   return "jugador2"
            turnoJugador1=not turnoJugador1

def mostrarMenu():
    print("----------- Bienvendio al Juego Batalla Naval ----------")
    print("1. Jugar contra la computadora")
    print("2. Jugar con dos jugadores")
    print("3. Salir")
    print("----------- Juego producido por TechiesLab ---------")

def iniciarJuego():
    while True:
        mostrarMenu()
        modo=input("Elige la opción deseada: ")
        if modo== "1":
            ganador= jugarContracomputador()
        elif modo== "2":
            ganador= jugarDosJugadores()
        elif modo== "3":
            print("----- Gracias, Hasta el próximo juego!! -----")
            break
        else:
            print("La opción digita no es valida, seleccione del 1 al 3: ")
            continue
        print(f"El ganador es {ganador}! ")

        jugardeNuevo=input("----- ¿Quieres jugar de nuevo? (s/n) -----").lower()
        if jugardeNuevo!="s":
            print("Gracias por jugar. Hasta el próximo!!")
            break

iniciarJuego()
        



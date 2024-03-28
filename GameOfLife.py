import pygame as pg
import numpy as np
import time

# Inicialización del módulo Pygame
pg.init()

# Dimensiones de la pantalla
WIDTH, HEIGHT = 600, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))

# Color de fondo
bg = 25, 25, 25

# Pintamos el fondo del color elegido
screen.fill(bg)

# Dimensiones de las celdas y estado inicial del juego
nxC, nyC = 25, 25
dimCW = WIDTH / nxC
dimcH = HEIGHT / nyC
gameState = np.zeros((nxC, nyC))

# Control de la ejecución del juego
pauseExect = False

# Bucle principal del juego
while True:
    newGameState = np.copy(gameState)
    
    # Limpiamos la pantalla y añadimos un pequeño retraso para controlar la velocidad de ejecución
    screen.fill(bg)
    time.sleep(0.1)
    
    # Registramos eventos de teclado y ratón
    ev = pg.event.get()
    
    for event in ev:
        # Detectamos si se presiona una tecla
        if event.type == pg.KEYDOWN:
            pauseExect = not pauseExect
        
        # Detectamos si se presiona el ratón
        mauseClik = pg.mouse.get_pressed()
        if sum(mauseClik) > 0:
            posX, posY = pg.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimcH))
            # Cambiamos el estado de la célula al hacer clic
            newGameState[celX, celY] = not mauseClik[2]
            
    for y in range(0, nxC):
        for x in range(0, nyC):
            if not pauseExect:
                # Calculamos el número de vecinos cercanos
                n_neigh = gameState[(x-1) % nxC, (y-1) % nyC] + \
                        gameState[(x)   % nxC, (y-1) % nyC] + \
                        gameState[(x+1) % nxC, (y-1) % nyC] + \
                        gameState[(x-1) % nxC, (y)   % nyC] + \
                        gameState[(x+1) % nxC, (y)   % nyC] + \
                        gameState[(x-1) % nxC, (y+1) % nyC] + \
                        gameState[(x)   % nxC, (y+1) % nyC] + \
                        gameState[(x+1) % nxC, (y+1) % nyC]
                
                # Aplicamos las reglas del juego de la vida de Conway
                
                # Regla 1: Una celula muerta con exactamente 3 vecinas vivas, "revive"
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y]= 1
                
                # Regla 2: Una celula viva con menos de 2 o mas de 3 vecinas vivas, "muere"
                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y]= 0
            
            # Definimos los vértices del polígono que representa la célula
            poly = [((x) * dimCW, y * dimcH),
                    ((x+1) * dimCW, y * dimcH),
                    ((x+1) * dimCW, (y+1) * dimcH),
                    ((x) * dimCW, (y+1) * dimcH)]
            
            # Dibujamos la célula para cada par de x e y
            if newGameState[x, y] == 0:
                pg.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pg.draw.polygon(screen, (255, 255, 255), poly, 0)
                
    # Actualizamos el estado del juego
    gameState = np.copy(newGameState)
        
    # Actualizamos la pantalla
    pg.display.flip()

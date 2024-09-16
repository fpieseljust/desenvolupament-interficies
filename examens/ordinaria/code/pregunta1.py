import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Configurar la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Juego Pygame")

# Definir el jugador (rectángulo rojo)
jugador_ancho = 50
jugador_alto = 50
jugador_x = ANCHO // 2 - jugador_ancho // 2
jugador_y = ALTO - jugador_alto - 10
jugador_velocidad = 5
jugador = pygame.Rect(jugador_x, jugador_y, jugador_ancho, jugador_alto)

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controlar el movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.x -= jugador_velocidad
    if teclas[pygame.K_RIGHT]:
        jugador.x += jugador_velocidad

    # Limitar el movimiento del jugador dentro de la pantalla
    jugador.left = max(0, jugador.left)
    jugador.right = min(ANCHO, jugador.right)

    # Dibujar el jugador en la pantalla
    pantalla.fill(BLANCO)
    pygame.draw.rect(pantalla, ROJO, jugador)

    # Actualizar la pantalla
    pygame.display.flip()
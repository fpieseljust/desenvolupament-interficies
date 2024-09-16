# Examen ordinària Desenvolupament d'interfícies - 2DAM

## Pregunta 1 - PyGame (3 punts)

Donat el següent codi:

```python
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
```

Desenvolupa un joc on van caient en vertical uns enemics de color negre que el jugador haurà d'evitar.

- Les dimensions dels enemics són aleatòries entre 20 i 50 píxels
- La velocitat de desplaçament és aleatòria entre 5 i 20 píxels
- Es crearà un enemic cada 200ms
- Els enemics que ja no ocupen espai en pantalla no s'han de pintar
- En colisionar amb el jugador, el joc acabarà
- El joc ha de ser jugable en qualsevol ordinador

## Pregunta 2 - Flet (3 punts)

Crea una aplicació com la següent.

![type:video](res/login.webm)

## Pregunta 3 - Qt (3 punts)

Utilitzant Qt Designer, dissenyeu una interfície d'usuari per a una aplicació de gestió de tasques bàsica. La interfície ha d'incloure el següent:

- Una llista per mostrar les tasques pendents.
- Un botó per afegir una nova tasca.
- Un botó per eliminar les tasques seleccionades de la llista.
- Un camp de text per introduir noves tasques.

Abans d'eliminar alguna tasca es preguntarà a l'usuari si realment es vol eliminar.

## Pregunta 4 - Instal·lador (1 punt)

Crea un instal·lador de qualsevol de les aplicacions de les preguntes anteriors.
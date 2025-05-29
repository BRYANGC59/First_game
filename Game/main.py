import pygame
from Game.jugador import Jugador

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Inferno Chronicles")

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
ROJO = (200, 0, 0)

fuente = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()

jugador = None
fase = "registro"
nombre_jugador = ""

juego = True
while juego:
    pantalla.fill(NEGRO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego = False

        if fase == "registro":
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nombre_jugador.strip():
                    jugador = Jugador(nombre_jugador.strip())
                    fase = "juego"
                elif evento.key == pygame.K_BACKSPACE:
                    nombre_input = nombre_jugador[:-1]
                else:
                    nombre_jugador += evento.unicode

    if fase == "registro":
        texto = fuente.render("Ingresa tu nombre: " + nombre_jugador, True, BLANCO)
        pantalla.blit(texto, (100, 250))

    elif fase == "juego":
        keys = pygame.key.get_pressed()
        texto_nombre = fuente.render(f"Jugador: {jugador.nombre}", True, BLANCO)
        texto_vida = fuente.render(f"Vida: {jugador.vida}", True, ROJO)
        pantalla.blit(texto_nombre, (20, 20))
        pantalla.blit(texto_vida, (20, 60))

        if keys[pygame.K_LEFT]:
            pantalla.blit(fuente.render("izquierda", True, BLANCO), (200, 300))
        if keys[pygame.K_RIGHT]:
            pantalla.blit(fuente.render("Mueves derecha", True, BLANCO), (200, 340))
        if keys[pygame.K_SPACE]:
            pantalla.blit(fuente.render("Saltas", True, BLANCO), (200, 380))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

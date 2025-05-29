import pygame
from Game.jugador import Jugador
from Game.enemigo import Enemigo_de_fuego

pygame.init()

ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Inferno Chronicles")

BLANCO = (255, 255, 255)
ROJO = (200, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)

fuente = pygame.font.SysFont("Arial", 28)
clock = pygame.time.Clock()

fase = "registro"
nombre_input = ""
mensaje = ""

# Jugador visual (posición del rectángulo)
jugador_pos = pygame.Rect(150, 300, 80, 100)
enemigo_pos = pygame.Rect(550, 300, 80, 100)
velocidad = 5

jugador = None
enemigo = None

corriendo = True
while corriendo:
    pantalla.fill(NEGRO)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

        if fase == "registro":
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN and nombre_input.strip():
                    jugador = Jugador(nombre_input.strip())
                    enemigo = Enemigo_de_fuego()
                    fase = "combate"
                elif evento.key == pygame.K_BACKSPACE:
                    nombre_input = nombre_input[:-1]
                else:
                    nombre_input += evento.unicode

        elif fase == "combate" and evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_e and jugador.esta_vivo() and enemigo.esta_vivo():
                jugador.atacar(enemigo)
                mensaje = f"{jugador.nombre} ataca a {enemigo.nombre}!"
                if enemigo.esta_vivo():
                    enemigo.atacar(jugador)
                    mensaje += f" {enemigo.nombre} contraataca!"

    if fase == "combate":
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            jugador_pos.x -= velocidad
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            jugador_pos.x += velocidad
        jugador_pos.x = max(0, min(ANCHO - jugador_pos.width, jugador_pos.x))

    if fase == "registro":
        pantalla.blit(fuente.render("Ingresa tu nombre y presiona ENTER:", True, BLANCO), (100, 200))
        pantalla.blit(fuente.render(nombre_input, True, AZUL), (100, 250))

    # FASE COMBATE
    elif fase == "combate":
        pygame.draw.rect(pantalla, AZUL, jugador_pos)
        pygame.draw.rect(pantalla, ROJO, enemigo_pos)
        pantalla.blit(fuente.render(f"{jugador.nombre}", True, BLANCO), (jugador_pos.x, jugador_pos.y - 30))
        pantalla.blit(fuente.render(f"{enemigo.nombre}", True, BLANCO), (enemigo_pos.x, enemigo_pos.y - 30))
        pantalla.blit(fuente.render(f"Vida: {jugador.vida}", True, AZUL), (jugador_pos.x, jugador_pos.y + 110))
        pantalla.blit(fuente.render(f"Vida: {enemigo.vida}", True, ROJO), (enemigo_pos.x, enemigo_pos.y + 110))
        pantalla.blit(fuente.render(mensaje, True, BLANCO), (50, 50))

        if not jugador.esta_vivo():
            pantalla.blit(fuente.render("¡Has sido derrotado!", True, ROJO), (250, 200))
            fase = "fin"
        elif not enemigo.esta_vivo():
            pantalla.blit(fuente.render("¡Has vencido al enemigo!", True, AZUL), (250, 200))
            fase = "fin"

    pygame.display.flip()
    clock.tick(30)

pygame.quit()


import sys

import pygame
import constantes
from mundo import Mundo
from personaje import Personaje

#Inicializar el juego
pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO, constantes.ALTO))
pygame.display.set_caption("First Game")

def main():
    clock = pygame.time.Clock()
    mundo = Mundo(constantes.ANCHO, constantes.ALTO)
    personaje = Personaje(constantes.ANCHO // 2, constantes.ALTO // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            personaje.movimientos(-5, 0)
        if keys[pygame.K_RIGHT]:
            personaje.movimientos(5, 0)
        if keys[pygame.K_UP]:
            personaje.movimientos(0, -5)
        if keys[pygame.K_DOWN]:
            personaje.movimientos(0, 5)

        mundo.draw(ventana)
        personaje.draw(ventana)
        pygame.display.flip()

if __name__ == "__main__":
    main()
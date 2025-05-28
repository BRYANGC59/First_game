import os
import random

import pygame


import constantes
from elementos import Enemigo, Roca


class Mundo:
    def __init__(self,  ancho, alto,):
        self.ancho = ancho
        self.alto = alto
        self.enemigo = [Enemigo(random.randint(0, ancho-40),
                                random.randint(0, alto-40)) for _ in range(10)]
        self.Roca = [Roca(random.randint(0, ancho - constantes.ROCA),
                                random.randint(0, alto - constantes.ROCA)) for _ in range(11)]


        cesped_path = os.path.join("recursos", "imagenes", "personajes", "fondo4.png")
        self.cesped_image = pygame.image.load(cesped_path).convert()
        self.cesped_image = pygame.transform.scale(self.cesped_image,
                                                   (constantes.CESPED, constantes.CESPED))



    def draw(self, ventana):
        for y in range(0, self.alto,constantes.CESPED,):
            for x in range(0, self.ancho, constantes.CESPED,):
                ventana.blit(self.cesped_image, (x, y))


        for enemigo in self.enemigo:
            enemigo.draw(ventana)

        for Roca in self.Roca:
            Roca.draw(ventana)

    def draw_inventario(self, pantalla, personaje):
        font = pygame.font.Font(None, 36)
        contador = font.render(f"GEMAS: {personaje.inventario['GEMAS']}", True, constantes.WHITE)

        pantalla.blit(contador, (10,10))
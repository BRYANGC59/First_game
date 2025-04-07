import os
import random

import pygame


import constantes
from elementos import Enemigo


class Mundo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.enemigo = [Enemigo(random.randint(0, ancho-40),
                                random.randint(0, alto-40)) for _ in range(10)]


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

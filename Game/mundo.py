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

    def draw(self, ventana):
        ventana.fill(constantes.GREEN)
        for enemigo in self.enemigo:
            enemigo.draw(ventana)

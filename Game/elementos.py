import random

import pygame

import constantes


class Enemigo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20
        self.gemas = random.randint(1,3)

    def draw(self, ventana):
        pygame.draw.rect(ventana, constantes.BLUE,(self.x, self.y, self.size, self.size))